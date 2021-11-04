from ast import parse
from django.db.models.fields.related import OneToOneField
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect, request
from django.views import View
from django.views.generic.base import RedirectView
from Beryllium.models import Test,Well,Plate,Patient,Tester
from .forms import TestForm, WellForm
from .initializeTest import CreateTest
from django.views.generic import TemplateView
from django.http import JsonResponse
from .calc import Formula
import json
import re

def isWellActive(request, id):
    w = Well.objects.get(id = id)
    if(w.isActive):
        return HttpResponse("True",content_type="text/plain")
    return HttpResponse("False", content_type="text/plain")




class WellPartialView(TemplateView):
    template_name = 'Beryllium/WellPartial_view.html'

    def get_context_data(self, **kwargs):
        well= Well.objects.get(id = kwargs['arg2'])
        result = WellForm(instance = well) 
        kwargs['form'] = result
        return super(WellPartialView, self).get_context_data(**kwargs)
    
    def post(self,request,id):
        instance = Well.objects.get(id = id)
        plate = instance.plate
        test = plate.test
        form = WellForm(request.POST, instance=instance)
        if request.POST:
            if form.is_valid():
               form.save()
        else:
            data ="form not valid"
       
        return HttpResponseRedirect('/Beryllium/TestView/'+str(test.id))


class BeTestWell(View):
    template = 'Beryllium/BeTestWell.html'

    def get(self, request, id):
        try:
            well = Well.objects.get(pk = id)
            print(well)
            form = WellForm(instance = well)
            context = {'form' :form}
            return render (request,self.template,context)
           
        except:
            print("oh no")
            return HttpResponse('<p>well was not found<p>')
    

def WellExcel(request, id):
    template = 'Beryllium/WellExcel.html'
    context = {
        "test" : Test.objects.get(id = id)
    }
   
    return render(request,template,context)

def dashboard(request,id):
    template = 'Beryllium/dashboard.html'
    context = {
        "test" : Test.objects.get(id = id)
    }
   
    return render(request,template)


def getWellsJSON(request, id):
    test = Test.objects.get(id = id)
    plates = Plate.objects.filter(test = test)
    wells = Well.objects.none()
    wellstring = ''

    for p in plates:
        wells |= Well.objects.filter(plate = p)
    
    for w in wells:
        wellstring = wellstring + '{"id":' + str(w.id) +', "plate":' + str(w.plate.num)  +', "row":' + str(w.row)  +', "column":' + str(w.column)  +', "active":' + str(w.isActive) +', "numInTest":' + str(w.numInTest) +', "reading":' + str(w.reading) +"}," 
    
    wellstring = wellstring[:-1:]
    json_data = '{"data":[ ' +wellstring+  ']}'

   # d = json.loads(str(json_data))
    import ast
    d = ast.literal_eval(json_data)
    return JsonResponse(d,safe=False)

def saveWellsJSON(request):
    if request.is_ajax():
        if request.method == 'POST':
            data = str(request.body)
            start = data.find('"data":[') + len('"data":[')
            end = data.find("]}")
            substring = data[start:end]
            data = substring[1:-1]
            ls = data.split("],[")
        for obj in ls:
            print (obj)
            raw = obj.split(",")
            well = Well.objects.get(id = raw[0])
            reading = stringReading = raw[-1]

            try:

                well.reading = int(reading)
                well.save()
            except:
                 
                try:
                    stringReading = raw[-1]
                    reading = stringReading[1:-1]
                    print(stringReading)
                    print(reading)
                    well.reading = int(reading)
                    well.save()
                except:
                     return HttpResponse("Reading is not a number")
            
    return HttpResponse("OK")

def testersView(request):
    template = "Beryllium/testers.html"
    context = {'testers':Tester.objects.all()}

    return render(request,template,context)

def patientsView(request):
    template = "Beryllium/patients.html"
    context = {'patients':Patient.objects.all()}

    return render(request,template,context)


def changeType(request,type):
    request.session["type"] = type
    return redirect('dashboard')



# Create your views here.
class dashboard(View):
    template = 'Beryllium/dashboard.html'
  
    def get(self,request):
        request.session["type"] ="Beryllium"
        form = TestForm()
        patients = Patient.objects.all()
        testers = Tester.objects.all()
        tests = Test.objects.all()

        context = {
            "form" : form,
            "patients" : patients,
            "testers" :testers,
            "tests" : tests,
            "type" : request.session["type"]
        }
        return render(request,self.template,context)
    
    def post(self, request):
        form = TestForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            testId = CreateTest(data['name'],data['patient'],data['tester'])

        return HttpResponseRedirect('/Beryllium/TestView/'+str(testId))

    

class BeTestView(View):
    template = 'Beryllium/BeTest.html'

    def get(self, request,id):


        # Code block for GET request
        try:    
            test = Test.objects.get(id = id)
            plates = Plate.objects.filter(test = test)
            wells = Well.objects.none()
            for p in plates:
                wells |= Well.objects.filter(plate = p)
        except:
            print("oh no")
            test = None


        context = {
         "test" : test,
         "plates" : plates,
         "wells" : wells
         
    }

        return render(request, self.template, context)


        

class TestViewView(View):
    template = 'Beryllium/TestView.html'

    def get(self, request,id):


        # Code block for GET request
        try:    
            beTest = BeTestView
            test = Test.objects.get(id = id)
            plates = Plate.objects.filter(test = test)
            wells = Well.objects.none()
            for p in plates:
                wells |= Well.objects.filter(plate = p)
        except:
            print("oh no")
            test = None


        context = {
         "test" : test,
         "plates" : plates,
         "wells" : wells,
       
         
    }

        return render(request, self.template, context)


class TestCalc(View):
    template = 'Beryllium/TestCalc.html'

    def get(self, request, id):
        test = Test.objects.get(id = id)
        plates = Plate.objects.filter(test = test)
        wells = Well.objects.none()

        
        try:
            f = Formula(test)
        except:
           return HttpResponseRedirect('TestView/'+str(test.id)+'/error')

        dict = f.wellsDict
        stats = f.statsDict
        context = {
            "test" : test,
            "plates" : plates,
            "loop": ['sec1','sec2','sec3','sec4'],
            "wells": wells,
            "stats" : stats,
            "resultDict" : f.resultDict,
            "controlDict" : f.controlDict
        }
        
        return render(request, self.template,context)


def getSecJSON(request,id ,num,sec):
    test = Test.objects.get(id = id)
    plates = Plate.objects.filter(test = test)
    from .calc import Formula
    f = Formula(test)
    dict = f.wellsDict
    lst = dict[num][sec]
    wellstring = ''


    for w in lst:
        wellstring = wellstring + '{"numInTest":' + str(w.numInTest) +', "reading":' + str(w.reading) +"}," 
    
    wellstring = wellstring[:-1:]
    json_data = '{"data":[ ' +wellstring+  ']}'

   # d = json.loads(str(json_data))
    import ast
    d = ast.literal_eval(json_data)
    return JsonResponse(d,safe=False)

def exportDoc(request,id):
    test = Test.objects.get(id = id)
    f = Formula(test)
    isNormal = request.POST["isNormal"]=='Yes'
    isPositive = request.POST["isPositive"]=='Positive'
    profession = request.POST["Profession"]
    
    respone = f.exportToDoc(isNormal,isPositive,profession)
  
 
    return respone


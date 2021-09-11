from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect, request
from django.views import View
from Beryllium.models import Test,Well,Plate
from .forms import TestForm, WellForm
from .initializeTest import CreateTest
from django.views.generic import TemplateView
from django.http import JsonResponse
import json


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
       
        return HttpResponseRedirect('/Beryllium/BeTest/'+str(test.id))


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
   
    return render(request,template)

def getWellsJSON(request, id):
    test = Test.objects.get(id = id)
    plates = Plate.objects.filter(test = test)
    wells = Well.objects.none()
    wellstring = ''

    for p in plates:
        wells |= Well.objects.filter(plate = p)
    
    for w in wells:
        wellstring = wellstring + '{"id":' + str(w.id) +', "active":' + str(w.isActive) +"}," 
    
    wellstring = wellstring[:-1:]
    json_data = '{"data":[ ' +wellstring+  ']}'

   # d = json.loads(str(json_data))
    import ast
    d = ast.literal_eval(json_data)
    return JsonResponse(d,safe=False)


def deleteTests(self):
    Test.objects.all().delete()

    return HttpResponseRedirect('index')


# Create your views here.
class index(View):
    template = 'Beryllium/index.html'
  
    def get(self,request):
        form = TestForm()

        context = {
            "form" : form,
        }
        return render(request,self.template,context)
    
    def post(self, request):
        form = TestForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            testId = CreateTest(data['name'],data['patient'],data['tester'])

        return HttpResponseRedirect('BeTest/'+str(testId))

    

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


   
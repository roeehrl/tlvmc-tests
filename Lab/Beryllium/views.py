from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from Beryllium.models import Test,Well,Plate
from .forms import TestForm, WellForm
from .initializeTest import CreateTest
from django.views.generic import TemplateView

class PartialView(TemplateView):
    template_name = 'Beryllium/partial_view.html'

    def get_context_data(self, **kwargs):
        result = WellForm(instance = Well.objects.get(id = kwargs['arg2'])) 
        kwargs['form'] = result
        return super(PartialView, self).get_context_data(**kwargs)

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
            "well" : Well.objects.get(id = 1403)
        }
        return render(request,self.template,context)
    
    def post(self, request):
        form = TestForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            testId = CreateTest(data['testName'],data['patient'],data['tester'])

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
        

    def post(self, request):
        # Code block for POST request
        pass
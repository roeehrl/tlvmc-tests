from time import timezone
from typing import List
from .models import Test, Plate, Plate_Type,Well,Material, Patient,Tester
import django.utils.timezone

#returns a plate type based on given plate number
def InitPlateType (num : int):
    p = Plate_Type()

    if( num == 1):
        p.id = 41
        p.days = 4
        p.classification = 1
    
    if(num ==2):
        p.id = 42
        p.days = 4
        p.classification = 2
    
    if( num == 3):
        p.id = 61
        p.days = 6
        p.classification = 1
    
    if(num == 4):
        p.id = 62
        p.days = 6
        p.classification = 2

    p.save()
    return p


        
def AddWellsToPlate (plate : Plate):
    pt = plate.plate_type
    if(plate.populated == 2):
        if(pt.days == 4):
            if(pt.classification == 1):
                for x in range(1,31):
                    w = Well()
                    w.numInPlate = x
                    w.plate = plate
                    w.isActive = False
                    w.dosage = 0
                    w.material = Material.objects.get(name = 'empty')
                    w.save()
          
        
        if(pt.days == 4):
                if(pt.classification == 2):
                    for x in range(1,21):
                        w = Well()
                        w.numInPlate = x
                        w.plate = plate
                        w.isActive = False
                        w.dosage = 0
                        w.material = Material.objects.get(name = 'empty')
                        w.save()
             
    
        if(pt.days == 6):
                if(pt.classification == 1):
                    for x in range(1,31):
                        w = Well()
                        w.numInPlate = x
                        w.plate = plate
                        w.isActive = False
                        w.dosage = 0
                        w.material = Material.objects.get(name = 'empty')
                        w.save()
    
    
        if(pt.days == 6):
                if(pt.classification == 2):
                    for x in range(1,21):
                        w = Well()
                        w.numInPlate = x
                        w.plate = plate
                        w.isActive = False
                        w.dosage = 0
                        w.material = Material.objects.get(name = 'empty')
                        w.save()
                    
                   
    plate.populated = 1
    plate.save()
        
def numerizeWellsInTest(test: Test):
    counter = 1
    for p in Plate.objects.filter(test = test):
        for w in Well.objects.filter(plate = p):
            w.numInTest = counter
            w.save()
            counter += 1




def CreateEmptyTest(name, p : Patient, t : Tester):
    test = Test(tester = t, patient = p)
    test.patient = p
    test.tester = t
    test.date = django.utils.timezone.now()
    test.name = name

    test.save()

    for x in range(1,5):
        plate = Plate ()
        plate.plate_type = InitPlateType(x)
        plate.test = test
        plate.num = x
        plate.save()
        AddWellsToPlate(plate)
        numerizeWellsInTest(test)

    return test.id






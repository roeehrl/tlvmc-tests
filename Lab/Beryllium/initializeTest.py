from time import timezone
from typing import List
from .models import Test, Plate, Plate_Type,Well,Material, Patient,Tester
import django.utils.timezone

def main():
    
    p = Patient(id = '318772969',first_name = 'Roee', last_name = 'Harel' )
    t = Tester(id = '839882769',first_name = 'Eyal', last_name = 'Kelner')
    p.save()
    t.save()
   
    Material(id = 1, name = 'empty').save()
    Material(id = 2, name='Beryllium').save()
    Material(id = 3, name='PHA').save()
    Material(id = 4, name='PWM').save()


    CreateTest(p,t)




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

# add wells to plate based on plate's type
def AddWellsToPlate (plate : Plate):
    pt = plate.plate_type
    if(plate.populated == 2):
        if(pt.days == 4):
            if(pt.classification == 1):
                counter = 1
                for x in range(1,16):
                    w = Well()
                    w.numInPlate = x
                    w.plate = plate
                    w.isActive = True
                    w.dosage = 0
                    w.material = Material.objects.get(name = 'empty')
                    
                    w.save()
            
                for x in range (16,21):
                    w = Well()
                    w.numInPlate = x
                    w.plate = plate
                    w.isActive = True
                    w.dosage = -4
                    w.material = Material.objects.get(name = 'Beryllium')
                    w.save()
                
                for x in range (21,26):
                    w = Well()
                    w.numInPlate = x
                    w.plate = plate
                    w.isActive = True
                    w.dosage = -5
                    w.material = Material.objects.get(name = 'Beryllium')
                    w.save()
                
                for x in range (26,31):
                    w = Well()
                    w.numInPlate = x
                    w.plate = plate
                    w.isActive = True
                    w.dosage = -6
                    w.material = Material.objects.get(name = 'Beryllium')
                    w.save()
        
        if(pt.days == 4):
                if(pt.classification == 2):
                    for x in range(1,6):
                        w = Well()
                        w.numInPlate = x
                        w.plate = plate
                        w.isActive = True
                        w.dosage = 0
                        w.material = Material.objects.get(name = 'empty')
                        w.save()
                
                    for x in range (6,11):
                        w = Well()
                        w.numInPlate = x
                        w.plate = plate
                        w.isActive = True
                        w.dosage = 20
                        w.material = Material.objects.get(name = 'PHA')
                        w.unitOfMeasure = 'ul'
                        w.save()
                    
                    for x in range (11,16):
                        w = Well()
                        w.numInPlate = x
                        w.plate = plate
                        w.isActive = True
                        w.dosage = 30
                        w.material = Material.objects.get(name = 'PHA')
                        w.unitOfMeasure = 'ul'
                        w.save()
                    
                    for x in range (16,21):
                        w = Well()
                        w.numInPlate = x
                        w.plate = plate
                        w.isActive = True
                        w.dosage = 40
                        w.unitOfMeasure = 'ul'
                        w.material = Material.objects.get(name = 'PHA')
                        w.save()
    
        if(pt.days == 6):
                if(pt.classification == 1):
                    for x in range(1,16):
                        w = Well()
                        w.numInPlate = x
                        w.plate = plate
                        w.isActive = True
                        w.dosage = 0
                        w.material = Material.objects.get(name = 'empty')
                        w.save()
                
                    for x in range (16,21):
                        w = Well()
                        w.numInPlate = x
                        w.plate = plate
                        w.isActive = True
                        w.dosage = -4
                        w.material = Material.objects.get(name = 'Beryllium')
                        w.save()
                    
                    for x in range (21,26):
                        w = Well()
                        w.numInPlate = x
                        w.plate = plate
                        w.isActive = True
                        w.dosage = -5
                        w.material = Material.objects.get(name = 'Beryllium')
                        w.save()
                    
                    for x in range (26,31):
                        w = Well()
                        w.numInPlate = x
                        w.plate = plate
                        w.isActive = True
                        w.dosage = -6
                        w.material = Material.objects.get(name = 'Beryllium')
                        w.save()
    
        if(pt.days == 6):
                if(pt.classification == 2):
                    for x in range(1,6):
                        w = Well()
                        w.numInPlate = x
                        w.plate = plate
                        w.isActive = True
                        w.dosage = 0
                        w.material = Material.objects.get(name = 'empty')
                        w.save()
                
                    for x in range (6,11):
                        w = Well()
                        w.numInPlate = x
                        w.plate = plate
                        w.isActive = True
                        w.dosage = 0.002
                        w.material = Material.objects.get(name = 'PWM')
                        w.unitOfMeasure = 'ug'
                        w.save()
                    
                    for x in range (11,16):
                        w = Well()
                        w.numInPlate = x
                        w.plate = plate
                        w.isActive = True
                        w.dosage = 0.01
                        w.material = Material.objects.get(name = 'PWM')
                        w.unitOfMeasure = 'ug'
                        w.save()
                    
                    for x in range (16,21):
                        w = Well()
                        w.numInPlate = x
                        w.plate = plate
                        w.isActive = True
                        w.dosage = 0.02
                        w.material = Material.objects.get(name = 'PWM')
                        w.unitOfMeasure = 'ug'
                        w.save()
    plate.populated = 1
    plate.save()

def numerizeWellsInTest(test: Test):
    counter = 1
    colcount =1
    rowcount =1
    
    for p in Plate.objects.filter(test = test):
        rowcount = 1
        wells =  Well.objects.filter(plate = p)
        for w in wells:
            w.numInTest = counter
            w.column = colcount
            w.row = rowcount
            w.save()
            counter += 1
            colcount +=1
            if colcount == 6:
                colcount = 1
                rowcount += 1





def CreateTest(name, p : Patient, t : Tester):
    test = Test(tester = t, patient = p)
    test.patient = p
    test.tester = t
    test.type = 1
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

    printTest(test)
    return test.id

def printTest (test : Test):
    for p in Plate.objects.filter(test = test):
        print(p)




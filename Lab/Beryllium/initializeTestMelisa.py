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
        p.id = 11
        p.days = None
        p.classification = 1
    
    if(num ==2):
        p.id = 12
        p.days = None
        p.classification = 2
    
    if( num == 3):
        p.id = 13
        p.days = None
        p.classification = 3
    
    if(num == 4):
        p.id = 14
        p.days = None
        p.classification = 4
    
    if(num == 4):
        p.id = 15
        p.days = None
        p.classification = 5

    p.save()
    return p

# add wells to plate based on plate's type
def AddWellsToPlate (plate : Plate):
    pt = plate.plate_type
    if(plate.populated == 2):
            if(pt.classification == 1):
                counter = 1
                for x in range(1,4):
                    w = Well()
                    w.numInPlate = x
                    w.plate = plate
                    w.isActive = True
                    w.dosage = 0
                    w.material = Material.objects.get(name = 'empty')
                    
                    w.save()
            
                for x in range (4,7):
                    w = Well()
                    w.numInPlate = x
                    w.plate = plate
                    w.isActive = True
                    w.dosage = -4
                    w.material = Material.objects.get(name = 'Zn')
                    w.save()
                
                for x in range (7,10):
                    w = Well()
                    w.numInPlate = x
                    w.plate = plate
                    w.isActive = True
                    w.dosage = -5
                    w.material = Material.objects.get(name = 'Ni')
                    w.save()
                
                for x in range (10,13):
                    w = Well()
                    w.numInPlate = x
                    w.plate = plate
                    w.isActive = True
                    w.dosage = None
                    w.material = Material.objects.get(name = 'Co')
                    w.save()
        
                for x in range(13,16):
                        w = Well()
                        w.numInPlate = x
                        w.plate = plate
                        w.isActive = True
                        w.dosage = None
                        w.material = Material.objects.get(name = 'Cu')
                        w.save()
                
                for x in range (16,19):
                        w = Well()
                        w.numInPlate = x
                        w.plate = plate
                        w.isActive = True
                        w.dosage = None
                        w.material = Material.objects.get(name = 'Cr')
                        w.unitOfMeasure = None
                        w.save()
                    
                for x in range (19,22):
                        w = Well()
                        w.numInPlate = x
                        w.plate = plate
                        w.isActive = True
                        w.dosage = None
                        w.material = Material.objects.get(name = 'Al')
                        w.unitOfMeasure = None
                        w.save()
                    
                for x in range (22,25):
                        w = Well()
                        w.numInPlate = x
                        w.plate = plate
                        w.isActive = True
                        w.dosage = None
                        w.unitOfMeasure = None
                        w.material = Material.objects.get(name = 'TiS')
                        w.save()
            if(pt.classification == 2):
                counter = 1
                for x in range(1,4):
                    w = Well()
                    w.numInPlate = x
                    w.plate = plate
                    w.isActive = True
                    w.dosage = 0
                    w.material = Material.objects.get(name = 'empty')
                    
                    w.save()
            
                for x in range (4,7):
                    w = Well()
                    w.numInPlate = x
                    w.plate = plate
                    w.isActive = True
                    w.dosage = None
                    w.material = Material.objects.get(name = 'TiO')
                    w.save()
                
                for x in range (7,10):
                    w = Well()
                    w.numInPlate = x
                    w.plate = plate
                    w.isActive = True
                    w.dosage = None
                    w.material = Material.objects.get(name = 'Ba')
                    w.save()
                
                for x in range (10,13):
                    w = Well()
                    w.numInPlate = x
                    w.plate = plate
                    w.isActive = True
                    w.dosage = None
                    w.material = Material.objects.get(name = 'Zr')
                    w.save()
        
                for x in range(13,16):
                        w = Well()
                        w.numInPlate = x
                        w.plate = plate
                        w.isActive = True
                        w.dosage = None
                        w.material = Material.objects.get(name = 'W')
                        w.save()
                
                for x in range (16,19):
                        w = Well()
                        w.numInPlate = x
                        w.plate = plate
                        w.isActive = True
                        w.dosage = None
                        w.material = Material.objects.get(name = 'Mo')
                        w.unitOfMeasure = None
                        w.save()
                    
                for x in range (19,22):
                        w = Well()
                        w.numInPlate = x
                        w.plate = plate
                        w.isActive = True
                        w.dosage = None
                        w.material = Material.objects.get(name = 'In')
                        w.unitOfMeasure = None
                        w.save()
                    
                for x in range (22,25):
                        w = Well()
                        w.numInPlate = x
                        w.plate = plate
                        w.isActive = True
                        w.dosage = None
                        w.unitOfMeasure = None
                        w.material = Material.objects.get(name = 'Mn')
                        w.save()

            if(pt.classification == 3):
            
                counter = 1
                for x in range(1,4):
                    w = Well()
                    w.numInPlate = x
                    w.plate = plate
                    w.isActive = True
                    w.dosage = 0
                    w.material = Material.objects.get(name = 'empty')
                    
                    w.save()
            
                for x in range (4,7):
                    w = Well()
                    w.numInPlate = x
                    w.plate = plate
                    w.isActive = True
                    w.dosage = None
                    w.material = Material.objects.get(name = 'Pb')
                    w.save()
                
                for x in range (7,10):
                    w = Well()
                    w.numInPlate = x
                    w.plate = plate
                    w.isActive = True
                    w.dosage = None
                    w.material = Material.objects.get(name = 'Hg')
                    w.save()
                
                for x in range (10,13):
                    w = Well()
                    w.numInPlate = x
                    w.plate = plate
                    w.isActive = True
                    w.dosage = None
                    w.material = Material.objects.get(name = 'Au')
                    w.save()
        
                for x in range(13,16):
                        w = Well()
                        w.numInPlate = x
                        w.plate = plate
                        w.isActive = True
                        w.dosage = None
                        w.material = Material.objects.get(name = 'Vn')
                        w.save()
                
                for x in range (16,19):
                        w = Well()
                        w.numInPlate = x
                        w.plate = plate
                        w.isActive = True
                        w.dosage = None
                        w.material = Material.objects.get(name = 'Fe')
                        w.unitOfMeasure = None
                        w.save()
            if(pt.classification == 4):
                counter = 1
                for x in range(1,4):
                    w = Well()
                    w.numInPlate = x
                    w.plate = plate
                    w.isActive = True
                    w.dosage = 0
                    w.material = Material.objects.get(name = 'empty')
                    
                    w.save()
            
                for x in range (4,7):
                    w = Well()
                    w.numInPlate = x
                    w.plate = plate
                    w.isActive = True
                    w.dosage = None
                    w.material = Material.objects.get(name = 'Si')
                    w.save()
                
                for x in range (7,10):
                    w = Well()
                    w.numInPlate = x
                    w.plate = plate
                    w.isActive = True
                    w.dosage = None
                    w.material = Material.objects.get(name = 'GroundSi')
                    w.save()
                
                for x in range (10,13):
                    w = Well()
                    w.numInPlate = x
                    w.plate = plate
                    w.isActive = True
                    w.dosage = None
                    w.material = Material.objects.get(name = 'Sn')
                    w.save()
            if(pt.classification == 5):
                counter = 1
                for x in range(1,4):
                    w = Well()
                    w.numInPlate = x
                    w.plate = plate
                    w.isActive = True
                    w.dosage = 0
                    w.material = Material.objects.get(name = 'empty')
                    
                    w.save()
            
                for x in range (4,7):
                    w = Well()
                    w.numInPlate = x
                    w.plate = plate
                    w.isActive = True
                    w.dosage = 0.1
                    w.material = Material.objects.get(name = 'PWM')
                    w.unitOfMeasure='ug'
                    w.save()
                
                for x in range (7,10):
                    w = Well()
                    w.numInPlate = x
                    w.plate = plate
                    w.isActive = True
                    w.dosage = 0.05
                    w.material = Material.objects.get(name = 'PWM')
                    w.unitOfMeasure='ug'
                    w.save()
                
                for x in range (10,13):
                    w = Well()
                    w.numInPlate = x
                    w.plate = plate
                    w.isActive = True
                    w.dosage = 0.01
                    w.material = Material.objects.get(name = 'PWM')
                    w.unitOfMeasure='ug'
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
    test.type = 2
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




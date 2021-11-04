from django.db import models
from django.db.models.deletion import CASCADE, DO_NOTHING

# Create your models here.

class Test_type(models.Model):
    name = models.CharField(max_length=200, null=True)

class Patient (models.Model):
    id = models.CharField(max_length=12, primary_key=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

    def __str__(self):
        return self.first_name + " " + self.last_name

class Tester (models.Model):
    id = models.CharField(max_length=12, primary_key=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.first_name + " " + self.last_name


class Test (models.Model):
    name = models.CharField(max_length=200)
    tester = models.ForeignKey(Tester,on_delete=DO_NOTHING)
    patient = models.ForeignKey(Patient, on_delete=DO_NOTHING)
    type = models.ForeignKey(Test_type, on_delete=DO_NOTHING, default=1)
    date = models.DateField()
    description = models.CharField(max_length= 1000)

   
        

class Plate_Type (models.Model):
    TEST = 1
    CONTROL = 2
    CLAS = (
       (TEST, ('test')),
       (CONTROL, ('control')),
    )
    
    classification = models.PositiveSmallIntegerField(
       choices=CLAS,
       default=TEST,
   )
    days = models.IntegerField(null=True)

class Plate (models.Model):
    YES = 1
    NO = 2
    POP = (
       (YES, ('populated')),
       (NO, ('empty')),
    )
    test = models.ForeignKey(Test, on_delete=CASCADE)
    num = models.IntegerField()
    plate_type = models.ForeignKey(Plate_Type, on_delete=DO_NOTHING)
    populated = models.PositiveSmallIntegerField(
       choices=POP,
       default=NO,
   )


class Material (models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Well (models.Model):
    plate = models.ForeignKey(Plate, on_delete=CASCADE)
    numInPlate = models.IntegerField()
    numInTest = models.IntegerField(null=True)
    row = models.IntegerField(null = True)
    column = models.IntegerField(null = True)
    isActive = models.BooleanField()
    material = models.ForeignKey(Material, on_delete= DO_NOTHING)
    dosage = models.FloatField()
    unitOfMeasure = models.CharField(max_length=200, default='mg')
    reading = models.FloatField(default=0)
    
   



from .models import Test, Plate, Plate_Type,Well,Material, Patient,Tester

class modelServices:

    def getWellsforPlate(plate : Plate):
        return Well.objects.filter(plate = plate)





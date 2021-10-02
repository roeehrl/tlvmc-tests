import statistics
from .models import Test, Plate,Well

class Formula():

    def __init__(self,t:Test):
        self.test = t

        self.wellsDict = {}
        self.statsDict = {}
        
        for p in Plate.objects.filter(test = self.test):
            wells = Well.objects.filter(plate = p)
            dos = wells[0].dosage
            counter = 1
            sec = []
         
            self.statsDict[p.num] = {"sec"+str(counter): {}}
            stats = self.statsDict[p.num]
            self.wellsDict[p.num] = {"sec"+str(counter): []}
            dic = self.wellsDict[p.num]
            first_avg = None

            for w in wells:
                if(w.dosage == dos):
                    sec.append(w)
                    dic["sec"+str(counter)] =  []
                    dic["sec"+str(counter)] = sec
                    dos = w.dosage
                   
                    if(counter == 4):
                        
                        stats["sec"+str(counter)]["avg"] = self.average(sec)
                        stats["sec"+str(counter)]["st_dev"] = self.st_dev(sec)
                        stats["sec"+str(counter)]["si"]  =  stats["sec"+str(counter)]["avg"]/first_avg
                       


                else:
                    stats["sec"+str(counter)]["avg"] = self.average(sec)
                    stats["sec"+str(counter)]["st_dev"] = self.st_dev(sec)
                    if(counter >1):
                        stats["sec"+str(counter)]["si"]  =  stats["sec"+str(counter)]["avg"]/first_avg
                    else:
                        first_avg = stats["sec"+str(counter)]["avg"]

                    counter = counter +1
                    sec = []
                    sec.append(w)
                    stats["sec"+str(counter)] = {}
                    dic["sec"+str(counter)] =  []
                    dic["sec"+str(counter)] = sec
                    dos = w.dosage
    
        self.resultDict = {
            "4D" :
        {"BeSO4 100uM [1X10-4]": self.statsDict[1]["sec2"]["si"], "BeSO4 10uM [1X10-5]": self.statsDict[1]["sec3"]["si"] ,"BeSO4 1uM [1X10-6]": self.statsDict[1]["sec4"]["si"]},
       
        "6D" :
        {"BeSO4 100uM [1X10-4]": self.statsDict[3]["sec2"]["si"], "BeSO4 10uM [1X10-5]": self.statsDict[3]["sec3"]["si"],"BeSO4 1uM [1X10-6]": self.statsDict[3]["sec4"]["si"]}
        }

        self.controlDict ={
            "4-PHA" : self.controlStat(self.statsDict[2]) ,
            "6-PWM" : self.controlStat(self.statsDict[4])
        }
    
    def controlStat(self, s :dict):
        ls = []
        counter = 1
        for key,value in s.items():
            print(key,value)
            if counter>1:
             ls.append(value["si"])
            counter = counter +1
        return max(ls)



    def average(self,lst):
        nums = []
        for w in lst:
            nums.append(w.reading)

        return sum(nums) / len(nums)

    def st_dev(self,lst):
        nums = []
        for w in lst:
            nums.append(w.reading)

        return statistics.stdev(nums)


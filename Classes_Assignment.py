class Vehicle:

    def __init__(self,make,model,year,weight):
        self.make = make
        self.model = model
        self.year = year
        self.weight = weight
        self.TripSinceMaintenance = 0
        self.NeedsMaintenance = False

    def carMake(self, make):
        self.make = make
    
    def carModel(self, model):
        self.model = model

    def carYear(self, year):
        self.year = year

    def carWeight(self, weight):
        self.weight = weight

    def repair(self):
        self.NeedsMaintenance = False
        self.TripSinceMaintenance = 0


# inheritance class of car
class Cars(Vehicle):

    def __init__(self,make,model,year,weight,isDriving):
        Vehicle.__init__(self,make,model,year,weight)
        self.isDriving = isDriving

    def drive(self,isDriving):
        self.isDriving = True
        
    def stop(self,isDriving):
        self.isDriving = False

    def switch(self,isDriving):
        if self.isDriving == True:
            self.isDriving = False
            self.TripSinceMaintenance += 1
        elif self.isDriving == False:
            self.isDriving = True
            
        if self.TripSinceMaintenance > 100:
            self.NeedsMaintenance = True

    def __str__(self):
        return self.make + " " + self.model + " of year " + str(self.year) + " model had ran " + str(self.TripSinceMaintenance) + " number of Trips. Does this car need maintenance at this point? - " + str(self.NeedsMaintenance)

Toyota = Cars("Toyota","Corolla",2019,"1000kg",True)
Benz = Cars("Mercedes-Benz","4_Matic",2020,"1300kg",True)
BMW = Cars("BMW","300Series",2010,"1155kg",True)

print(Toyota)
print(Benz)
print(BMW)

Toyota.drive(True)
Benz.drive(True)
BMW.drive(True)


# inheritance class of plane
class Plane(Vehicle):

    def __init__(self,make,model,year,weight,isFlying):
        Vehicle.__init__(self,make,model,year,weight)
        self.isFlying = False

    def flying(self):
        if self.NeedsMaintenance:
            print("This airplane needs repairs and cannot take-off")
        else:
            self.isFlying = True
            self.TripSinceMaintenance += 1
        

    def landing(self, isFlying):
        self.isFlying = False

    def __str__(self):
        return self.make + " " + self.model + " of year " + str(self.year) + " model had ran " + str(self.TripSinceMaintenance) + " number of Trips. Does this aircraft need maintenance at this point? - " + str(self.NeedsMaintenance)

Boeing = Plane("Boeing","737_max",2000,"10000000kg",True)

print(Boeing)

Boeing.NeedsMaintenance = True
Boeing.flying()
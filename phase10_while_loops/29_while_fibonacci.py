from abc import ABC, abstractmethod 
class Vehicle:
    def start(self):
        print("Vehicle is starting...")
    
    @abstractmethod
    def VehicleNo(self):
        print(123)
class Car(Vehicle):
    def drive(self):
        print("Car is driving")

c = Car()
c.start()
c.drive()
c.VehicleNo()
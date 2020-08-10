from datetime import date
from datetime import datetime
from datetime import time

class Car:
    def startEngine(self):
        print("Starting the engine")

    def accelerate(self):
        print("Accelerate the car")

    def deaccelerate(self):
        print("Deaccelerate the car")

class Hatchback(Car):
    def startEngine(self):
        Car.startEngine(self)
        print("Starting the hatchback engine")

    def accelerate(self):
        print("Accelerate the hatchback car")

    def deaccelerate(self):
        print("Deaccelerate the hatchback car")


def testObject():
    car = Car()
    car.startEngine()
    car.accelerate()
    car.deaccelerate()

    hCar = Hatchback()
    hCar.startEngine()
    hCar.accelerate()
    hCar.deaccelerate()

    today = date.today()
    print("Today is ", today)

    # Date format: %y/%Y - Year, %a/%A - Weekday, %b/%B - Month, %d - day of month
    now = datetime.now()
    print(now.strftime("%a, %d, %B, %y"))    

# The following code snippet tells this file should start as the main script
if __name__ == "__main__":
    testObject()        
from datetime import date
from datetime import datetime
from datetime import time
import sys

class Car:
    # Class variables
    x = [1, 2]
    noOfWheels = 4

    def __init__(self, color, type, brand):
        # Object variables
        self._color = color
        self._type = type
        self._brand = brand

    def startEngine(self):
        print("Starting the engine")

    def accelerate(self):
        print("Accelerate the car")

    def deaccelerate(self):
        print("Deaccelerate the car")

class Hatchback(Car):
    def __init__(self, color, brand):
        super().__init__(color, "Hatchback", brand)

    def startEngine(self):
        Car.startEngine(self)
        print("Starting the hatchback engine")

    def accelerate(self):
        print("Accelerate the hatchback car")

    def deaccelerate(self):
        print("Deaccelerate the hatchback car")

class inclusive_range:
    def __init__(self, *args):
        arg_length=len(args)
        self._start = 0
        self._step = 1

        if (arg_length < 1):
            raise TypeError(f'except at least one arguments')
        elif (arg_length == 1):
            self._stop = args[0]
        elif (arg_length == 2):
            (self._start, self._stop) = args
        elif (arg_length == 3):
            (self._start, self._stop, self._step) = args
        else:
            raise TypeError(f'expect maximum 3 arguments')
    
        self._next = self._start

    def __iter__(self):
        return self

    def __next__(self):
        if (self._next > self._stop):
            raise StopIteration
        else:
            value = self._next
            self._next += self._step
            return value


def testObject():
    car = Car("red", "sedan", "hyundai")
    car.startEngine()
    car.accelerate()
    car.deaccelerate()

    hCar = Hatchback("blue", "honda")
    hCar.startEngine()
    hCar.accelerate()
    hCar.deaccelerate()

    today = date.today()
    print("Today is ", today)

    # Date format: %y/%Y - Year, %a/%A - Weekday, %b/%B - Month, %d - day of month
    now = datetime.now()
    print(now.strftime("%a, %d, %B, %y"))    

    for v in inclusive_range(5, 23, 3):
        print(v, end=' ')

    try:
        val = int('test')
    except ValueError:
        print('ValueError is thrown')
    except ZeroDivisionError:
        print('ZeroDivisionError is thrown')
    except:
        print(f'Unknown error: {sys.exc_info()}')
    else:
        print('No error')

# The following code snippet tells this file should start as the main script
if __name__ == "__main__":
    testObject()        
class Car:
    def start(self):
        print("brum brum")

def start_car(car):
    car.start()

start_car("hello world") # This does not work!

car = Car()
start_car(car) # This does work!
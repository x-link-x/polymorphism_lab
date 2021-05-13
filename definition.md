There are different types of object (e.g. strings, list, or self-defined classes).

Polymorphism is a system by which objects of different types can be given to the same function.

A polymorphic function can take different types of object.
A non-polymorphic function can only take one type of object.

example of a polymorphic function:
```Python
print("Hello")
print([1, 2, 3])
```
example of a non-polymorphic function:
```Python
class Car:
    def start(self):
        print("brum brum")

def start_car(car):
    car.start()

start_car("hello world") # This does not work!

car = Car()
start_car(car) # This does work!

```
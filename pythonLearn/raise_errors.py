# Errors
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def __repr__(self):
        return f'<Car {self.make}, {self.model}>'


class Garage:
    def __init__(self):
        self.cars = []

    def __len__(self):
        return len(self.cars)

    def add_car(self, car):
        if not isinstance(car, Car):
            raise TypeError(f"Tried to add a {car.__class__.__name__} to Garage but expected instance of Car")
        else:
            self.cars.append(car)


car = Car("Ford", "Focus")
car2 = Car("Toyota", "Rav4")
garage = Garage()
garage.add_car(car)
garage.add_car(car2)
print(len(garage))

print(garage.cars)
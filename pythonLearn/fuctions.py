# functions
car1 = {
    "make": "Ford",
    "model": "Fiesta",
    "mileage": 23900,
    "fuel_consumed": 345
}


def calculate_mpg(car):
    mpg = car["mileage"] / car["fuel_consumed"]
    name = f"{car['make']} {car['model']}"
    print(f"{name} has {mpg} miles per gallon")


calculate_mpg(car1)
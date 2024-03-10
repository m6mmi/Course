# import datetime to get current year
from datetime import date


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    # calculate car age
    def age_old(self):
        # get current year
        current_year = date.today().year
        return current_year - self.year


class ElectricCar(Car):
    def __init__(self, make, model, year, bat_cap_new):
        # values from car
        super().__init__(make, model, year)
        self.bat_cap_new = bat_cap_new

    # calculate estimated remaining battery capacity based on age
    def remaining_bat_cap(self):
        # average battery degradation is 2,3 % per year
        bat_cap_left = 100 - self.age_old() * 2.3
        return bat_cap_left


# function to print out car details
def announce(car):
    print(f"Make:  {car.make}\n"
          f"Model: {car.model}\n"
          f"Year:  {car.year}\n"
          f"This car is {car.age_old()} years old.")
    # if car has battery value then print left capacity
    try:
        print(f"Estimated remaining battery capacity is {car.remaining_bat_cap()} %")
    except AttributeError:
        pass
    print()


# create car objects
car1 = Car("Skoda", "Kodiaq", 2022)
car2_e = ElectricCar("Tesla", "Model 3", 2020, 100)

# print empty line
print()
# announce cars
announce(car1)
announce(car2_e)



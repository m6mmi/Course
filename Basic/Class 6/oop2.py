class Car:
    def __init__(self, brand, fuel_tank,speed , engine=1.6):
        self.brand = brand
        self.fuel = fuel_tank
        self.engine = engine
        self.speed = speed

    def drive(self):
        self.fuel -= 10

    def __str__(self):
        return f"Brand: {self.brand}, {self.fuel} l in the tank, current speed {self.speed}"


car1 = Car("VW", 60, 90)  # uses default engine class value. In this case it is 1.6
car2 = Car("Opel", 55, 78,  2.0)

# print("This is car 1 fuel tank:", car1.fuel)
# print("This is car 2 fuel tank:", car2.fuel)
#
# print("-" * 20)
#
# print("Car driving")
# car1.drive()
# car2.drive()
#
# print("-" * 20)
#
# print("This is car 1 fuel tank:", car1.fuel)
# print("This is car 2 fuel tank:", car2.fuel)
#
# print("-" * 20)
# car1.print_details()
# car2.print_details()

print(car1)
print(car2)

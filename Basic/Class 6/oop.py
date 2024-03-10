class Car:
    def __init__(self, brand, fuel_tank, engine=1.6):
        self.brand = brand
        self.fuel = fuel_tank
        self.engine = engine

    def drive(self):
        self.fuel -= 10

    def print_details(self):
        print(f"{self.brand} has fuel tank {self.fuel} liters and {self.engine}L engine")


car1 = Car("VW", 60)  # uses default engine class value. In this case it is 1.6
car2 = Car("Opel", 55, 2.0)

print("This is car 1 fuel tank:", car1.fuel)
print("This is car 2 fuel tank:", car2.fuel)

print("-" * 20)

print("Car driving")
car1.drive()
car2.drive()

print("-" * 20)

print("This is car 1 fuel tank:", car1.fuel)
print("This is car 2 fuel tank:", car2.fuel)

print("-" * 20)
car1.print_details()
car2.print_details()

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Square(Rectangle):
    def __init__(self, length):
        self.width = length
        self.length = length

    def perimeter(self):
        return (self.width + self.length) * 2

print()
x = int(input("Enter x: "))
y = int(input("Enter y: "))
print()
while True:
    if x != y:
        print(f"Area: {Rectangle(x, y).area()}")
        break
    elif x == y:
        print(f"Area: {Square(x).area()}")
        print(f"Perimeter: {Square(x).perimeter()}")
        break
    else:
        print("Something went wrong !! ")

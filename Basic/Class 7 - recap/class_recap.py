class RocketShip:
    def __init__(self, fuel, lenght):
        self.fuel = fuel
        self.length = lenght

    def __gt__(self, other):
        return self.length > other.length

    def __eq__(self, other):
        return self.fuel == other.fuel

    def __str__(self):
        return str(self.fuel)

    def __contains__(self, item):
        if self.fuel:
            return True


rocket_1 = RocketShip(1200, 20)
rocket_2 = RocketShip(1200, 10)

print(rocket_1 > rocket_2)
print(rocket_1 < rocket_2)
print(rocket_1 == rocket_2)
print(rocket_1 != rocket_2)
print(rocket_1)
print(rocket_2)
print('fuel' in rocket_1)

variable = range(50, 101, 10)
for i in variable:
    print(variable)

number = [i for i in range(0, 100, 25)]
print(number)


def better_conditional(num=18):
    if num < 18:
        return "mina"
    # elif num == 18:
    #     return "equal"
    return "sina"


print(better_conditional())  # sina
print(better_conditional(10))  # mina
print(better_conditional(20))  # sina



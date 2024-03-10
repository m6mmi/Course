# while condition:
# #     instruction
# print(1)
# # print(2)
# # print(3)
# # print(4)
# # print(5)

# number = 0
# while number <= 100:
#     print(number)
#     number += 1
# --------------------------------------------------------------------------------------------
# while True:
#     user_input = input("a - for addition, s - for substraction, x - to Quit: ").lower()
#     if user_input == 'a':
#         print(f"2+2={2+2}")
#     elif user_input == 's':
#         print(f"2-2{2-2}")
#     elif user_input == 'x':
#         print("Thank you using our services")
#         break
#     else:
#         print("Text was wrong, try on of possible options")
# --------------------------------------------------------------------------------------------
# for condition:
#     instructions
cars = ["VW", "Audi", "BMW"]
# print(cars[0], cars[1], cars[2])
#
# for car in cars:
#     print(car, end=" ")
# print()
#
# for index, car in enumerate(cars):
#     print(index, car)
#
# some_text = "This is,!  a very cool text!"
# new_text = ""
# for char in some_text:
#     if char == 'e':
#         new_text += char.upper()
#     elif char in "xlT":
#         new_text += "@"
#     else:
#         new_text += char
# print(new_text)
#
# for word in some_text.split():
#     print(word.strip("!, "))

# variable = range(5, 101,20)
# print(list(variable))

# for number in range(5, 100, 20):
#     print(number)

for index, car in enumerate(cars):
    print(car)

number = [i for i in range(100)]
print(number)


# --------------------------------------------------------------------------------------------
# do:
# instruction
# while condition




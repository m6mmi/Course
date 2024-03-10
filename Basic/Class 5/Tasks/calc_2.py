print("Hello, Welcome to calculator 2.0")

while True:
    number_one = int(input("Please provide first number: "))
    number_two = int(input("Please provide second number: "))
    action = input("Select action to do: \n"
                   "a - Add \n"
                   "s - Subtract\n"
                   "d - Divide \n"
                   "m - Multiply\n"
                   "> ")

    if action == 'a':
        print(f"The sum of these numbers is", number_one + number_two)
    elif action == 's':
        print(f"The subtraction of these numbers is",  number_one - number_two)
    elif action == 's':
        print(f"The division of these numbers is", number_one / number_two)
    elif action == 's':
        print(f"The multiplication of these numbers is", number_one * number_two)

    is_again = input("Would you calculate more? Y or N:")
    if is_again.lower() == "y":
        continue
    break

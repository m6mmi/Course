while True:
    try:
        x = int(input("Enter x = "))
        y = int(input("Enter y = "))
        action = input("Action: (+, -, /, *) ")

        if action not in ['+', '-', '/', '*']:
            print("Invalid action! Please enter one of '+', '-', '/', '*'")
            continue

        if action == "+":
            result = x + y
        elif action == "-":
            result = x - y
        elif action == "/":
            if y == 0:
                print("Cannot divide by zero!")
                continue
            result = x / y
        elif action == "*":
            result = x * y

        print(f"{x} {action} {y} = {round(result, 2)}")
    except ValueError:
        print("Invalid input! Please enter valid integers.")

    more = input("Do you want to calculate more? (y/n) ")
    if more.lower() != "y":
        break

user_dict = [
    {
        "name": "Janek",
        "age": 38,
        "country": "Estonia",
        "potatoes": 10000
    }
]

while True:
    print("1. Register new user\n"
          "2. Display users\n"
          "Q. Exit program")
    choice = input("> ")
    if choice.isnumeric():
        if int(choice) == 1:
            name = input("\nEnter name: ")
            age = int(input("Enter age: "))
            country = input("Enter country: ")
            potatoes = int(input("How many potatoes consumed yesterday: "))
            user_dict.append({"name": name.capitalize(), "age": age, "country": country.capitalize(), "potatoes": potatoes})
            print("Thank you for your input\n")
        elif int(choice) == 2 and len(user_dict) != 0:
            print()
            for n, user in enumerate(user_dict, start=1):
                print(f'{n}: {user["name"]}')
            user_choice = int(input("Enter the number of the user you want to view: "))
            if 1 <= user_choice <= len(user_dict):
                user_info = user_dict[user_choice - 1]
                print(f"The participant {user_info['name']}, aged {user_info['age']} years old, "
                      f"coming from {user_info['country']} have destroyed {user_info['potatoes']} potatoes yesterday.\n")
            else:
                print("Invalid user number. Please try again.\n")
        else:
            print("Invalid choice. Please enter a valid option.\n")
    elif choice.upper() == 'Q':
        break
    else:
        print("Invalid input. Please enter a valid option.\n")


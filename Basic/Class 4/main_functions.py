def greet(name):
    print(f"Welcome to potato eating register, {name}!")


def get_action():
    print()
    print("1 - Add new entry")
    print("2 - Display all entries")
    print("3 - Exit the program")
    user_input = input("Choose your action: ")

    return user_input


def get_entry_details():
    print()
    name = input("Please state your name: ")
    age = input("Please state your age: ")
    city = input("Where are you from: ")
    amount_of_potatoes = input("How many potatoes did you down yesterday: ")
    print(f"Thanks {name}, your record of {amount_of_potatoes} potatoes eaten is now recorded!")

    return f"The participant {name}, aged {age} years old, coming from {city} have destroyed {amount_of_potatoes} potatoes!"


def show_entries(entries):
    print()
    for entry in entries:
        print(entry)


print(__name__)


if __name__ == "__main__":
    greet("Some random text")
    show_entries(['text1', 'text2'])


import json
from icecream import ic

# load json file
with open('dict.json', 'r') as f:
    data = f.read()
    janek = json.loads(data)


def main():
    # Ask user input
    user_input = input("\nDo you want to: \n"
                "1. Read\n"
                "2. Write\n"
                "3. My info\n"
                "4. Family names\n"
                "5. Auto format info\n"
                "6. Exit\n"
                "Choose nr: ")
    action(user_input)


def action(choice):
    match choice:
        case "1":
            ic(janek)
            main()
        case "2":
            print("Work in progress.")
            # with open('dict.json', 'w') as f:
            #     print(json.dumps(janek, indent=4), file=f)
            main()
        case "3":
            print(f"Name: {janek['first_name']}")
            print(f"Surname: {janek['last_name']}")
            print(f"Age: {janek['age']}")
            print(f"Status: {janek['married']}")
            main()
        case "4":
            x = 0
            for i in janek['family']:
                print(janek['family'][x]['name'])
                x += 1
            main()
        case "5":
            for key, value in janek.items():
                print(f'{key}: {value}')
            main()
        case "6":
            print('Have a nice day :)')


main()

while True:
    number_of_cats = input("Please provide number: ")
    if number_of_cats.isnumeric():
        number_of_cats = int(number_of_cats)
        if 20 > number_of_cats >= 0:
            animal = 'cats' if (number_of_cats > 1 or number_of_cats == 0) else 'cat'
            print(f'Alice have {number_of_cats} {animal}')
            break
        elif number_of_cats >= 20:
            print('Alice has a cat shelter')
            break

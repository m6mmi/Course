import json

janek = {
    'first_name': 'Janek',
    'last_name': 'Sitsmann',
    'age': 38,
    'married': True,
    'address': [
        {
            'country': 'Estonia',
            'county': 'Jõgevamaa',
            'street': 'Männi',
            'index': '48103'
        }
    ],
    'family': [
        {
            'name': 'Riina',
            'age': 34,
            'married': True
        },
        {
            'name': 'Elis',
            'age': 13,
            'married': False
        },
        {
            'name': 'Maiken',
            'age': 7,
            'married': False
        }
    ],
    'pets': [
        {
            'type': 'cat',
            'name': 'Mia'
        },
        {
            'type': 'dog',
            'name': 'Sweety'
        }
    ],
    'cars': ['Renault', 'Audi', 'Skoda']
}

# janek['cars'].append('Opel')
# print(janek['cars'])
print(janek['family'])
print(janek['family'][0])
temp_list = janek['family']
x = 0
while x < len(temp_list):
    temp_dict = temp_list[x]
    for i in temp_dict:
        print(i.capitalize(), temp_dict[i])
    x += 1


# x = 0
# while x < len(janek.get('cars')):
#     print(janek['cars'][x])
#     x += 1
#
# for i in janek['cars']:
#     print(i)

# animal = janek['pets'][0].get('type')
# name = janek['pets'][0].get('name')


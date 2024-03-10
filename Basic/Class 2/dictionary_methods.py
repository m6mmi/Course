import json
from icecream import ic
sample_dict = {
    "name": "Eimantas",
    "age": 30,
    "city": "Vilnius",
    "cats": ["Yoda", "Obi"],
    "family": [
        {
            "name": "Janek",
            "age": 38
        },
        {
            "name": "Riina",
            "age": 34
        }
    ],
    "car": "Skoda",
    "married": True
}
print(sample_dict)
sample_dict['favorite_color'] = "Green"
sample_dict['age'] += 10
sample_dict['cats'].append('Mia')
print(sample_dict)
print(sample_dict['cats'])
print(sample_dict['cats'][0])
print(sample_dict['family'][0]['age'])
print(sample_dict.get('city'))
print(sample_dict.get('food', 'No food in dictionary'))

del sample_dict['favorite_color']
deleted_value = sample_dict.pop('city')
print(f"Deleted value: {deleted_value}")
print(sample_dict)

print(len(sample_dict))
print(len(sample_dict["family"]))
print(len(sample_dict["cats"]))
# print(json.dumps(sample_dict, indent=4))
# print(sample_dict.values())

# for key in sample_dict:
#     if type(sample_dict[key]) is list:
#         counter = 0
#         length = len(sample_dict[key])
#         print(f'{key}: ', end="")
#         while counter < length:
#             if counter < length:
#                 print(sample_dict[key][counter], end=", ")
#                 counter += 1
#             else:
#                 print(sample_dict[key][counter])
#                 counter += 1
#
#
#     else:
#         print(f'{key}: {sample_dict[key]}')

# for key, value in sample_dict.items():
#     print(f'{key}: {value}')
#
# print(sample_dict['family'][0])
# print()
# for key, value in sample_dict['family'][0].items():
#     print(f'{key}: {value}')
# print()
# for key, value in sample_dict['family'][1].items():
#     print(f'{key}: {value}')
#
# print('Cats: ',end="")
# for value in sample_dict['cats']:
#     print(f'{value}', end=", ")
# print()
# ic(sample_dict)

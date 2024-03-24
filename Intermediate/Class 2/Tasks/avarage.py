import json

with open('data.json', 'r') as f:
    data = json.load(f)


def get_average(*args):
    return sum(args) / len(args)


print(f'Left side average:  {get_average(*data['left_side']):.2f}')
print(f'Right side average: {get_average(*data['right_side']):.2f}')
print(f'Total average:      {get_average(*data['left_side'], *data['right_side']):.2f}')

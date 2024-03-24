import csv
import json

with open('music.csv', 'r') as f:
    data = [row for row in csv.DictReader(f)]


new_dict_list = []
for line in data:
    new_dict = {}
    for i in line:
        if line[i].strip().isnumeric():
            new_dict[i.strip()] = int(line[i].strip())
        else:
            new_dict[i.strip()] = line[i].strip()
    new_dict_list.append(new_dict)

with open('music.json', 'w') as f:
    json.dump(new_dict_list, f, indent=4)

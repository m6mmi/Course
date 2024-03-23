import json

with open('json_source.json', 'r') as f:
    data = json.load(f)

# print(json.dumps(data, indent=4))


with open('json_output.json', 'w') as output:
    json.dump(data, output, indent=4)

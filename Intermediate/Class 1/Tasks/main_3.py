import csv
import json
import requests
from time import time

t1_start = time()
def convert_list(list, key='name'):
    new_list = []
    for item in list:
        r_item = requests.get(item, headers={"User_Agent": user_agent})
        new_list.append(r_item.json()[key])
    return new_list


def process_data(data):
    for person in data:
        homeworld = person['homeworld']
        r_homeworld = requests.get(homeworld, headers={"User_Agent": user_agent})
        person['homeworld'] = r_homeworld.json()['name']

        person['films'] = convert_list(person['films'], 'title')
        person['species'] = convert_list(person['species'])
        person['vehicles'] = convert_list(person['vehicles'])
        person['starships'] = convert_list(person['starships'])

    return data


user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'

try:
    r = requests.get('https://swapi.dev/api/people/', headers={'User_Agent': user_agent})
    results = process_data(r.json()['results'])
    next_page = r.json()['next']
    while next_page is not None:
        r = requests.get(next_page, headers={'User_Agent': user_agent})
        results.extend(process_data(r.json()['results']))
        next_page = r.json()['next']

except Exception as e:
    print(e)
    results = {}

with open('sw_output_detailed.csv', 'w', newline='', encoding='UTF-8') as f:
    headers = results[0].keys()
    writer = csv.DictWriter(f, fieldnames=headers)

    writer.writeheader()
    writer.writerows(results)

t1_stop = time()

print(t1_stop - t1_start)


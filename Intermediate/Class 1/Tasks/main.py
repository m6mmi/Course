import csv
import json
import requests

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'

try:
    r = requests.get('https://swapi.dev/api/people/', headers={'User_Agent': user_agent})
    results = r.json()['results']
    next_page = r.json()['next']
    while next_page is not None:
        r = requests.get(next_page, headers={'User_Agent': user_agent})
        results.extend(r.json()['results'])
        next_page = r.json()['next']

except Exception as e:
    print(e)
    results = {}

with open('sw_output.json', 'w') as f:
    json.dump(results, f, indent=4)

with open('sw_output.csv', 'w', newline='', encoding='UTF-8') as f:
    headers = results[0].keys()
    writer = csv.DictWriter(f, fieldnames=headers)

    writer.writeheader()
    writer.writerows(results)




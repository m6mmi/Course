import json
import requests

base_api = 'https://swapi.dev/api'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'

try:
    r = requests.get(f'{base_api}/people', headers={'User_Agent': user_agent})
    results = r.json()['results']

except Exception as e:
    print(e)
    results = {}

with open('api_output.json', 'w') as f:
    json.dump(results,f,  indent=4)




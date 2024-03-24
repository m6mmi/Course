from datetime import datetime, timedelta
import requests
import json

today = datetime.today().day
tomorrow = (datetime.today() + timedelta(1)).day

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
base_api = f'https://dashboard.elering.ee/api/nps/price?start=2024-03-{today}T21%3A59%3A59.999Z&end=2024-03-{tomorrow}T21%3A59%3A59.999Z'

r = requests.get(base_api, headers={'User_Agent': user_agent})
results = r.json()['data']['ee']

for hour in results:
    print(f"{datetime.fromtimestamp(hour['timestamp'])} | {'=' * int(hour['price'])}> {hour['price']} €")

price_list = [data['price'] for data in results]

print(price_list)

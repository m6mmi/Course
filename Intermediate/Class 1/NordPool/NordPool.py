from datetime import datetime, timedelta
import requests

if datetime.today().hour >= 15:
    today = datetime.today().day
    tomorrow = (datetime.today() + timedelta(1)).day
else:
    today = (datetime.today() - timedelta(1)).day
    tomorrow = datetime.today().day

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
base_api = f'https://dashboard.elering.ee/api/nps/price?start=2024-03-{today}T22%3A59%3A59.999Z&end=2024-03-{tomorrow}T22%3A59%3A59.999Z'

r = requests.get(base_api, headers={'User_Agent': user_agent})
results = r.json()['data']['ee']

for hour in results:
    print(f"{datetime.fromtimestamp(hour['timestamp'])} | {'=' * int(hour['price'])}> {hour['price']} €")

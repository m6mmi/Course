import csv
import json
import requests

def process_data(data):
    for person in data:
        homeworld = person['homeworld']
        r_homeworld = requests.get(homeworld, headers={"User_Agent": user_agent})
        person['homeworld'] = r_homeworld.json()['name']

        films = person['films']
        new_films = []
        for film in films:
            r_film = requests.get(film, headers={"User_Agent": user_agent})
            new_films.append(r_film.json()['title'])
        person['films'] = new_films

        species = person['species']
        new_species = []
        for specie in species:
            r_specie = requests.get(specie, headers={"User_Agent": user_agent})
            new_species.append(r_specie.json()['name'])
        person['species'] = new_species

        vehicles = person['vehicles']
        new_vehicles = []
        for vehicle in vehicles:
            r_vehicle = requests.get(vehicle, headers={"User_Agent": user_agent})
            new_vehicles.append(r_vehicle.json()['name'])
        person['vehicles'] = new_vehicles

        starships = person['starships']
        new_starships = []
        for starship in starships:
            r_starship = requests.get(starship, headers={"User_Agent": user_agent})
            new_starship = requests.get(r_starship.json()['name'])
        person['starships'] = new_starships

    return data


user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'

try:
    r = requests.get('https://swapi.dev/api/people/', headers={'User_Agent': user_agent})
    results = process_data(r.json()['results'])
    next_page = r.json()['next']
    # while next_page is not None:
    #     r = requests.get(next_page, headers={'User_Agent': user_agent})
    #     results.extend(process_data(r.json()['results']))
    #     next_page = r.json()['next']

except Exception as e:
    print(e)
    results = {}

# with open('sw_output_detailed.csv', 'w', newline='', encoding='UTF-8') as f:
#     headers = results[0].keys()
#     writer = csv.DictWriter(f, fieldnames=headers)
#
#     writer.writeheader()
#     writer.writerows(results)

print(results)


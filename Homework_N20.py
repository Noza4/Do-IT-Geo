import requests
import json


endpoint = 'https://rickandmortyapi.com/api/character'

response = requests.get(endpoint)
page_quantity = response.json()['info']['pages']
data = dict()

for page in range(1, 15): # 15 გვერდის მერე მონაცემები აღარ მოაქვს სწორად, ლიმიტს აღწევს ჩემი აზრით
    new_endpoint = f'{endpoint}?page={page}'
    response = requests.get(new_endpoint)
    characters = response.json()['results']
    for character in characters:
        data[character['name']] = []
        for ep in character['episode']:
            data[character['name']].append(ep.split('/')[-1])


with open('file.json', 'w') as json_file:
    json_file.write(json.dumps(data, indent=4))


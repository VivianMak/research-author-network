import requests
import json

API_KEY=""
with open('api_key.txt') as keyfile:
    API_KEY = keyfile.read()

with open('titles.json', 'r') as file:
    print("READING JSON FILES OF PAPER TITLES....")
    data = json.load(file)

r = requests.post(
    'https://api.semanticscholar.org/graph/v1/paper/batch',
    params={'fields': 'authors,referenceCount,citationCount,title'},
    json=data
)
print(json.dumps(r.json(), indent=2))


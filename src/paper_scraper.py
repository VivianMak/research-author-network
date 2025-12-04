import requests
import json
from network import *

API_KEY=""
with open('api_key.txt') as keyfile:
    API_KEY = keyfile.read()

with open('data/initial_data.json', 'r') as file:
    INIT_DATA = json.load(file)

network = NetworkGraph()

IDS = {
    "5201322": "Sarah Spence Adams",
    "1769552": "Brad Minch",
    "2002806": "Victoria Preston",
    "50058359": "David Shuman",
    "134901850": "Zachary del Rosario",
    "35474768": "Rachel Yang",
    "66274227": "Kene Mbanisi",
    "2291589240": "Steve Matsumoto",
    "5226037": "Sam Michalka"
}


def scrape_initial_profs():
    with open('data/prof_author_ids.json', 'r') as file:
        print("READING JSON FILES OF AUTHORS....")
        data = json.load(file)

    r = requests.post(
        'https://api.semanticscholar.org/graph/v1/author/batch',
        params={'fields': 'papers.authors'},
        json=data
    )

    with open("data/initial_data.json", "w") as f:
        json.dump(r.json(), f, indent=2)


def find_prof_network(prof_idx, depth):
    collab_data = []
    collab_ids = []
    author_id = INIT_DATA[prof_idx]['authorId']
    papers = INIT_DATA[prof_idx]['papers']
    for p in papers:
        for a in p['authors']:
            collab_data.append({
                "authorId": a['authorId'], 
                "name": a['name']
                })
            collab_ids.append(a['authorId'])
    
    with open("data/p.json", "w") as f:
        json.dump(collab_data, f, indent=2)


find_prof_network(0, 1)


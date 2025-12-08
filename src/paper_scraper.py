import requests
import json
import time
from network import *

API_KEY=""
with open('api_key.txt') as keyfile:
    API_KEY = keyfile.read()

with open('data/initial_data.json', 'r') as file:
    INIT_DATA = json.load(file)

network = NetworkGraph()

PROF_IDS = {
    "5201322": "Sarah Spence Adams",
    # "1769552": "Brad Minch",
    # "2002806": "Victoria Preston",
    # "50058359": "David Shuman",
    # "134901850": "Zachary del Rosario",
    # "35474768": "Rachel Yang",
    # "66274227": "Kene Mbanisi",
    # "2291589240": "Steve Matsumoto",
    # "5226037": "Sam Michalka"
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


def find_author_collabs(author_id, papers):
    collab_ids = []
    # author_id = INIT_DATA[prof_idx]['authorId']
    # papers = INIT_DATA[prof_idx]['papers']
    for p in papers:
        for collaborator in p['authors']:
            if collaborator['authorId'] != author_id:
                collab_ids.append(collaborator['authorId'])
            # collab_data.append({
            #     "authorId": a['authorId'], 
            #     "name": a['name']
            #     })
    return collab_ids
    
    # with open("data/p.json", "w") as f:
    #     json.dump(collab_data, f, indent=2)

def split_list(lst, chunk_size):
    return [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]

def find_papers(author_list):
    # Example with a list of 50 elements
    all_papers = []
    chunked_list = split_list(author_list, 100)
    for chunk in chunked_list:

        r = requests.post(
            'https://api.semanticscholar.org/graph/v1/author/batch',
            params={'fields': 'papers.authors'},
            json={"ids":chunk}
        )
        all_papers.extend(r.json())

    with open("data/papers_test.json", "w") as f:
        json.dump(all_papers, f, indent=2)

    return all_papers

# print(type(find_papers(['5201322'])))
# print(type(INIT_DATA))
# print(find_papers(['5201322', '1769552']))

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
    "66274227": "Kene Mbanisi",
    # "2291589240": "Steve Matsumoto",
    # "5226037": "Sam Michalka"
}


def scrape_initial_profs():
    '''
    Scrape papers of initial professors
    '''
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
    '''
    Find all direct collaborations of a specified author using the 
    list of all their papers previously scraped
    
    :param author_id: string of digits representing an author ID
    :param papers: list of papers scraped from the API containing multiple
    authors' papers
    '''
    collab_ids = []
    for p in papers:
        for collaborator in p['authors']:
            if collaborator['authorId'] != author_id and collaborator['authorId'] is not None:
                collab_ids.append(collaborator['authorId'])
    return collab_ids

def split_list(lst, chunk_size):
    "Split list into chunks"
    return [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]

def find_papers(author_list):
    '''
    Find all papers in a batch API call for a list of author IDs
    
    :param author_list: list of string author IDs
    '''
    all_papers = []
    chunked_list = split_list(author_list, 100)
    for chunk in chunked_list:

        r = requests.post(
            'https://api.semanticscholar.org/graph/v1/author/batch',
            params={'fields': 'papers.authors'},
            json={"ids":chunk}
        )
        all_papers.extend(r.json())
        time.sleep(1)

    return all_papers

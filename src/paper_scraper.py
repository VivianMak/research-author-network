import requests
import json
import time

API_KEY=""
with open('api_key.txt') as keyfile:
    API_KEY = keyfile.read()

with open('data/initial_data.json', 'r') as file:
    INIT_DATA = json.load(file)

# Uncomment professors to query
PROF_IDS = {
    # "5201322": "Sarah Spence Adams",
    # "1769552": "Brad Minch",
    "2002806": "Victoria Preston",
    # "50058359": "David Shuman",
    # "134901850": "Zachary del Rosario",
    # "35474768": "Rachel Yang",
    "66274227": "Kene Mbanisi",
    # "2291589240": "Steve Matsumoto",
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


def find_author_collabs(author_id, papers):
    collab_ids = []

    for p in papers:
        for collaborator in p['authors']:
            if collaborator['authorId'] != author_id:
                collab_ids.append(collaborator['authorId'])

    return collab_ids

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
        time.sleep(1)

    with open("data/papers_test.json", "w") as f:
        json.dump(all_papers, f, indent=2)
    print("done")

    return all_papers

def get_name(id_list):
    """
    Given a list of author ids, return a list of author names
    """
    
    r = requests.post(
        "https://api.semanticscholar.org/graph/v1/author/batch",
        params={"fields": "name"},
        json={"ids": id_list}
    )

    authors = r.json()
    name_list = [a["name"] for a in authors if a.get("name")]

    return name_list


import json
import time
from network import NetworkGraph
from paper_scraper import INIT_DATA, PROF_IDS, find_author_collabs, find_papers
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import visualization
import a_star

def main():
    graph = NetworkGraph()
    # author = "vp"
    # collabs = ["bm", "rw"]

    papers = find_papers(list(PROF_IDS.keys()))
    for i, (prof_id, prof_name) in enumerate(PROF_IDS.items()):
        print(f"Finding {prof_name}'s collaborators...")
        # papers = INIT_DATA[i]['papers']
        collabs = find_author_collabs(prof_id, papers[i]['papers'])

        # Check if author exists yet fr depth 0
        if not graph.check_author(prof_id):
            graph.add_new_author(prof_id)

        # Add author's list of collborations
        graph.add_author_collab(prof_id, collabs)

        
        depth = 1
        scan_list = collabs
        while depth > 0:
            all_indirect_collabs = []
            print(f"Scanning depth {depth}...")
            depth = depth - 1
            indirect_papers = find_papers(scan_list)
            # print(indirect_papers)
            for j, col in enumerate(scan_list):
                if j % 50 == 0:
                    print(col)
                # print(col)
                try:
                    p = indirect_papers[j]['papers']
                except TypeError:
                    print(f"id: {col}")
                    print(f"index: {j}")
                indirect_collabs = find_author_collabs(col, p)
                graph.add_author_collab(col, indirect_collabs)
                all_indirect_collabs.extend(indirect_collabs)
            # for col in scan_list:
            #     print(col)
            #     indirect_papers = find_papers(col)
            #     indirect_collabs = find_author_collabs(col, indirect_papers)

            scan_list = all_indirect_collabs

    # Print out adjacency matrix
    df = graph.get_collabs()
    graph.save_matrix_as_csv("test1")

    edges = graph.get_neighbors("5201322")
    print(f"the neighbors of Sarah are {edges}")

    edges2 = graph.get_neighbors("5226037")
    print(f"the neighbors of Sam are {edges2}")



    # # Build graph from adjacency matrix
    # A = df.values
    # G = nx.from_numpy_array(A, create_using=nx.DiGraph)

    # # Relabel nodes with author IDs
    # mapping = {i: name for i, name in enumerate(graph.author_ids)}
    # G = nx.relabel_nodes(G, mapping)

    # # Network graph
    # visualization.visualize(G)

    # # shortest path
    # path = a_star.find_path("5201322", "5226037", graph)
    # print("Shortest path:", path)

if __name__ == "__main__":
    main()

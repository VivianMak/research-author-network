from network import NetworkGraph
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import visualization

from a_star import find_path
from search2 import create_adjacency_collab
from network import NetworkGraph
from bk_clique import BK
from paper_scraper import PROF_IDS


def main():
    
    graph = NetworkGraph()

    create_adjacency_collab(graph, 1)

    # graph.save_matrix_as_csv("test1")

    # Cliques
    # bk = BK(graph, PROF_IDS)
    # _ = bk.get_maximal_cliques()

    # new_mat = bk.remake_adjacency()

    # print(new_mat)
    
    # Shortest Path: A-star
    path = find_path("5201322", "66274227", graph)
    print("Shortest path:", path)

    # Visualization

    # Build graph from adjacency matrix
    df = graph.get_collabs()
    A = df.values
    G = nx.from_numpy_array(A, create_using=nx.DiGraph)

    # Relabel nodes with author IDs
    mapping = {i: name for i, name in enumerate(graph.author_ids)}
    G = nx.relabel_nodes(G, mapping)

    # color graph based on profs
    for prof in PROF_IDS.keys():
        neighbors = graph.get_neighbors(prof)
        for n in neighbors:
            G.nodes[n[0]]['prof_group'] = prof
    
    for node in G.nodes:
        if 'prof_group' not in G.nodes[node]:
            G.nodes[node]['prof_group'] = 'none'


    # Get the 'club' attribute for each node
    club_labels = nx.get_node_attributes(G, 'prof_group')
    print(club_labels)

    # 2. Map the categorical club labels to specific colors
    # The two clubs are 'Mr. Hi' and 'Officer'
    # We will use 'blue' for 'Mr. Hi' and 'red' for 'Officer'
    color_map_dict = {
        '5201322': 'blue',
        '66274227': 'red',
        'none': 'gray'
    }

    # 3. Create a list of colors for all nodes, ensuring order matches the nodes in G.nodes()

    node_colors = [color_map_dict[club_labels[node]] for node in G.nodes()]

    # Network graph
    visualization.visualize(G, node_colors)

    


if __name__ == "__main__":
    main()


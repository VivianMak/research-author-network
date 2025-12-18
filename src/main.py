from network import NetworkGraph
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import visualization

from a_star import find_path
from search import create_adjacency_collab
from network import NetworkGraph
from bk_clique import BK
from paper_scraper import PROF_IDS


def main():
    
    graph = NetworkGraph()

    create_adjacency_collab(graph, 1)

    # graph.save_matrix_as_csv("big2")

    # Cliques
    bk = BK(graph, PROF_IDS)
    _ = bk.get_maximal_cliques()

    new_mat = bk.remake_adjacency()

    # print(new_mat)
    
    # Shortest Path: A-star
    for key in PROF_IDS.keys():
        path = find_path("5201322", "1769552", graph)
        print("Shortest path:", path)

    # Visualization

    # Build graph from adjacency matrix
    df = graph.get_collabs()
    A = df.values
    G = nx.from_numpy_array(A, create_using=nx.Graph)

    # Relabel nodes with author IDs
    mapping = {i: name for i, name in enumerate(graph.author_ids)}
    G = nx.relabel_nodes(G, mapping)

    PATHS = [
        ("5201322", "1769552"), 
        ("5201322", "2002806"),
        ("5201322", "66274227"),
        ("1769552", "2002806"),
        ("1769552", "66274227"),
        # ("66274227", "2002806")
    ]

    # Network graph
    for path_pair in PATHS:
        path = find_path(path_pair[0], path_pair[1], graph)
        print("Shortest path:", path)
        visualization.visualize(G, path)


if __name__ == "__main__":
    main()


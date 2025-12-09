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

    create_adjacency_collab(graph)

    # Cliques
    bk = BK(graph, PROF_IDS)
    _ = bk.get_maximal_cliques()
    
    # Shortest Path: A-star
    path = find_path("2002806", "66274227", graph)
    print("Shortest path:", path)

    # Visualization

    # # Build graph from adjacency matrix
    # A = df.values
    # G = nx.from_numpy_array(A, create_using=nx.DiGraph)

    # # Relabel nodes with author IDs
    # mapping = {i: name for i, name in enumerate(graph.author_ids)}
    # G = nx.relabel_nodes(G, mapping)

    # # Network graph
    # visualization.visualize(G)

    


if __name__ == "__main__":
    main()


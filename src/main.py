from network import NetworkGraph
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import visualization


def main():
    graph = NetworkGraph()
    author = "vp"
    collabs = ["bm", "rw"]

    # Check if author exists yet fr depth 0
    if not graph.check_author(author):
        graph.add_new_author(author)

    # Add author's list of collaborations
    graph.add_author_collab(author, collabs)

    # Print out adjacency matrix
    df = graph.get_collabs()
    edges = graph.get_neighbors("bm")
    print(f"the neighbors of bm are {edges}")

    # Build graph from adjacency matrix
    A = df.values
    G = nx.from_numpy_array(A, create_using=nx.DiGraph)

    # Relabel nodes with author IDs
    mapping = {i: name for i, name in enumerate(graph.author_ids)}
    G = nx.relabel_nodes(G, mapping)

    visualization.visualize(G)


if __name__ == "__main__":
    main()

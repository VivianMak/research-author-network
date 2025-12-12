import matplotlib.pyplot as plt
import networkx as nx
from paper_scraper import PROF_IDS


def visualize(G, node_colors):
    """
    Visualize network.

    Args:
        G: Adjacency matrix
    """

    # Draw
    
    # 2. Get the layout positions (crucial for consistent drawing)
    pos = nx.spring_layout(G)

    # 4. Draw the graph without any labels
    plt.figure(figsize=(8, 6))
    nx.draw(G, pos, with_labels=False, node_color=node_colors, node_size=10, edge_color='gray')

    # 5. Draw labels only for the specified nodes
    nx.draw_networkx_labels(G, pos, labels=PROF_IDS, font_size=12, font_color='red')

    # Show edge weights
    # edge_labels = nx.get_edge_attributes(G, "weight")
    # nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    plt.show()

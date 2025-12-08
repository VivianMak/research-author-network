import matplotlib.pyplot as plt
import networkx as nx


def visualize(G):
    """
    Visualize network.

    Args:
        G: Adjacency matrix
    """

    # Draw
    pos = nx.spring_layout(G)
    nx.draw(
        G,
        pos,
        with_labels=True,
        node_size=700,
        node_color="skyblue",
        font_weight="bold",
    )

    # Show edge weights
    edge_labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    plt.show()

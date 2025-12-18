import matplotlib.pyplot as plt
import networkx as nx
from paper_scraper import PROF_IDS

PROF_LOCS = {
    "5201322": (-1, -1),
    "1769552": (1, 1),
    "2002806": (-1, 1),
    # "50058359": "David Shuman",
    # "134901850": "Zachary del Rosario",
    # "35474768": "Rachel Yang",
    "66274227": (1, -1),
    # "2291589240": "Steve Matsumoto",
    # "5226037": "Sam Michalka"
}

PROF_COLORS = {
    "5201322": "green",
    "1769552": "yellow",
    "2002806": "purple",
    # "50058359": "David Shuman",
    # "134901850": "Zachary del Rosario",
    # "35474768": "Rachel Yang",
    "66274227": "blue",
    # "2291589240": "Steve Matsumoto",
    # "5226037": "Sam Michalka"
}



def visualize(G, path):
    """
    Visualize network.

    Args:
        G: Adjacency matrix
    """
    
    # 2. Get the layout positions (crucial for consistent drawing)
    pos = nx.spring_layout(G)

    # 3. relocate profs
    for prof in PROF_IDS.keys():
        pos[prof] = PROF_LOCS[prof] 

    # Define which nodes should be a specific color
    color_map = []
    front_nodes = []
    normal_nodes = []
    for node in G.nodes():
        if node in PROF_IDS.keys():
            color_map.append(PROF_COLORS[node])
            front_nodes.append(node)
        elif node in path:
            color_map.append('red')
            front_nodes.append(node)
        else:
            normal_nodes.append(node)
            # color_map.append('gray')

    
    highlight_edges = []
    if len(path) > 0:
        for i in range(len(path) - 1):
            highlight_edges.append((path[i], path[i+1]))

    # 4. Draw the graph without any labels
    plt.figure(figsize=(20, 20))
    nx.draw_networkx_edges(G, pos, edge_color='gray', width=0.1)
    nx.draw_networkx_edges(G, pos, edge_color='red', width=0.5, edgelist=highlight_edges)
    nx.draw_networkx_nodes(G, pos, nodelist=normal_nodes, node_color='gray', node_size=10, alpha=0.5)
    nx.draw_networkx_nodes(G, pos, nodelist=front_nodes, node_color=color_map, node_size=70)
    # nx.draw(G, pos, with_labels=False, node_color=color_map, node_size=20, edge_color='gray')

    # 5. Draw labels only for the specified nodes
    # nx.draw_networkx_labels(G, pos, labels=PROF_IDS, font_size=12, font_color='red')

    plt.show()

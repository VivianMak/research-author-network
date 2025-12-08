from typing import List, Tuple, Dict, Set
import numpy as np
import heapq
import matplotlib.pyplot as plt
import networkx as nx
from network import NetworkGraph


def create_node(
    author1_id, g: float = float("inf"), h: float = 0.0, parent: Dict = None
):
    """
    Create a node for the A* algorithm.

    Args:
        position: (x, y) coordinates of the node
        g: Cost from start to this node (default: infinity)
        h: Estimated cost from this node to goal (default: 0)
        parent: Parent node (default: None)

    Returns:
        Dictionary containing node information
    """
    return {"author": author1_id, "g": g, "h": h, "f": g + h, "parent": parent}


def calculate_heuristic(author1_id, author2_id):
    """
    Calculate the estimated distance (weighted) between the two authors.
    """
    # get neighbors function
    edges = NetworkGraph.get_neighbors(author1_id)
    if author2_id in edges:
        # if author 2 is in the list of neighbors, heuristic=1
        heuristic = 1
    else:
        # if author 2 is not in the list of neighbors, heuristic=2
        heuristic = 2
    # return heuristic value
    return heuristic

def find_valid_neighbors(adjacency_matrix, current_author, parent_author):
    # from current author, find all neighbors. If a neighbor matches a parent author, don't add to the list

def reconstruct_path(author2_id: Dict) -> List[Tuple[str, int]]:
    """
    Reconstruct the path from goal to start by following parent pointers. Returns list of authors with weights of edges.
    """
    path = []
    current = author2_id

    while current is not None:
        path.append(current["position"])
        current = current["parent"]

    return path[::-1]  # Reverse to get path from start to goal


def find_path(author1_id, author2_id) -> List[Tuple[int, int]]:
    """
    Find the optimal path from author1 to author2 using A* algorithm.

    Args:
        adjacency_matrix: 2D numpy array (0 = free space, 1 = obstacle)
        author1_id: Starting author
        author2_id: Goal author

    Returns:
        List of positions representing the optimal path
    """
    # Initialize start node
    start_node = create_node(
        author1_id, g=0, h=calculate_heuristic(author1_id, author2_id)
    )

    # Initialize open and closed sets
    open_list = [(start_node["f"], author1_id)]  # Priority queue
    open_dict = {author1_id: start_node}  # For quick node lookup
    closed_set = set()  # Explored nodes

    while open_list:
        # Get node with lowest f value
        _, current_pos = heapq.heappop(open_list)
        current_node = open_dict[current_pos]

        # Check if we've reached the goal
        if current_pos == author2_id:
            return reconstruct_path(current_node)

        closed_set.add(current_pos)

        # Explore neighbors
        for neighbor in NetworkGraph.get_neighbors(author1_id):
            # Skip if already explored
            if neighbor in closed_set:
                continue

            # Calculate new path cost
            tentative_g = current_node["g"] + calculate_heuristic(current_pos, neighbor)

            # Create or update neighbor
            if neighbor not in open_dict:
                neighbor = create_node(
                    position=neighbor_pos,
                    g=tentative_g,
                    h=calculate_heuristic(neighbor_pos, author2_id),
                    parent=current_node,
                )
                heapq.heappush(open_list, (neighbor["f"], neighbor_pos))
                open_dict[neighbor_pos] = neighbor
            elif tentative_g < open_dict[neighbor_pos]["g"]:
                # Found a better path to the neighbor
                neighbor = open_dict[neighbor_pos]
                neighbor["g"] = tentative_g
                neighbor["f"] = tentative_g + neighbor["h"]
                neighbor["parent"] = current_node

    return []  # No path found

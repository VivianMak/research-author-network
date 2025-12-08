from typing import List, Tuple, Dict, Set
import numpy as np
import heapq
import matplotlib.pyplot as plt
import networkx as nx
from network import NetworkGraph
from typing import List, Dict, Tuple


def create_node(
    current_author: str, g: float = float("inf"), h: float = 0.0, parent: Dict = None
):
    """
    Create a node for the A* algorithm.

    Args:
        author_id: identity of node
        g: Cost from start to this node (default: infinity)
        h: Estimated cost from this node to goal (default: 0)
        parent: Parent node (default: None)

    Returns:
        Dictionary containing node information
    """
    return {"author": current_author, "g": g, "h": h, "f": g + h, "parent": parent}


def calculate_heuristic(current_author: str, goal_author: str, graph: NetworkGraph):
    """
    Calculate the estimated distance (weighted) between the two authors.
    """
    edges = graph.get_neighbors(current_author)
    neighbor_ids = [name for name, _ in edges]  # edges is [(neighbor, weight), ...]
    if goal_author in neighbor_ids:
        heuristic = 1
    else:
        heuristic = 2
    return heuristic


def find_valid_neighbors(current_author: str, parent_author: str, graph: NetworkGraph):
    # from current author, find all neighbors.
    edges = graph.get_neighbors(current_author)

    # If a neighbor matches a parent author, remove from list
    neighbors = [(n, w) for n, w in edges if n != parent_author]
    return neighbors


def reconstruct_path(goal_node: Dict) -> List[str]:
    """
    Reconstruct the path from goal to start by following parent pointers.
    Returns a list of author IDs from start to goal.
    """
    path = []
    current = goal_node

    while current is not None:
        path.append(current["author"])
        current = current["parent"]

    return path[::-1]  # Reverse to get path from start to goal


def find_path(start_author: str, goal_author: str, graph: NetworkGraph) -> List[str]:
    """
    Find the optimal path from start_author to goal_author using A* algorithm.
    Takes into account edge weights from the collaboration matrix.
    """

    # Initialize start node
    start_node = create_node(
        current_author=start_author,
        g=0,
        h=calculate_heuristic(start_author, goal_author, graph),
        parent=None,
    )

    # Priority queue (min-heap) ordered by f = g + h
    open_list = [(start_node["f"], start_author)]
    open_dict = {start_author: start_node}
    closed_set = set()

    while open_list:
        # Pop node with lowest f
        _, current_author = heapq.heappop(open_list)
        current_node = open_dict[current_author]

        # Goal check
        if current_author == goal_author:
            return reconstruct_path(current_node)

        closed_set.add(current_author)

        # Explore neighbors (with weights)
        neighbors = graph.get_neighbors(
            current_author
        )  # returns [(neighbor, weight), ...]
        for neighbor_author, weight in neighbors:
            if neighbor_author in closed_set:
                continue

            tentative_g = current_node["g"] + weight

            if neighbor_author not in open_dict:
                neighbor_node = create_node(
                    current_author=neighbor_author,
                    g=tentative_g,
                    h=calculate_heuristic(neighbor_author, goal_author, graph),
                    parent=current_node,
                )
                open_dict[neighbor_author] = neighbor_node
                heapq.heappush(open_list, (neighbor_node["f"], neighbor_author))
            elif tentative_g < open_dict[neighbor_author]["g"]:
                # Found a better path
                neighbor_node = open_dict[neighbor_author]
                neighbor_node["g"] = tentative_g
                neighbor_node["f"] = tentative_g + neighbor_node["h"]
                neighbor_node["parent"] = current_node
                return []  # No path found

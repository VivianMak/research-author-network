"""
Implementation of A* Path-Finding algorithm with a heuristic based on edge weights.
    Loosely modeled off of DataCamp A* Algorithm.
"""

from typing import List, Dict
import heapq
from network import NetworkGraph


def create_node(
    current_author: str, g: float = float("inf"), h: float = 0.0, parent: Dict = None
):
    """
    Create a node for the A* algorithm.

    Args:
        current_author: string representing identity of current node.
        g: float representing cost from start to this node (default: infinity).
        h: float representing estimated cost from this node to goal (default: 0).
        parent: dict mapping all current_authors so far to their parent node (default: None).

    Returns:
        A dictionary containing node information for the current node.
    """
    return {"author": current_author, "g": g, "h": h, "f": g + h, "parent": parent}


def calculate_heuristic(current_author: str, goal_author: str, graph: NetworkGraph):
    """
    Calculate the estimated weighted distance between the two authors.

    Args:
        current_author: string representing identity of current node.
        goal_author: string representing the identity of the goal node.
        graph: a graph object representing the author network.

    Returns:
        An int representing the heuristic from the current author to the goal_author.
    """
    # Get neighbors
    edges = graph.get_neighbors(current_author)
    neighbor_ids = [name for name, _ in edges]

    # If goal_author is a neighbor, h=1
    if goal_author in neighbor_ids:
        heuristic = 1
    else:
        heuristic = 0
    return heuristic


def reconstruct_path(goal_node: Dict) -> List[str]:
    """
    Reconstruct the path from goal to start by following parent pointers.

    Args:
        goal_node: a dict containing information on the identity of the goal node
            and parent nodes.

    Returns:
        A list of author IDs from start to goal.
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

    Args:
        start_author: string representing identity of current node.
        goal_author: string representing identity of goal node.
        graph: a graph object representing the author network.

    Returns:
        A list of the path from the start author to the goal author.
    """

    # Initialize start node
    start_node = create_node(
        current_author=start_author,
        g=0,
        h=calculate_heuristic(start_author, goal_author, graph),
        parent=None,
    )

    counter = 0  # tie-breaker

    # Priority queue (min-heap) ordered by f = g + h
    open_list = [(start_node["f"], counter, start_node)]
    open_dict = {start_author: start_node}
    closed_set = set()

    while open_list:
        # Pop node with lowest f
        _, _, current_node = heapq.heappop(open_list)
        current_author = current_node["author"]

        # Goal check
        if current_author == goal_author:
            return reconstruct_path(current_node)

        closed_set.add(current_author)

        # Explore neighbors (with weights)
        for neighbor_author, weight in graph.get_neighbors(current_author):
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
                counter += 1
                heapq.heappush(open_list, (neighbor_node["f"], counter, neighbor_node))
            elif tentative_g < open_dict[neighbor_author]["g"]:
                neighbor_node = open_dict[neighbor_author]
                neighbor_node["g"] = tentative_g
                neighbor_node["f"] = tentative_g + neighbor_node["h"]
                neighbor_node["parent"] = current_node
                counter += 1
                heapq.heappush(open_list, (neighbor_node["f"], counter, neighbor_node))

    return ["No Path Found"]  # No path found

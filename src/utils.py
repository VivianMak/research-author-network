import numpy as np

from dataclasses import dataclass

@dataclass
class Node:
    author_name: str
    author_id: str
    collab_edges: list   #(author_id, number of collabs) 

    # Extra info -- node size
    citation_count: int
    paper_count:int
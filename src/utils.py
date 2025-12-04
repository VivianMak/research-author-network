import numpy as np
from typing import Optional

from dataclasses import dataclass

@dataclass
class Node:
    author_name: str
    author_id: str
    collab_edges: Optional['Node'] = None   #(author_id, number of collabs) 

    # Extra info -- node size
    # citation_count: int
    # paper_count:int
# Node class

from utils import Node
from typing import List

class NetworkGraph:
    """Create a network"""

    def __init__(self):
        """Initialize an instance of the Network Graph."""

        self.node_list = []


    def add_node(self, 
                 author_name,
                 author_id,
                 collab_edges,
                 citation_count,
                 paper_count):
        """
        Make a new node with a new author
        
        Args:
            author_name: Description
            author_id: Description
            collab_edges: Description
            citation_count: Description
            paper_count: Description
        """
        
        # Check if node already exists
        if self.node_lookup(author_id):
            self.edit_node(author_name,
                           author_id,
                           collab_edges)
            

        new_node = Node(
            author_name=author_name, 
            author_id=author_id, 
            collab_edges=collab_edges)
        
        self.node_list.append(new_node)

    def edit_node(self, author_name,
                        author_id,
                        collab_edges):
        """"""
        pass

    def node_lookup(self, author_id):
        """Turn node list into a dictionary for quick key lookup."""

         # Create a dictionary for quick lookups
         idx, node = next(((i,node) for i,node in self.node_list if node.author_id == author_id), None)

        return idx, node



    def add_edge(self, node:Node):
        """Update the edges of an author."""

        # Check if collaboration already exists
        if node not in self.collab_edges:
            node.collab_edges.append(node)


    def calculate_weight(self):
        """Calculate the collaborations to populate the collaboration edges of a node with author_id and num_of_collabs."""


    

    def connected_authors(self, node:Node) -> List[Node]:
        """
        Return the authors connected to the author (node).

        Args:
            node: a node representing the author to query neighbors

        Return:
            a list of neighbor nodes
        """

    

from typing import List
import pandas as pd

class NetworkGraph:
    """Create a network"""

    def __init__(self):
        """Initialize an instance of the Network Graph."""

        # Keeps track of matrix headers
        self.author_ids = []

        # Dictionary "author_id": (name,)
        self.author_info = {}

        self.collabs_mat = []


    def add_new_author(self, author_id):
        """
        Create a new row/col for an author and populate collaborations
        
        Args:
            author_id: (string) the id of corresponding author
        """
        print("----ADDING NEW AUTHOR-----")
        # Add new author to list
        self.author_ids.append(author_id)

        n = len(self.author_ids)

        # Populate row and col with zeros
        self.collabs_mat.append([0]*(n))

        for i in range(n-1):
            self.collabs_mat[i].append(0)

    def add_author_collab(self, author_id, collabs):
        """For an existing author, adjust the collaborations.
        Args:
            author_id: (string) the id of corresponding author.
            collabs: (list) a list of collaborated authors.
        """

        idx = self.author_ids.index(author_id)

        for c in collabs:

            # Add row and col for new authors
            if not self.check_author(c):
                self.add_new_author(author_id=c)

                # New author is known at last index
                self.collabs_mat[idx][-1] += 1
                self.collabs_mat[-1][idx] += 1
                
            else:
                # Find seen author index
                i = self.author_ids.index(c)
                self.collabs_mat[idx][i] += 1
                self.collabs_mat[i][idx] += 1


    def check_author(self, author_id) -> bool:
        """Check if author exists.
        Args:
            author_id: (string) the id of corresponding author.
        Return:
            true if author has been seen
        """

        if author_id in self.author_ids:
            return True
        return False

    def get_collabs(self):
        """Format the adjacency matrix as a dataframe"""

        print("Showing final collboration adjacency matrix...")

        df = pd.DataFrame(self.collabs_mat, columns=self.author_ids, index=self.author_ids)
        print(df)


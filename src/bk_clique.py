# Clique finding algorithm

from network import NetworkGraph

class BK:

    def __init__(self, network:NetworkGraph):

        # All sets of cliques
        self.maximal_cliques = []

        
        self.network = network  # network object
        self.authors = network.author_ids  # list of authors
        

        # Current neighbors
        self.v_neighbors = {}


    def bk_clique(self, R, P, X):
        """
        Find all the maximal cliques in a graph.
        
        Args:
            R: a set of the current clique
            P: a set of the candidate verticies
            X: a set of exclusions
        """


        if (not P) and (not X):
            print(f"Outputting the current clique: {R}")
            self.maximal_cliques.append(R)

        for vertex in P:
            print(f"At current loop for vertex: {vertex}")

            # Redefine arguements in entire set
            R.add(vertex)     # add vertex of current loop
            P = P & set(self.network.bk_get_neighbors(vertex))    # neighbors of current vertex
            X = X & set(self.network.bk_get_neighbors(vertex))    # 

            print("INPUTS TO RECURSIVE CALL ARE: ")
            print(f"R = {R}")
            print(f"P = {P}")
            print(f"X = {X}")

            # Recursive call 
            self.bk_clique(R, P, X)

            # print(f"At the current iteration of vertex: {vertex}, the set of cadidate verticies P are: {P}")

            # Remove checked candidates
            P.re(vertex)
            X.add(vertex)



    def get_maximal_cliques(self):

        R = set()
        P = set(self.authors)
        X = set()

        print("---- FINDING MAXIMAL CLIQUES -----")
        print(f"All candidates set P starting with: {P}")

        self.bk_clique(R, P, X)

        return self.maximal_cliques
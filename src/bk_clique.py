# Clique finding algorithm

from network import NetworkGraph

class BK:

    def __init__(self, network:NetworkGraph, prof_ids):

        # All sets of cliques
        self.maximal_cliques = []
   
        self.network = network  # network object
        self.authors = network.author_ids  # list of authors

        self.prof_ids = prof_ids
        


    def bk_clique(self, R, P, X):
        """
        Find all the maximal cliques in a graph.
        
        Args:
            R: a set of the current clique
            P: a set of the candidate verticies
            X: a set of exclusions
        """


        if (not P) and (not X):
            # print(f"Outputting the a maximal clique: {R}")
            if (len(R) > 2) and (set(self.prof_ids.keys()) & set(R)):
                self.maximal_cliques.append(R.copy())

        for vertex in list(P):

            # Get neighbors of current vertex
            neighbors = set(self.network.bk_get_neighbors(vertex))

            # Redefine arguements in entire set
            R_temp = R + [vertex]     # add vertex of current loop
            P_temp = P & neighbors    # candidates intersect neighbors
            X_temp = X & neighbors    # candidates intersect excluded verticies

            # Recursive call 
            self.bk_clique(R_temp, P_temp, X_temp)

            # Remove checked candidates
            P.remove(vertex)
            X.add(vertex)



    def get_maximal_cliques(self):
        """
        Calls Bron-Kerbosch algorithm
        
        Return:
            maximal_cliques: (list) of all clique
        """

        R = []
        P = set(self.authors)
        X = set()

        print("---- FINDING MAXIMAL CLIQUES -----")
        # print(f"All candidates set P starting with: {P}")

        self.bk_clique(R, P, X)

        print(f"---- FINISHED -----")
        print(f"The set of all cliques are: {self.maximal_cliques}.")
        print(f"There are a total of {len(self.maximal_cliques)} cliques for professors: {', '.join(self.prof_ids.values())}.")

        return self.maximal_cliques
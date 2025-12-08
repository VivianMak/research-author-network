from network import NetworkGraph


def main():
    
    graph = NetworkGraph()
    author = "vp"
    collabs = ["bm", "rw"]

    # Check if author exists yet fr depth 0
    if not graph.check_author(author):
        graph.add_new_author(author)

    # Add author's list of collborations
    graph.add_author_collab(author, collabs)

    # Print out adjacency matrix
    graph.get_collabs()

    edges = graph.get_neighbors("bm")
    print(f"the neighbors of bm are {edges}")



if __name__=="__main__":
    main()
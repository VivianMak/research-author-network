import json
import time
from network import NetworkGraph
from paper_scraper import INIT_DATA, PROF_IDS, find_author_collabs, find_papers

def main():
    graph = NetworkGraph()
    # author = "vp"
    # collabs = ["bm", "rw"]

    for i, (prof_id, prof_name) in enumerate(PROF_IDS.items()):
        print(f"Finding {prof_name}'s collaborators...")
        papers = INIT_DATA[i]['papers']
        collabs = find_author_collabs(prof_id, papers)

        # Check if author exists yet fr depth 0
        if not graph.check_author(prof_id):
            graph.add_new_author(prof_id)

        # Add author's list of collborations
        graph.add_author_collab(prof_id, collabs)

        
        depth = 1
        scan_list = collabs
        while depth > 0:
            all_indirect_collabs = []
            print(f"Scanning depth {depth}...")
            depth = depth - 1
            indirect_papers = find_papers(scan_list)
            # print(indirect_papers)
            for j, col in enumerate(scan_list):
                print(col)
                p = indirect_papers[j]['papers']
                indirect_collabs = find_author_collabs(col, p)
                graph.add_author_collab(col, indirect_collabs)
                all_indirect_collabs.extend(indirect_collabs)
            # for col in scan_list:
            #     print(col)
            #     indirect_papers = find_papers(col)
            #     indirect_collabs = find_author_collabs(col, indirect_papers)

            scan_list = all_indirect_collabs

    # Print out adjacency matrix
    graph.get_collabs()
    graph.save_matrix_as_csv("test1")

    edges = graph.get_neighbors("2479251")
    print(f"the neighbors of Sarah are {edges}")

if __name__ == "__main__":
    main()

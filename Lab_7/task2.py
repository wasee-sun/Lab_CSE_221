from merge_sort import mergesort


def kruskal(graph):
    edges_lst = []
    graph_id = {key : i for key, i in zip(graph.keys(), range(len(graph)))}
    for key, edges in graph.items():
        edges_lst += [(key, edge[0], edge[1]) for edge in edges]
        
    edges_lst = mergesort(edges_lst)
    union_arr = [key for key in graph_id.keys()]
    
    mst = 0
    
    for edges in edges_lst:
        grp_1 = edges[0]
        grp_2 = edges[1]
        while union_arr[graph_id[grp_1]] != grp_1:
            grp_1 = union_arr[graph_id[grp_1]]  
        while union_arr[graph_id[grp_2]] != grp_2:
            grp_2 = union_arr[graph_id[grp_2]]  
            
        if grp_1 != grp_2:
            mst += edges[2]
            if graph_id[grp_1] < graph_id[grp_2]:
                union_arr[graph_id[grp_2]] = grp_1
            else:
                union_arr[graph_id[grp_1]] = grp_2
                
    return mst


def traversal():
    for n in range(1, 3):
        with open(f"input2_{n}.txt", "r") as f1:
            vertices, edges = f1.readline().strip().split()
            graph = {i : [] for i in range(1, int(vertices) + 1)}
            for i in range(int(edges)):
                u, v, w = f1.readline().strip().split()
                graph[int(u)].append((int(v), int(w)))
            mst = kruskal(graph)
            with open(f"output2_{n}.txt", "w") as f2:
                f2.write(f"{str(mst)}")
            
            
if __name__ == "__main__":
    traversal()
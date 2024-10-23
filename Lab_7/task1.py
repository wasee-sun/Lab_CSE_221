def friend_circle(graph_nodes, vertices):
    groups = [1 for i in range(vertices)]
    union_arr = [i for i in range(vertices)]
    
    friends = []
    for edges in graph_nodes:
        grp_1 = edges[0]
        grp_2 = edges[1]
        while union_arr[grp_1] != grp_1:
            grp_1 = union_arr[grp_1] 
        while union_arr[grp_2] != grp_2:
            grp_2 = union_arr[grp_2]
            
        if grp_1 != grp_2:
            friends.append(groups[grp_1] + groups[grp_2])
            if grp_1 < grp_2:
                union_arr[grp_2] = grp_1
                groups[grp_1] += groups[grp_2]
                groups[grp_2] = 0
            else:
                union_arr[grp_1] = grp_2
                groups[grp_2] += groups[grp_1]
                groups[grp_1] = 0
        else:
            friends.append(groups[grp_1])
                    
    return friends
    
    
def traversal():
    for n in range(1, 3):
        with open(f"input1_{n}.txt", "r") as f1:
            vertices, edges = f1.readline().strip().split()
            graph_nodes = []
            for i in range(int(edges)):
                u, v = f1.readline().strip().split()
                graph_nodes.append((int(u), int(v)))
            friends = friend_circle(graph_nodes, int(vertices))
            with open(f"output1_{n}.txt", "w") as f2:
                for val in friends:
                    f2.write(f"{str(val)}\n")



if __name__ == "__main__":
    traversal()
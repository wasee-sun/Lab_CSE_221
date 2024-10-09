def cycle(graph, node, color_lst, dfs_lst):
    if len(graph[node]) == 0:
        dfs_lst[node] = False
        return False
    if dfs_lst[node] == 1 and color_lst[node] == 1:
        return True
    
    color_lst[node] = 1
    dfs_lst[node] = True
    
    for val in graph[node]:
        cycle_bool = cycle(graph, val, color_lst, dfs_lst)
        if cycle_bool:
            return cycle_bool
    
    dfs_lst[node] = False
    return False
    
                

def traversal():
    for n in range(1, 6):
        with open(f"input4_{n}.txt", "r") as f1:
            vertices, edges = f1.readline().strip().split()
            diction = {i:[] for i in range(1, int(vertices) + 1)}
            color_lst = [0 for i in range((int(vertices) + 1))]
            dfs_lst = [False for i in range((int(vertices) + 1))]
            for i in range(int(edges)):
                u, v = f1.readline().strip().split()
                diction[int(u)].append(int(v))
            cycle_bool = cycle(diction, 1, color_lst, dfs_lst)
            with open(f"output4_{n}.txt", "w") as f2:
                if cycle_bool:
                    f2.write(f"YES")
                else:
                    f2.write(f"NO")
    
    
if __name__ == '__main__':
    traversal()
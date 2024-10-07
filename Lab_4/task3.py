def colour_init(graph):
    for key in graph.keys():
        graph[key].append(0)
        
    return graph
    
    
def dfs(graph, node, path):
    graph[node][1] = 1
    path.append(node)
    
    for val in graph[node][0]:
        if graph[val][1] == 0:
            path = dfs(graph, val, path)
        
    return path
    
                

def traversal():
    for n in range(1, 5):
        with open(f"input3_{n}.txt", "r") as f1:
            vertices, edges = f1.readline().strip().split()
            diction = {i:[[]] for i in range(1, int(vertices) + 1)}
            for i in range(int(edges)):
                u, v = f1.readline().strip().split()
                diction[int(u)][0].append(int(v))
            diction = colour_init(diction)
            dfs_arr = dfs(diction, 1, [])
            with open(f"output3_{n}.txt", "w") as f2:
                for val in dfs_arr:
                    f2.write(f"{str(val)} ")
    
    
if __name__ == '__main__':
    traversal()
class Queue:
    def __init__(self):
        self.queue = []
        
    def is_empty(self):
        return len(self.queue) == 0
        
    def enqueue(self, val):
        self.queue.append(val)
        
    def dequeue(self):
        if self.is_empty():
            return False
        return self.queue.pop(0)
    
    
def bfs(graph, start, end):
    for key in graph.keys():
        graph[key].append(0)
    
    Q = Queue()
    graph[start][1] = 1
    Q.enqueue(start)
    return _bfs(graph, Q, start, end)

def _bfs(graph, Q, start, end):
    parent_dict = {start: None}
    flag = False
    while not Q.is_empty():
        node = Q.dequeue()
        for val in graph[node][0]:
            if val not in parent_dict.keys():
                parent_dict[val] = [node]
            else:
                parent_dict[val].append(node)
            Q.enqueue(val)
            if val == end:
                flag = True
                break
            graph[val][1] = 1
        if flag:
            break
    path = [end]
    while True:
        if parent_dict[path[0]] == None:
            break
        if len(parent_dict[path[0]]) > 1:
            path = [parent_dict[path[0]][0]] + path
        else:
            path = parent_dict[path[0]] + path
    return path
            

def traversal():
    for n in range(1, 6):
        with open(f"input5_{n}.txt", "r") as f1:
            vertices, edges, end = f1.readline().strip().split()
            diction = {i:[[]] for i in range(1, int(vertices) + 1)}
            for i in range(int(edges)):
                u, v = f1.readline().strip().split()
                diction[int(u)][0].append(int(v))
            bfs_arr = bfs(diction, 1, int(end))
            with open(f"output5_{n}.txt", "w") as f2:
                f2.write(f"Time: {str(len(bfs_arr) - 1)}\n")
                path = "Shortest Path: "
                for val in bfs_arr:
                    path += f"{str(val)} "
                f2.write(path)
    
    
if __name__ == '__main__':
    traversal()
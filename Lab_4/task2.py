class Queue:
    def __init__(self):
        self.queue = []
        
    def _is_empty(self):
        return len(self.queue) == 0
        
    def enqueue(self, val):
        self.queue.append(val)
        
    def dequeue(self):
        if self._is_empty():
            return False
        return self.queue.pop(0)
    
    
def bfs(graph, start):
    for key in graph.keys():
        graph[key].append(0)
    
    Q = Queue()
    graph[start][1] = 1
    Q.enqueue(start)
    bfs_arr = []
    
    while not Q._is_empty():
        ele = Q.dequeue()
        bfs_arr.append(ele)
        for val in graph[ele][0]:
            if graph[val][1] == 0:
                graph[val][1] = 1
                Q.enqueue(val)
                
    return bfs_arr
                

def traversal():
    for n in range(1, 5):
        with open(f"input2_{n}.txt", "r") as f1:
            vertices, edges = f1.readline().strip().split()
            diction = {i:[[]] for i in range(1, int(vertices) + 1)}
            for i in range(int(edges)):
                u, v = f1.readline().strip().split()
                diction[int(u)][0].append(int(v))
            bfs_arr = bfs(diction, 1)
            with open(f"output2_{n}.txt", "w") as f2:
                for val in bfs_arr:
                    f2.write(f"{str(val)} ")
    
    
if __name__ == '__main__':
    traversal()
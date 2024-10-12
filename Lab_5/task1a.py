import random


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
    
    
def cycle(start, parent_dict):
    visited_arr = {i : -1 for i in parent_dict.keys()}
    return _cycle(start, parent_dict, visited_arr)

def _cycle(start, parent_dict, visited_arr):
    visited_arr[start] = 0
    if parent_dict[start]:
        for val in parent_dict[start]:
            if visited_arr[val] == -1:
                cycle_bool = _cycle(val, parent_dict, visited_arr)
                if cycle_bool:
                    return True
            if visited_arr[val] == 0:
                return True
    
    visited_arr[start] = 1
    return False
            
    

def top_sort_bfs(graph, idx_arr, visited_items, parent_dict):
    Q = Queue()
    lst = [i for i in graph.keys() if graph[i][1] == 0]
    start = random.choice(lst)
    graph[start][1] = 1
    idx_arr[start] = visited_items
    visited_items += 1
    Q.enqueue(start)
    
    while not Q._is_empty():
        key = Q.dequeue()
        if key:
            for val in graph[key][0]:
                if graph[val][1] == 0:
                    idx_arr[val] = visited_items
                    graph[val][1] = 1
                    parent_dict[val] = [key]
                    visited_items += 1
                    Q.enqueue(val)
                    continue
                if graph[val][1] == 1:
                    bool_val = cycle(val, parent_dict)
                    if not bool_val:
                        if idx_arr[val] < idx_arr[key]:
                            if not parent_dict[val]:
                                parent_dict[val] = [key]
                            else:
                                for par in parent_dict[val]:
                                    if par == key:
                                        break
                                else:
                                    parent_dict[val].append(key)
                            idx_arr[val], idx_arr[key] = idx_arr[key], idx_arr[val]
                            if parent_dict[key]:
                                for par_key in parent_dict[key]:
                                    Q.enqueue(par_key)
                            Q.enqueue(val)
                    else:
                        return False, visited_items, parent_dict
                
    return idx_arr, visited_items, parent_dict



def traversal():
    for n in range(1, 4):
        with open(f"input1_{n}.txt", "r") as f1:
            vertices, edges = f1.readline().strip().split()
            diction = {i:[[], 0] for i in range(1, int(vertices) + 1)}
            idx_arr = {i : -1 for i in diction.keys()}
            parent_dict = {i : None for i in diction.keys()}
            visited_items = 0
            for i in range(int(edges)):
                u, v = f1.readline().strip().split()
                diction[int(u)][0].append(int(v))
            while visited_items != int(vertices):
                idx_arr, visited_items, parent_dict = top_sort_bfs(diction, idx_arr, visited_items, parent_dict)
                if not idx_arr:
                    break
            with open(f"output1a_{n}.txt", "w") as f2:
                if idx_arr:
                    top_arr = [0 for i in range(int(vertices))]
                    for key, val in idx_arr.items():
                        top_arr[val] = key
                    for val in top_arr:
                        f2.write(f"{val} ")
                else:
                    f2.write("IMPOSSIBLE")
            
            
if __name__ == "__main__":
    traversal()
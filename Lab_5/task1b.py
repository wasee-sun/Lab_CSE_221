import random

class Topsort:
    def __init__(self, graph):
        self.graph = graph
        self.graph_id = {key : j for key, j in zip(graph.keys(), range(len(graph)))}
        self.top_arr = [0] * len(self.graph)
        self.idx = len(self.graph) - 1
        
    def top_sort(self):
        visited_lst = [False for i in range(len(self.graph))]
        explored_lst = [False for i in range(len(self.graph))]
            
        while True:
            val = list(self.graph.keys() - self.top_arr)
            if len(val) == 0:
                break
            r_key = random.choice(val) # depending on random choice
            explored_lst, visited_lst = self._top_sort(r_key, explored_lst, visited_lst)
            if not explored_lst:
                return False
            
        return self.top_arr
            
    def _top_sort(self, cur_key, explored_lst, visited_lst): 
        visited_lst[self.graph_id[cur_key]] = True
        for val in self.graph[cur_key]:
            if ((explored_lst[self.graph_id[val]] is False) and 
            (visited_lst[self.graph_id[val]] is False)):
                explored_lst, visited_lst = self._top_sort(val, explored_lst, visited_lst)
                if not explored_lst:
                    return False, visited_lst
            if ((explored_lst[self.graph_id[val]] is False) and 
            (visited_lst[self.graph_id[val]] is True)):
                return False, visited_lst
                
        if explored_lst[self.graph_id[cur_key]] is False:
            self.top_arr[self.idx] = cur_key
            explored_lst[self.graph_id[cur_key]] = True
            self.idx -= 1
            
        return explored_lst, visited_lst


def traversal():
    for n in range(1, 4):
        with open(f"input1_{n}.txt", "r") as f1:
            vertices, edges = f1.readline().strip().split()
            diction = {i: [] for i in range(1, int(vertices) + 1)}
            for i in range(int(edges)):
                u, v = f1.readline().strip().split()
                diction[int(u)].append(int(v))
            TPS = Topsort(diction)
            top_arr = TPS.top_sort()
            with open(f"output1b_{n}.txt", "w") as f2:
                if top_arr:
                    for val in top_arr:
                        f2.write(f"{val} ")
                else:
                    f2.write("IMPOSSIBLE")
            
if __name__ == "__main__":
    traversal()
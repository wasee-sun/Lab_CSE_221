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
            
        return self.top_arr
            
    def _top_sort(self, cur_key, explored_lst, visited_lst): 
        visited_lst[self.graph_id[cur_key]] = True
        for val in self.graph[cur_key]:
            if ((explored_lst[self.graph_id[val]] is False) and 
            (visited_lst[self.graph_id[val]] is False)):
                explored_lst, visited_lst = self._top_sort(val, explored_lst, visited_lst)
                
        if explored_lst[self.graph_id[cur_key]] is False:
            self.top_arr[self.idx] = cur_key
            explored_lst[self.graph_id[cur_key]] = True
            self.idx -= 1
            
        return explored_lst, visited_lst


def kosaraju(graph):
    tps = Topsort(graph)
    tps_arr = tps.top_sort()
    graph = transpose_graph(graph)
    visited = [-1 for i in range(len(graph))]
    graph = {key : [val, i] for key, val, i in zip(graph.keys(), graph.values(), range(len(graph)))}
    scc_eles = []
    scc = 0
    while len(sum(scc_eles, [])) != len(graph):
        start = [item for item in tps_arr if item not in sum(scc_eles, [])]
        new_completed, visited = _kosaraju(graph, start[0], visited)
        scc_eles.append(new_completed)
        scc += 1
        
    return scc_eles
    
def _kosaraju(graph, node, visited):
    visited[graph[node][1]] = 0
    scc_eles = []
    for nxt_node in graph[node][0]:
        if visited[graph[nxt_node][1]] == -1:
            scc_eles, visited = _kosaraju(graph, nxt_node, visited)
        if visited[graph[nxt_node][1]] == 0:
            scc_eles.append(nxt_node)
            visited[graph[nxt_node][1]] = 1
            return scc_eles, visited
        
    scc_eles.append(node)
    visited[graph[node][1]] = 1
    return scc_eles, visited
            
def transpose_graph(graph):
    n_graph = {key : [] for key in graph.keys()}
    for key, vals in graph.items():
        for val in vals:
            n_graph[val].append(key)
    return n_graph


def traversal():
    for n in range(1, 4):
        with open(f"input3_{n}.txt", "r") as f1:
            vertices, edges = f1.readline().strip().split()
            diction = {i: [] for i in range(1, int(vertices) + 1)}
            for i in range(int(edges)):
                u, v = f1.readline().strip().split()
                diction[int(u)].append(int(v))
            scc_arr = kosaraju(diction)
            with open(f"output3_{n}.txt", "w") as f2:
                for ele in scc_arr:
                    for val in ele:
                        f2.write(f"{val} ")
                    f2.write(f"\n")

if __name__ == '__main__':
    traversal()
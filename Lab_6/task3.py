from Data_structure.priority_queue_graph import Priority_Queue
import numpy as np


def dijkstra(graph, graph_id, st_idx):
    dist_arr = [np.inf for i in range(len(graph))]
    dist_arr[graph_id[st_idx]] = 0
    PQ = Priority_Queue()
    PQ.enqueue((st_idx, 0))
    return _dijkstra(graph, graph_id, dist_arr, PQ)
    
def _dijkstra(graph, graph_id, dist_arr, PQ):
    while not PQ.is_empty():
        node = PQ.dequeue()
        if dist_arr[graph_id[node[0]]] >= node[1]:
            for edge in graph[node[0]]:
                if ((dist_arr[graph_id[edge[0]]] == np.inf) or 
                    (dist_arr[graph_id[edge[0]]] > edge[1])):
                    dist_arr[graph_id[edge[0]]] = edge[1]
                    PQ.enqueue(edge)
                
    return dist_arr

    
def traversal():
    for n in range(1, 3):
        with open(f"input3_{n}.txt", "r") as f1:
            vertices, edges = f1.readline().strip().split()
            graph = {i : [] for i in range(1, int(vertices) + 1)}
            for i in range(int(edges)):
                u, v, w = f1.readline().strip().split()
                graph[int(u)].append((int(v), int(w)))
            graph_id = {key : i for key, i in zip(graph.keys(), range(len(graph)))}
            dist_arr = dijkstra(graph, graph_id, 1)
            with open(f"output3_{n}.txt", "w") as f2:
                f2.write(f"{str(max(dist_arr))}")
                    
if __name__ == "__main__":
    traversal()
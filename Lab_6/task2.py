from Data_structure.priority_queue_graph import Priority_Queue
import numpy as np

def dijkstra(graph, st_idx):
    graph_id = {key : i for key, i in zip(graph.keys(), range(len(graph)))}
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
                    (dist_arr[graph_id[edge[0]]] > dist_arr[graph_id[node[0]]] + edge[1])):
                    dist_arr[graph_id[edge[0]]] = dist_arr[graph_id[node[0]]] + edge[1]
                                        
                    PQ.enqueue(edge)
                
    return dist_arr


def traversal():
    for n in range(1, 4):
        with open(f"input2_{n}.txt", "r") as f1:
            vertices, edges = f1.readline().strip().split()
            graph = {i : [] for i in range(1, int(vertices) + 1)}
            for i in range(int(edges)):
                u, v, w = f1.readline().strip().split()
                graph[int(u)].append((int(v), int(w)))
            start1, start2 = f1.readline().strip().split()
            dist_arr_1 = dijkstra(graph, int(start1))
            dist_arr_2 = dijkstra(graph, int(start2))
            max_dist = np.inf
            node = None
            graph_id = {i : key for key, i in zip(graph.keys(), range(len(graph)))}
            for i in range(len(dist_arr_1)):
                max_val = max(dist_arr_1[i], dist_arr_2[i])
                if max_val < max_dist:
                    max_dist = max_val
                    node = graph_id[i]
            with open(f"output2_{n}.txt", "w") as f2:
                if max_dist == np.inf:
                    f2.write("Impossible")
                else:
                    f2.write(f"Time {max_dist}\nNode {node}")


if __name__ == "__main__":
    traversal()
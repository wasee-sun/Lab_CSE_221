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
    
    
def bfs(graph, start, row, col):
    Q = Queue()
    graph[start[0]][start[1]][1] = 1
    Q.enqueue(start)
    diamonds = 0
    if graph[start[0]][start[1]][0] == "D":
        diamonds += 1
    block = []
        
    while not Q._is_empty():
        ele = Q.dequeue()
        ways = [
            (ele[0], ele[1] + 1),
            (ele[0] + 1, ele[1]),
            (ele[0] - 1, ele[1]),
            (ele[0], ele[1] - 1),
            ]
        for way in ways:
            if 0 <= way[0] < row and 0 <= way[1] < col:
                if graph[way[0]][way[1]][0] == "#":
                    block.append(way)
                    continue
                if graph[way[0]][way[1]][1] == 1:
                    continue
                graph[way[0]][way[1]][1] = 1
                Q.enqueue(way)
                if graph[way[0]][way[1]][0] == "D":
                    diamonds += 1
                
    return diamonds, block


def matrix(f1):
    row, col = f1.readline().strip().split()
    matrix = [[0 for i in range(int(col))] for i in range(int(row))]
    idx = 0
    for line in f1:
        for i in range(len(line.strip())):
            matrix[idx][i] = [line[i], 0]
        idx += 1
    return matrix, row, col


def dungeon():
    for n in range(1, 8):
        with open(f"input6_{n}.txt", "r") as f1:
            matrix_arr, row, col = matrix(f1)
            diamonds, blocks = bfs(matrix_arr, (0, 0), int(row), int(col))
            for block in blocks:
                ways = [
                    (block[0], block[1] + 1),
                    (block[0] + 1, block[1]),
                    (block[0] - 1, block[1]),
                    (block[0], block[1] - 1),
                    ]
                for way in ways:
                    if 0 <= way[0] < int(row) and 0 <= way[1] < int(col):
                        if matrix_arr[way[0]][way[1]][0] != "#" and matrix_arr[way[0]][way[1]][1] == 0:
                            new_diamonds, new_blocks = bfs(matrix_arr, way, int(row), int(col))
                            if new_diamonds > diamonds:
                                diamonds = new_diamonds
            with open(f"output6_{n}.txt", "w") as f2:
                f2.write(f"{diamonds}")
                
            
            
if __name__ == "__main__":
    dungeon()
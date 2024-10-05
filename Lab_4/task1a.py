def adj_matrix():
    for n in range(1, 3):
        with open(f"input1a_{n}.txt", "r") as f1:
            vertices, edges = f1.readline().strip().split()
            matrix = [[0 for i in range(int(vertices) + 1)] for i in range(int(vertices) + 1)]
            for i in range(int(edges)):
                u, v, w = f1.readline().strip().split()
                matrix[int(u)][int(v)] = int(w)
            print(matrix)
            with open(f"output1a_{n}.txt", "w") as f2:
                for i in range(int(vertices) + 1):
                    for j in range(int(vertices) + 1):
                        f2.write(f"{matrix[i][j]} ")
                    f2.write("\n")
                

if __name__ == "__main__":
    adj_matrix()
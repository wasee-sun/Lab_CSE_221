def adj_list():
    for n in range(1, 4):
        with open(f"input1b_{n}.txt", "r") as f1:
            vertices, edges = f1.readline().strip().split()
            diction = {i:[] for i in range(int(vertices) + 1)}
            for i in range(int(edges)):
                u, v, w = f1.readline().strip().split()
                diction[int(u)].append((int(v), int(w)))
            print(diction)
            with open(f"output1b_{n}.txt", "w") as f2:
                for key, val in diction.items():
                    f2.write(f"{key} : ")
                    for value in val:
                        f2.write(f"{value} ")
                    f2.write(f"\n")
                
if __name__ == "__main__":
    adj_list()
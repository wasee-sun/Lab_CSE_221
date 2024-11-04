def steps_combo(s, target):
    matrix = [[0 for i in range(target + 1)] for i in range(len(s) + 1)]
    
    for n in range(len(s) + 1):
        matrix[n][0] = 1
        
    for i in range(len(matrix)):
        if i == 0:
            continue
        for j in range(target + 1):
            if j - s[i - 1] < 0:
                matrix[i][j] = matrix[i - 1][j]
            else:
                for k in range(1, s[i - 1] + 1):
                    matrix[i][j] += matrix[i][j - k]

    return matrix[len(s)][target]


def traversal():
    for n in range(1, 5):
        with open(f"input3_{n}.txt", "r") as f1:
            target = f1.readline().strip()
            steps = steps_combo([1, 2], int(target))
            print(steps)
            with open(f"output3_{n}.txt", "w") as f2:
                f2.write(f"{str(steps)}")
            
            
if __name__ == "__main__":
    traversal()
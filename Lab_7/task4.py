import numpy as np


def coin_change(c, target):
    matrix = [np.inf for i in range(target + 1)]
    matrix[0] = 0
    
    for i in range(1, target + 1):
        for coin in c:
            if i - coin < 0:
                continue
            else:
                matrix[i] = min(matrix[i - coin] + 1, matrix[i])
    
    return matrix[target]

def traversal():
    for n in range(1, 3):
        with open(f"input4_{n}.txt", "r") as f1:
            coins, target = f1.readline().strip().split()
            notes = f1.readline().strip().split()
            for i in range(int(coins)):
                notes[i] = int(notes[i])
            total_coins = coin_change(notes, int(target))
            with open(f"output4_{n}.txt", "w") as f2:
                f2.write(f"{str(total_coins)}")
                            
            
if __name__ == "__main__":
    traversal()
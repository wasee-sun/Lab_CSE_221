def div_conquer(arr):
    if len(arr) == 1:
        return arr[0]
    
    mid = len(arr) // 2
    left = div_conquer(arr[:mid])
    right = div_conquer(arr[mid:])
    
    if left > right:
        return left
    else:
        return right    
    
    
def max_ele():
    with open("input2.txt", "r") as f1:
        with open("output2.txt", "w") as f2:
            for line in f1:
                arr = f1.readline().strip().split()
                for i in range(len(arr)):
                    arr[i] = int(arr[i])
                max_elem = div_conquer(arr)
                f2.write(f"{max_elem}\n")
                

if __name__ == "__main__":
    max_ele()
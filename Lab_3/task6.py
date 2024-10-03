def partition(arr):
    pivot = arr[0]
    start_idx = 1 
    end_idx = len(arr) - 1 
    
    while end_idx >= start_idx:
        if arr[start_idx] <= pivot: 
            start_idx += 1
            continue 
            
        if arr[end_idx] > pivot: 
            end_idx -= 1
            continue 
        
        if arr[end_idx] < pivot:
            arr[start_idx], arr[end_idx] = arr[end_idx], arr[start_idx]
     
    arr[0], arr[end_idx] = arr[end_idx], arr[0] 
    
    return arr, end_idx


def index(arr, ele_idx, start_idx = 0):
    if len(arr) == 1:
        if ele_idx == start_idx:
            return arr[0]
        else:
            return False
        
    arr, idx = partition(arr)
    if start_idx + idx == ele_idx:
        return arr[idx]
    elif ele_idx < start_idx + idx:
        return index(arr[:idx], ele_idx, start_idx)
    else:
        return index(arr[idx + 1:], ele_idx, start_idx + idx + 1)
    
    
    
def kth_ele():
    with open("input6.txt", "r") as f1:
        with open("output6.txt", "w") as f2:
            for line in f1:
                arr = f1.readline().strip().split()
                for i in range(len(arr)):
                    arr[i] = int(arr[i])
                queries = f1.readline().strip().split()
                queries = int(queries[0])
                for i in range(queries):
                    idx = int(f1.readline().strip())
                    val = index(arr, idx - 1)
                    f2.write(f"{val}\n")
                    
                    
if __name__ == "__main__":
    kth_ele()
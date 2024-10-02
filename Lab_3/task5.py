def quicksort(arr):
    if len(arr) <= 1: 
        return arr
    
    pivot = arr[0] 
    arr, end_idx = partition(arr, pivot)
    
    left_arr = quicksort(arr[:end_idx]) 
    right_arr = quicksort(arr[end_idx + 1:]) 
    
    return left_arr + [pivot] + right_arr 

def partition(arr, pivot):
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


def sort():
    with open("input5.txt", "r") as f1:
        with open("output5.txt", "w") as f2:
            for line in f1:
                unsorted = f1.readline().strip().split()
                for i in range(len(unsorted)):
                    unsorted[i] = int(unsorted[i])
                sort_arr = quicksort(unsorted)
                for val in sort_arr:
                    f2.write(f"{val} ")
                f2.write(f"\n")
                
                
if __name__ == "__main__":
    sort()
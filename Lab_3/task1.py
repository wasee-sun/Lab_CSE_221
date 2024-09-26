def mergesort(arr):
    if len(arr) == 1:
        return arr
    
    mid = len(arr) // 2
    left_arr = arr[:mid]
    right_arr = arr[mid:]
    
    left_arr = mergesort(left_arr)
    right_arr = mergesort(right_arr)
    
    k_arr = []
    i = 0
    j = 0
    
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] < right_arr[j]:
            k_arr.append(left_arr[i])
            i += 1
        else:
            k_arr.append(right_arr[j])
            j += 1
    
    while i < len(left_arr):
        k_arr.append(left_arr[i])
        i += 1
    
    while j < len(right_arr):
        k_arr.append(right_arr[j])
        j += 1
        
    return k_arr


def sort():
    with open("input1.txt", "r") as f1:
        with open("output1.txt", "w") as f2:
            for line in f1:
                unsorted = f1.readline().strip().split()
                for i in range(len(unsorted)):
                    unsorted[i] = int(unsorted[i])
                sort_arr = mergesort(unsorted)
                for val in sort_arr:
                    f2.write(f"{val} ")
                f2.write(f"\n")
                
                
if __name__ == "__main__":
    sort()
                
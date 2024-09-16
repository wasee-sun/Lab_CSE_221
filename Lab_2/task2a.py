def mergesort(arr):
    if len(arr) == 1:
        return arr
    
    mid = len(arr) // 2
    left_arr = arr[:mid]
    right_arr = arr[mid:]
    
    left_arr = mergesort(left_arr)
    right_arr = mergesort(right_arr)
    
    i = 0
    j = 0
    k_arr = []
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


        
def sort_ologn():
    with open("output2a.txt", "w") as f2:
        f2.write("")
    with open("input2.txt", "r") as f1:
        for line in f1:
            arr1 = f1.readline().strip().split()
            next(f1)
            arr2 = f1.readline().strip().split()
            new_arr = arr1 + arr2
            for i in range(len(new_arr)):
                new_arr[i] = int(new_arr[i])
            with open("output2a.txt", "a") as f2:
                for ele in mergesort(new_arr):
                    f2.write(f"{ele} ")
                f2.write("\n")
                
                
sort_ologn()
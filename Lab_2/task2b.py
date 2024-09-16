def on(left_arr, right_arr):
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


def sort_on():
    with open("output2b.txt", "w") as f2:
        f2.write("")
    with open("input2.txt", "r") as f1:
        for line in f1:
            arr1 = f1.readline().strip().split()
            next(f1)
            arr2 = f1.readline().strip().split()
            for i in range(len(arr1)):
                arr1[i] = int(arr1[i])
            for i in range(len(arr2)):
                arr2[i] = int(arr2[i])
            with open("output2b.txt", "a") as f2:
                for ele in on(arr1, arr2):
                    f2.write(f"{ele} ")
                f2.write("\n")
                
                
sort_on()
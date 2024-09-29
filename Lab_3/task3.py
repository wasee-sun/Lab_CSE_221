def perms(arr):
    if len(arr) == 1:
        return arr, 0
    
    mid = len(arr) // 2
    permues = 0
    left_arr, perms1 = perms(arr[:mid])
    right_arr, perms2 = perms(arr[mid:])
    
    permues += perms1 + perms2
    
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
            permues += len(left_arr) - i
    
    while i < len(left_arr):
        k_arr.append(left_arr[i])
        i += 1
    
    while j < len(right_arr):
        k_arr.append(right_arr[j])
        j += 1
                
    return k_arr, permues

def brac():
    with open("input3.txt", "r") as f1:
        with open("output3.txt", "w") as f2:
            for line in f1:
                arr = f1.readline().strip().split()
                for i in range(len(arr)):
                    arr[i] = int(arr[i])
                arr, max_perms = perms(arr)
                f2.write(f"{max_perms}\n")
                

if __name__ == "__main__":
    brac()
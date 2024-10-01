def max_val(arr):
    if len(arr) == 1:
        return arr, 0
    
    mid = len(arr) // 2
    left_arr, max1 = max_val(arr[:mid])
    right_arr, max2 = max_val(arr[mid:])
    
    maxim = max(max1, max2)
    i = 0
    j = 0
    k_arr = []
    left_max = left_arr[-1]
    
    while i < len(left_arr) and j < len(right_arr):
        if left_max + right_arr[j]**2 > maxim:
            maxim = left_max + right_arr[j]**2
            
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
        if left_max + right_arr[j]**2 > maxim:
            maxim = left_max + right_arr[j]**2
            
        k_arr.append(right_arr[j])
        j += 1
                
    return k_arr, maxim
    
    
def max_sum():
    with open("input4.txt", "r") as f1:
        with open("output4.txt", "w") as f2:
            for line in f1:
                arr = f1.readline().strip().split()
                for i in range(len(arr)):
                    arr[i] = int(arr[i])
                arr, max_num = max_val(arr)
                f2.write(f"{max_num}\n")
                
                
if __name__ == "__main__":
    max_sum()
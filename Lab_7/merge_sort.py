def mergesort(arr):
    if len(arr) == 1: # if only one item is left return it
        return arr
    
    k_arr = [] # sorted array
    mid = len(arr) // 2 #midpoint
    left_arr = arr[:mid] # left array
    right_arr = arr[mid:] # right array
    
    left_arr = mergesort(left_arr) # recursion on left array
    right_arr = mergesort(right_arr) # recursion on right array
    
    i = 0 # index of left array
    j = 0 # index of right array
    
    while i < len(left_arr) and j < len(right_arr): # looping until both left and right index is in bound
        if left_arr[i][2] < right_arr[j][2]: # if left item is less than right item
            k_arr.append(left_arr[i])
            i += 1 # next item
        else: # if right item is less than left item
            k_arr.append(right_arr[j])
            j += 1 # next itme
    
    while i < len(left_arr): # if item left in left array
        k_arr.append(left_arr[i])
        i += 1
        
    
    while j < len(right_arr): # if item left in right array
        k_arr.append(right_arr[j])
        j += 1
        
    return k_arr # return the sorted array
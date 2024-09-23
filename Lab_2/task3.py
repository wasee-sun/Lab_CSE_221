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
        if left_arr[i][0] < right_arr[j][0]:
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


def selection(arr):
    sel_arr = []
    for start, end in arr:
        if len(sel_arr) == 0:
            sel_arr.append((start, end))
        elif sel_arr[-1][1] <= start:
            sel_arr.append((start, end))
        else:
            diff1 = sel_arr[-1][1] - sel_arr[-1][0]
            diff2 = end - start
            if diff2 < diff1:
                sel_arr[-1] = (start, end)
    return sel_arr


def activity_sel():
    with open("output3.txt", "w") as f2:
        f2.write("")
    with open("input3.txt", "r") as f1:
        for line in f1:
            interval_no = int(line.strip())
            arr = []
            for i in range(interval_no):
                start, end = f1.readline().strip().split()
                arr.append((int(start), int(end)))
            arr = mergesort(arr)
            sel_acts = selection(arr)
            with open("output3.txt", "a") as f2:
                f2.write(f"{len(sel_acts)}\n")
                for start, end in sel_acts:
                    f2.write(f"{start} {end}\n")
                    
                    

activity_sel()
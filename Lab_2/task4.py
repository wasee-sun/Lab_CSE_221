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
    length = len(arr)
    i = 0
    while i < length:
        if i == len(arr):
            break
        start = arr[i][0]
        end = arr[i][1]
        if len(sel_arr) == 0:
            sel_arr.append((start, end))
            arr = arr[:i] + arr[i+1:]
        elif sel_arr[-1][1] <= start:
            sel_arr.append((start, end))
            arr = arr[:i] + arr[i+1:]
        else:
            diff1 = sel_arr[-1][1] - sel_arr[-1][0]
            diff2 = end - start
            if diff2 < diff1:
                if len(sel_arr) > 1 and sel_arr[-1][0] == sel_arr[-2][1]:
                        i+=1
                else:
                    arr = arr[:i] + [sel_arr[-1]] + arr[i+1:]
                    sel_arr[-1] = (start, end)
            else:
                i += 1
                
    return sel_arr, arr


def activity_sel_doub():
    with open("output4.txt", "w") as f2:
        f2.write("")
    with open("input4.txt", "r") as f1:
        for line in f1:
            interval_no, people_no = line.strip().split()
            interval_no, people_no = int(interval_no), int(people_no)
            arr = []
            for i in range(interval_no):
                start, end = f1.readline().strip().split()
                arr.append((int(start), int(end)))
            arr = mergesort(arr)
            sel_acts = []
            for i in range(people_no):
                sel_arr, arr = selection(arr)
                sel_acts += sel_arr
            with open("output4.txt", "a") as f2:
                f2.write(f"{len(sel_acts)}\n")
                
                
                
activity_sel_doub()
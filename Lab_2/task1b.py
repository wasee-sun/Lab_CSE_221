#O(n) solution
def on(arr, target):
    start = 0
    end = len(arr) - 1
    while start < end:
        if arr[start] + arr[end] == target:
            return (start + 1, end + 1)
        elif arr[start] + arr[end] < target:
            start += 1
        elif arr[start] + arr[end] > target:
            end -= 1
            
            
#task 1 (b)
def idx_sum2():
    with open("output1b.txt", "w") as f2:
        f2.write("")
    with open("input1.txt", "r") as f1:
        for line in f1:
            inp_no, target = line.strip().split()
            new_arr = f1.readline().strip().split()
            for i in range(len(new_arr)):
                new_arr[i] = int(new_arr[i])
            arr = on(new_arr, int(target))
            arr_str = ""
            if arr != None:
                for val in arr:
                    arr_str += str(val) + " "
            else:
                arr_str = "IMPOSSIBLE"
            with open("output1b.txt", "a") as f2:
                f2.write(f"{arr_str}\n")
                
                
idx_sum2()
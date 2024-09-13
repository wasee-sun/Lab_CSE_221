#O(n^2) solution
def on2(arr, target):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if (arr[i])+ arr[j] == target:
                return (i + 1, j + 1)
            
#task 1 (a)
def idx_sum1():
    with open("output1a.txt", "w") as f2:
        f2.write("")
    with open("input1.txt", "r") as f1:
        for line in f1:
            inp_no, target = line.strip().split()
            new_arr = f1.readline().strip().split()
            for i in range(len(new_arr)):
                new_arr[i] = int(new_arr[i])
            arr = on2(new_arr, int(target))
            arr_str = ""
            if arr != None:
                for val in arr:
                    arr_str += str(val) + " "
            else:
                arr_str = "IMPOSSIBLE"
            with open("output1a.txt", "a") as f2:
                f2.write(f"{arr_str}\n")
                

idx_sum1()
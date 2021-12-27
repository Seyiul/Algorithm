n = int(input())
arr = list(map(int, input().split()))
sorted_arr = sorted(arr)
swap = 0

while arr != sorted_arr:
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
            swap += 1

print(swap)

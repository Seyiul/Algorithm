n = int(input())
arr = list(map(int, input().split()))
m = int(input())


start = 0
end = max(arr)

while start <= end:
    mid = (start+end)//2
    total = 0

    for a in arr:
        if a < mid:
            total += a
        else:
            total += mid

    if total <= m:
        start = mid+1
    else:
        end = mid-1

print(end)

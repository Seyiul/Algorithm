n, m = map(int, input().split())
arr = list(map(int, input().split()))

start, end = 0, max(arr)

ans = 0
while start <= end:
    mid = (start + end) // 2
    res = sum([i - mid for i in arr if i > mid])

    if res < m:
        end = mid - 1
    else:
        ans = mid
        start = mid + 1
print(ans)

import sys
input = sys.stdin.readline

N, C = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(int(input()))
arr.sort()

start, end = 1, arr[-1]-arr[0]
ans = 0

while start <= end:
    mid = (start+end)//2
    current = arr[0]
    count = 1

    for i in range(1, len(arr)):
        if current + mid <= arr[i]:
            count += 1
            current = arr[i]

    if count >= C:
        ans = mid
        start = mid + 1
    else:
        end = mid - 1

print(ans)

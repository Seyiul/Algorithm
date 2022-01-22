n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

for i in reversed(range(n)):
    for j in range(i):
        arr[i-1][j] += max(arr[i][j], arr[i][j+1])

print(arr[0][0])

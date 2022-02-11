n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

dp = [[0 for _ in range(n)] for _ in range(n)]
dp[0][0] = 1

for i in range(n):
    for j in range(n):
        if i == n-1 and j == n-1:
            print(dp[i][j])
            break
        if j + arr[i][j] < n:
            dp[i][j+arr[i][j]] += dp[i][j]
        if i + arr[i][j] < n:
            dp[i + arr[i][j]][j] += dp[i][j]

n = int(input())
arr = list(map(int, input().split()))

dp = [0 for _ in range(n)]

for i in range(n):
    dp[i] = max(dp[i-1]+arr[i], arr[i])

print(max(dp))

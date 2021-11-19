n = int(input())

dp = [0 for _ in range(n+1)]

for i in range(1, n+1):
    if i == 1:
        dp[i] = 9
    else:
        dp[i] = dp[i-1]*2 - 1
print(dp[n])

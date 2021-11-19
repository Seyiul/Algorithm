n = int(input())

dp = [0 for _ in range(1001)]

for i in range(1, 1001):
    if i == 1:
        dp[i] = 1
    elif i == 2:
        dp[i] = 2
    else:
        dp[i] = dp[i-1] + dp[i-2]

print(dp[n] % 10007)

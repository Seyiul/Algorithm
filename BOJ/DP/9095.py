n = int(input())

for i in range(n):
    x = int(input())
    dp = [0 for _ in range(x+1)]
    for i in range(1, x+1):
        if i == 1:
            dp[i] = 1
        elif i == 2:
            dp[i] = 2
        elif i == 3:
            dp[i] = 4
        else:
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

    print(dp[x])

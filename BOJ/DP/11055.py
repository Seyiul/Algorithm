N = int(input())

A = list(map(int, input().split()))

dp = [i for i in A]

for i in range(N):
    for j in range(i):
        if A[j] < A[i]:
            dp[i] = max(dp[j] + A[i], dp[i])

print(max(dp))

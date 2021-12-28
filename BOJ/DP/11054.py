n = int(input())
arr = list(map(int, input().split()))

asc_dp = [0 for _ in range(n)]
dec_dp = [0 for _ in range(n)]
for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            asc_dp[i] = max(asc_dp[i], asc_dp[j] + 1)

for i in reversed(range(n)):
    for j in range(n-1, i, -1):
        if arr[i] > arr[j]:
            dec_dp[i] = max(dec_dp[i], dec_dp[j] + 1)


dp = []
for i in range(n):
    dp.append(asc_dp[i] + dec_dp[i] + 1)

print(max(dp))

from sys import stdin


def gcd(n, m):
    while m:
        n, m = m, n % m
    return n


n = int(stdin.readline())

for i in range(n):
    ans = 0
    nums = list(map(int, stdin.readline().split()))
    for a in range(1, len(nums)):
        for b in range(a+1, len(nums)):
            ans += gcd(nums[a], nums[b])
    print(ans)

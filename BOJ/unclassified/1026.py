import itertools

n = int(input())

a = list(map(int, input().split()))
a.sort()
b = list(map(int, input().split()))
b.sort(reverse=True)

res = 0

for j in range(n):
    res += a[j] * b[j]

print(res)

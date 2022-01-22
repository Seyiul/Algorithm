from functools import cmp_to_key

k, n = map(int, input().split())

num = []

for _ in range(k):
    num.append(int(input()))

maxNum = max(num)
for _ in range(n-len(num)):
    num.append(maxNum)

num = sorted(num, key=cmp_to_key(
    lambda a, b: -1 if int(str(a)+str(b)) < int(str(b)+str(a)) else 1))

print(*num, sep='')

from sys import stdin
n = int(stdin.readline())
num = [0] * n

for i in range(n):
    num[i] = list(stdin.readline().split())

num = sorted(num, key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))
s = ""
for i in num:
    s += ('{}\n').format(i[0])
print(s)

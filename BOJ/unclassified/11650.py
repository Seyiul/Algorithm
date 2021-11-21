from sys import stdin
n = int(stdin.readline())
num = [0] * n

for i in range(n):
    num[i] = list(map(int, stdin.readline().split()))

num = sorted(num, key=lambda x: (x[0], x[1]))
s = ""
for i in num:
    s += ('{} {}\n').format(i[0], i[1])
print(s)

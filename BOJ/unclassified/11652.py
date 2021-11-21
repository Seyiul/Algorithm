from sys import stdin

n = int(stdin.readline())
num = {}
for i in range(n):
    a = int(stdin.readline())
    if a in num:
        num[a] += 1
    else:
        num[a] = 1

num = sorted(num.items(), key=lambda item: (-item[1], item[0]))
print(num[0][0])

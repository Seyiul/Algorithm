from sys import stdin
n = int(stdin.readline())
num = []
for i in range(n):
    num.append(int(stdin.readline()))
num.sort()
s = ""
for i in num:
    s += (str(i)+'\n')
print(s)

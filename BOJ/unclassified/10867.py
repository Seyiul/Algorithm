n = int(input())
num = list(map(int, input().split()))

num = list(set(num))
num.sort()

for n in num:
    print(n, end=' ')

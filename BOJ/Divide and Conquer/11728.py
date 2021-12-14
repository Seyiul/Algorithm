n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = a+b

c.sort()
c = list(map(str, c))

print(' '.join(c))

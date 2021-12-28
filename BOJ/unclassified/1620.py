import sys
input = sys.stdin.readline

n, m = map(int, input().split())
mon = {}

for i in range(n):
    a = input().rstrip()
    mon[a] = i+1
    mon[i+1] = a

for _ in range(m):
    s = input().rstrip()

    if s.isdigit():
        print(mon[int(s)])
    else:
        print(mon[s])

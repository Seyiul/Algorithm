import sys
input = sys.stdin.readline

a, p = map(int, input().split())
D = [a]

while True:
    n = list(map(int, str(D[-1])))
    n = sum(list(map(lambda i: i**p, n)))
    if n not in D:
        D.append(n)
    else:
        D.append(n)
        break
print(D.index(D.pop()))

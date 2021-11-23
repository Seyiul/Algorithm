from sys import stdin
from collections import deque
T = int(stdin.readline())

for i in range(T):
    p = stdin.readline().rstrip('\n')
    n = int(stdin.readline())
    x = deque(stdin.readline().rstrip('\n')[1:-1].split(','))

    rev = True
    flag = 0
    if n == 0:
        x = []

    for j in p:
        if j == 'R':
            rev = not rev
        elif j == 'D':
            if len(x) < 1:
                flag = 1
                print("error")
                break
            else:
                if rev:
                    x.popleft()
                else:
                    x.pop()
    if flag == 0:
        if rev:
            print("[" + ",".join(x) + "]")
        else:
            x.reverse()
            print("[" + ",".join(x) + "]")

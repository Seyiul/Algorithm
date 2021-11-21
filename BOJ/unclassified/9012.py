from sys import stdin


def checkPS(T):
    while '()' in T:
        T = T.replace('()', '')

    if len(T) == 0:
        return 'YES'
    else:
        return 'NO'


n = int(stdin.readline())
for i in range(n):
    line = input()
    print(checkPS(line))

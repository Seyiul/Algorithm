import sys
input = sys.stdin.readline


def backTracking(idx):
    for i in range(1, idx//2+1):
        if result[-i:] == result[-2*i:-i]:
            return -1
    if idx == n:
        for i in range(n):
            print(*result, sep='')
            return 0
    for i in range(1, 4):
        result.append(i)
        if backTracking(idx+1) == 0:
            return 0
        result.pop()


n = int(input())
result = []
backTracking(0)

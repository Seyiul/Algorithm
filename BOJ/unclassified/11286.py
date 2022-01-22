from sys import stdin
import heapq

input = stdin.readline

n = int(input())
arr = []

for _ in range(n):
    x = int(input())
    if x == 0:
        if len(arr) == 0:
            print('print', 0)
        else:
            print('print', heapq.heappop(arr)[1])
    else:
        if x < 0:
            heapq.heappush(arr, (-x, x))
        else:
            heapq.heappush(arr, (x, x))

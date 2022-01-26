import sys
import heapq

input = sys.stdin.readline

n = int(input())

leftHeap = []
rightHeap = []

for i in range(n):
    x = int(input())

    if len(leftHeap) == len(rightHeap):
        heapq.heappush(leftHeap, (-x, x))
    else:
        heapq.heappush(rightHeap, (x, x))

    if rightHeap and leftHeap[0][1] > rightHeap[0][0]:
        min = heapq.heappop(rightHeap)[0]
        max = heapq.heappop(leftHeap)[1]

        heapq.heappush(leftHeap, (-min, min))
        heapq.heappush(rightHeap, (max, max))

    print('답', leftHeap[0][1])

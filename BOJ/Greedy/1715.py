import sys
import heapq
input = sys.stdin.readline

n = int(input())
card = []
for _ in range(n):
    heapq.heappush(card, int(input()))

if len(card) == 1:
    print(0)
else:
    answer = 0
    while len(card) > 1:
        tmp1 = heapq.heappop(card)
        tmp2 = heapq.heappop(card)
        answer += tmp1 + tmp2
        heapq.heappush(card, tmp1+tmp2)

    print(answer)

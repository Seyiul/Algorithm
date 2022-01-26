import heapq
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

jewel = []
bag = []

for _ in range(n):
    jewel.append(list(map(int, input().split())))
for _ in range(k):
    bag.append(int(input()))

jewel.sort()
bag.sort()

ans = 0
temp = []

for i in bag:
    while jewel and i >= jewel[0][0]:
        heapq.heappush(temp, -jewel[0][1])
        heapq.heappop(jewel)

    if temp:
        ans += heapq.heappop(temp)
    elif not jewel:
        break

print(-ans)

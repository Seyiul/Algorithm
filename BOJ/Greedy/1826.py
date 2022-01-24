import heapq

n = int(input())
station = []
for i in range(n):
    station.append(list(map(int, input().split())))
l, p = map(int, input().split())

station.append([l, 0])
station.sort()

heap = []
ans = 0

for i in range(len(station)):
    if p - station[i][0] < 0:
        while heap:
            p += -heapq.heappop(heap)
            ans += 1
            if p - station[i][0] >= 0:
                break
    if len(heap) == 0 and p - station[i][0] < 0:
        ans = -1
        break
    else:
        heapq.heappush(heap, -station[i][1])

print(ans)

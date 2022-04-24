from collections import deque
from turtle import distance
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

distance = [-1] * (n+1)
distance[x] = 0

result = []


def bfs(city):

    queue = deque([])
    queue.append(city)

    while queue:
        city = queue.popleft()

        for i in graph[city]:
            if distance[i] == -1:
                distance[i] = distance[city] + 1
                queue.append(i)


bfs(x)

for i in range(1, n+1):
    if distance[i] == k:
        result.append(i)

print(*result, end='\n') if len(result) != 0 else print(-1)

import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

m, n = map(int, input().split())
graph = []
queue = deque([])
res = 0

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for _ in range(n):
    graph.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append([i, j])


def bfs():
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y

            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append([nx, ny])


bfs()
for i in graph:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)

    res = max(res, max(i))

print(res-1)

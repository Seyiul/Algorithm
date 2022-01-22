from collections import deque
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

m, n, h = map(int, input().split())
graph = []
res = 0

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

for _ in range(h):
    floor = []
    for _ in range(n):
        floor.append(list(map(int, input().split())))
    graph.append(floor)

queue = deque([])

for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 1:
                queue.append([j, k, i])


def bfs():
    while queue:
        x, y, z = queue.popleft()

        if h == 1:
            for i in range(4):
                nx, ny, nz = dx[i]+x, dy[i]+y, 0

                if 0 <= nx < n and 0 <= ny < m and graph[0][nx][ny] == 0:
                    graph[0][nx][ny] = graph[0][x][y] + 1
                    queue.append([nx, ny, 0])
        else:
            for i in range(6):
                nx, ny, nz = dx[i]+x, dy[i]+y, dz[i]+z

                if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h and graph[nz][nx][ny] == 0:
                    graph[nz][nx][ny] = graph[z][x][y] + 1
                    queue.append([nx, ny, nz])


bfs()

for i in graph:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                exit(0)

        res = max(res, max(j))

print(res-1)

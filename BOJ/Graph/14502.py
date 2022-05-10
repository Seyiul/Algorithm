from copy import deepcopy
from itertools import combinations
from collections import deque
n, m = map(int, input().split())
graph = []

# 상 하 좌 우
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]


for _ in range(n):
    graph.append(list(map(int, input().split())))

blank = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            blank.append([i, j])

walls = list(combinations(blank, 3))


def bfs(ng, x, y, v):
    queue = deque([])
    queue.append([x, y])
    v[x][y] = True

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x+dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and ng[nx][ny] == 0 and v[nx][ny] == False:
                ng[nx][ny] = 2
                v[nx][ny] = True
                queue.append([nx, ny])


max_val = 0
for wall in walls:
    new_graph = deepcopy(graph)
    for i in wall:
        new_graph[i[0]][i[1]] = 1

    visited = [[False for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 2 and visited[i][j] == False:
                bfs(new_graph, i, j, visited)

    value = 0
    for i in new_graph:
        value += i.count(0)

    if value > max_val:
        max_val = value

print(max_val)

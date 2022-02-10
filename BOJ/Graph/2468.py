from collections import deque

n = int(input())
graph = []

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(i, j, water):
    queue = deque([])
    queue.append((i, j))
    visited[i][j] = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] >= water and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))


for _ in range(n):
    graph.append(list(map(int, input().split())))

max_val = max(map(max, graph))
min_val = min(map(min, graph))

res = 0

for water in range(min_val, max_val+1):
    visited = [[0 for _ in range(n)] for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] >= water and visited[i][j] == 0:
                bfs(i, j, water)
                cnt += 1
    if cnt > res:
        res = cnt

print(res)

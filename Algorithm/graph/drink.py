from collections import deque
n, m = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(list(map(int, input())))

visited = [[0]*m for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]


def bfs(i, j):
    queue = deque([])
    queue.append([i, j])
    visited[i][j] = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 0 and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                queue.append([nx, ny])


result = 0

for i in range(n):
    for j in range(m):
        if arr[i][j] == 0 and visited[i][j] == 0:
            bfs(i, j)
            result += 1

print(result)

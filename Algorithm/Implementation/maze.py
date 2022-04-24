from collections import deque
n, m = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(list(map(int, input())))

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]


def bfs(i, j):
    queue = deque([])
    queue.append([i, j])

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 1:
                arr[nx][ny] += arr[x][y]
                queue.append([nx, ny])


bfs(0, 0)

print(arr[-1][-1])

from collections import deque

n, m = map(int, input().split())
graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
ans = []


def bfs():
    queue = deque([])
    queue.append([0, 0])
    visited[0][0] = 1
    cnt = 0

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = dx[i]+x, dy[i] + y

            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0:
                if graph[nx][ny] == 0:
                    visited[nx][ny] = 1
                    queue.append([nx, ny])

                elif graph[nx][ny] == 1:
                    graph[nx][ny] = 0
                    visited[nx][ny] = 1
                    cnt += 1

    ans.append(cnt)
    return cnt


time = 0
while 1:
    time += 1
    visited = [[0] * m for _ in range(n)]
    cnt = bfs()
    if cnt == 0:
        break

print(time-1)
print(ans[-2])

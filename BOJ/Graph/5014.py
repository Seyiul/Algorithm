from collections import deque
F, S, G, U, D = map(int, input().split())

button = [U, -D]
floor = [0 for _ in range(F+1)]
visited = [0 for _ in range(F+1)]


def bfs():
    queue = deque([S])
    visited[S] = 1

    while queue:
        x = queue.popleft()

        if x == G:
            return floor[G]

        for i in range(2):
            nx = x + button[i]

            if 1 <= nx <= F and visited[nx] == 0:
                floor[nx] = floor[x] + 1
                visited[nx] = 1
                queue.append(nx)

    if floor[G] == 0:
        return 'use the stairs'


print(bfs())

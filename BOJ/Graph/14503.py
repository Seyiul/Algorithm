n, m = map(int, input().split())
r, c, d = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

visited = [[0 for _ in range(m)] for _ in range(n)]


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def clean(x, y, d):
    global ans

    if graph[x][y] == 0:
        graph[x][y] = 2
        ans += 1

    for _ in range(4):
        nd = (d+3) % 4
        nx = x + dx[nd]
        ny = y + dy[nd]

        if graph[nx][ny] == 0:
            clean(nx, ny, nd)
            return

        d = nd

    nd = (d+2) % 4
    nx = x + dx[nd]
    ny = y + dy[nd]
    if graph[nx][ny] == 1:
        return

    clean(nx, ny, d)


ans = 0
clean(r, c, d)
print(ans)

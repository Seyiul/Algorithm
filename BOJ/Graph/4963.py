import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def dfs(x, y):

    if x < 0 or x >= h or y < 0 or y >= w:
        return False

    if graph[x][y] == 1:
        graph[x][y] = 0
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)
        return True

    return False


w, h = map(int, input().split())

while w and h:

    dx = [0, 0, 1, -1, 1, 1, -1, -1]
    dy = [1, -1, 0, 0, -1, 1, 1, -1]

    graph = []
    num = 0
    # count = 0
    for _ in range(h):
        graph.append(list(map(int, input().split())))

    for i in range(w):
        for j in range(h):
            if dfs(j, i) == True:
                num += 1
    print(num)

    w, h = map(int, input().split())

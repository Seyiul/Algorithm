import sys

input = sys.stdin.readline

graph = []

for _ in range(9):
    graph.append(list(map(int, input().split())))

zero = []
for i in range(9):
    for j in range(9):
        if graph[i][j] == 0:
            zero.append([i, j])


def checkRow(n, val):
    if val in graph[n]:
        return False
    return True


def checkCol(m, val):
    for i in range(9):
        if val == graph[i][m]:
            return False
    return True


def checkRect(n, m, val):
    nx = n//3 * 3
    ny = m//3 * 3

    for i in range(3):
        for j in range(3):
            if val == graph[nx+i][ny+j]:
                return False
    return True


def dfs(index):
    if index == len(zero):
        for g in graph:
            print(*g, sep=' ')
        exit()

    for i in range(1, 10):
        n, m = zero[index][0], zero[index][1]

        if checkRow(n, i) and checkCol(m, i) and checkRect(n, m, i):
            graph[n][m] = i
            dfs(index+1)
            graph[n][m] = 0


dfs(0)

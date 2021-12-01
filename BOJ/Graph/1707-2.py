import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def dfs(v, group):
    visited[v] = group
    for i in graph[v]:
        if visited[i] == 0:
            if not dfs(i, -group):
                return False
        elif visited[i] == visited[v]:
            return False
    return True


for _ in range(int(input())):
    v, e = map(int, sys.stdin.readline().split())

    graph = [[] for _ in range(v+1)]
    visited = [0] * (v+1)

    for i in range(e):
        a, b = map(int, input().split())
        graph[b].append(a)
        graph[a].append(b)

    bipatite = True

    for i in range(1, v+1):
        if visited[i] == 0:
            bipatite = dfs(i, 1)
            if not bipatite:
                break

    print('YES' if bipatite else 'NO')

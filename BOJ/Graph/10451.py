import sys
input = sys.stdin.readline


def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(i)


for _ in range(int(input())):
    n = int(input())
    p = list(map(int, input().split()))

    graph = [[] for _ in range(n+1)]
    visited = [False] * (n+1)
    visited[0] = True

    for i in range(1, n+1):
        graph[i].append(p[i-1])
        graph[p[i-1]].append(i)

    ans = 0

    while False in visited:
        for i in range(1, n+1):
            if visited[i] == False:
                dfs(i)
                ans += 1
    print(ans)

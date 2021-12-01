import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def dfs(v):
    global result
    visited[v] = True
    node.append(v)
    for i in graph[v]:
        if not visited[i]:
            dfs(i)
        else:
            if i in node:
                result += node[node.index(i):]


for _ in range(int(input())):
    n = int(input())
    p = list(map(int, input().split()))

    graph = [[] for _ in range(n+1)]
    visited = [False] * (n+1)
    visited[0] = True
    result = []

    for i in range(1, n+1):
        graph[i].append(p[i-1])

    ans = 0

    for i in range(1, n+1):
        if visited[i] == False:
            node = []
            dfs(i)

    print(n - len(result))

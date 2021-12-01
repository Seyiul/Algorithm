from collections import deque
import sys
sys.setrecursionlimit(10 ** 6)

K = int(sys.stdin.readline())


def DFS(v, group):
    visited[v] = group
    for i in graph_list[v]:
        if visited[i] == 0:
            if not DFS(i, -group):
                return False
        elif visited[i] == visited[v]:
            return False
    return True


def BFS(graph, start, visited):
    visited[start] = 1
    queue = deque([start])

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if visited[i] == 0:
                visited[i] = -visited[v]
                queue.append(i)
            else:
                if visited[i] == visited[v]:
                    return False
    return True


for case in range(K):
    v, e = map(int, sys.stdin.readline().split())

    graph_list = [[] for _ in range(v+1)]
    visited = [0] * (v+1)

    for i in range(e):
        node1, node2 = map(int, input().split())
        graph_list[node2].append(node1)
        graph_list[node1].append(node2)

    bipatite = True

    for k in range(1, v+1):
        if visited[k] == 0:
            bipatite = DFS(k, 1)
            if not bipatite:
                break

    print('YES' if bipatite else 'NO')

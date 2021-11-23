from collections import deque


def DFS(graph, v, visited):
    visited[v] = True
    print(v, end=' ')

    for i in graph[v]:
        if not visited[i]:
            DFS(graph, i, visited)


def BFS(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


n, m, start = map(int, input().split())
graph_list = [[] for _ in range(n+1)]
visited_bfs = [False] * (n+1)
visited_dfs = [False] * (n+1)

for i in range(m):
    node1, node2 = map(int, input().split())
    graph_list[node2].append(node1)
    graph_list[node1].append(node2)
    graph_list[node1].sort()
    graph_list[node2].sort()

DFS(graph_list, start, visited_dfs)
print()
BFS(graph_list, start, visited_bfs)

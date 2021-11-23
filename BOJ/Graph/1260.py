from collections import deque


def DFS(graph, start):
    visitied = []
    stack = [start]

    while stack:
        n = stack.pop()
        if n not in visitied:
            visitied.append(n)
            if n in graph:
                temp = list(set(graph[n])-set(visitied))
                temp.sort(reverse=True)
                stack += temp
    return visitied


def BFS(graph, start):
    visited = []
    queue = deque([start])

    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            if n in graph:
                temp = list(set(graph[n])-set(visited))
                temp.sort()
                queue += temp
    return visited


n, m, start = map(int, input().split())
graph_list = {}
for i in range(m):
    a, b = map(int, input().split())
    if a not in graph_list:
        graph_list[a] = [b]
    else:
        graph_list[a].append(b)

    if b not in graph_list:
        graph_list[b] = [a]
    else:
        graph_list[b].append(a)

print(' '.join(map(str, DFS(graph_list, start))))
print(' '.join(map(str, BFS(graph_list, start))))

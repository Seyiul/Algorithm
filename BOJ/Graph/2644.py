from collections import deque

n = int(input())
a, b = map(int, input().split())
m = int(input())


def bfs():
    queue = deque([a])

    while queue:
        n = queue.popleft()
        for i in graph[n]:
            if check[i] == 0:
                check[i] = check[n] + 1
                queue.append(i)


graph = [[] for _ in range(n+1)]
check = [0 for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

bfs()
print(check[b] if check[b] > 0 else -1)

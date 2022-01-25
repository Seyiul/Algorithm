from collections import deque
from re import L
import sys

input = sys.stdin.readline

graph = []

for _ in range(9):
    graph.append(list(map(int, input().split())))

zero = deque([])
for i in range(9):
    for j in range(9):
        if graph[i][j] == 0:
            zero.append([i, j])

while zero:
    n, m = zero.popleft()

    x_line = [x for x in range(10) if x not in graph[n]]
    if len(x_line) == 1:
        graph[n][m] = x_line[0]
        continue

    y_line = [x for x in range(10) if x not in [g[m] for g in graph]]
    if len(y_line) == 1:
        graph[n][m] = y_line[0]
        continue

    square = [x for x in range(10) if x not in sum([
        g[(m//3*3):(m//3*3) + 3] for g in graph[(n//3 * 3):(n//3 * 3)+3]], [])]
    if len(square) == 1:
        graph[n][m] = square[0]
        continue

    zero.append([n, m])


for g in graph:
    print(*g, sep=' ')

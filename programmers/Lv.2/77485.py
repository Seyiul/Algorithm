import sys


def solution(rows, columns, queries):
    answer = []
    graph = [[0] * columns for _ in range(rows)]
    num = 1
    for i in range(rows):
        for j in range(columns):
            graph[i][j] = num
            num += 1

    for query in queries:
        sx, sy, ex, ey = query[0]-1, query[1]-1, query[2]-1, query[3]-1

        temp = graph[sx][sy]
        min_val = sys.maxsize

        # 왼쪽
        for i in range(sx, ex):
            graph[i][sy] = graph[i+1][sy]
            min_val = min(min_val, graph[i+1][sy])

        # 아래
        for i in range(sy, ey):
            graph[ex][i] = graph[ex][i+1]
            min_val = min(min_val, graph[ex][i+1])

        # 오른쪽
        for i in range(ex, sx, -1):
            graph[i][ey] = graph[i-1][ey]
            min_val = min(min_val, graph[i-1][ey])

        # 위
        for i in range(ey, sy + 1, -1):
            graph[sx][i] = graph[sx][i-1]
            min_val = min(min_val, graph[sx][i-1])

        graph[sx][sy+1] = temp
        min_val = min(min_val, temp)
        answer.append(min_val)
    return answer


# print(solution(6, 6, [[2, 2, 5, 4]]))
print(solution(6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]))
# [8, 10, 25]

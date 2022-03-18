from collections import deque


def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n+1)]
    for v in edge:
        graph[v[0]].append(v[1])
        graph[v[1]].append(v[0])

    print(graph)

    visited = [False for _ in range(n+1)]

    def bfs():
        cnt = 0
        queue = deque()
        queue.append(graph[1])
        print(queue)

        while queue:
            node = queue.popleft()

            for n in node:
                if visited[n] == False:
                    visited[n] = True
                    queue.append(graph[n])

        return cnt

    answer = bfs()

    return answer


solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])

from collections import deque
t = int(input())


for _ in range(t):
    n = int(input())
    home = list(map(int, input().split()))
    conv = []

    for _ in range(n):
        conv.append(list(map(int, input().split())))

    visited = [0 for _ in range(n)]

    fest = list(map(int, input().split()))

    def bfs():
        queue = deque([])
        queue.append([home[0], home[1]])

        while queue:
            x, y = queue.popleft()

            if abs(x-fest[0]) + abs(y-fest[1]) <= 1000:
                print('happy')
                return

            for i in range(n):
                if not visited[i]:
                    new_x, new_y = conv[i]
                    if abs(x-new_x) + abs(y-new_y) <= 1000:
                        queue.append([new_x, new_y])
                        visited[i] = 1
        print('sad')
        return

    bfs()

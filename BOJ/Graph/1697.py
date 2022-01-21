from collections import deque


def bfs(queue):
    queue.append(n)
    while queue:
        v = queue.popleft()
        if v == k:
            print(time[v])
            return
        for i in (v-1, v+1, v*2):
            if 0 <= i < 100001 and not time[i]:
                time[i] = time[v] + 1
                queue.append(i)


n, k = map(int, input().split())
time = [0] * 100001

queue = deque()
bfs(queue)

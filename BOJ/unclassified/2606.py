def graph(n):
    global cnt

    if n != 1:
        cnt += 1
    visited[n] = True

    for c in computer[n]:
        if visited[c] == False:
            graph(c)


n = int(input())
p = int(input())

computer = [[] for _ in range(n+1)]


for _ in range(1, p+1):
    a, b = map(int, input().split())
    computer[a].append(b)
    computer[b].append(a)


visited = [False] * (n+1)
cnt = 0
graph(1)

print(cnt)

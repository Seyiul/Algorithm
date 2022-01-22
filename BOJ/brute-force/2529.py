k = int(input())
sign = list(input().split())
visited = [False] * 10

minResult = ''
maxResult = ''


def possible(i, j, sign):
    if sign == '>':
        return i > j
    else:
        return i < j


def backTracking(idx, s):
    global minResult, maxResult

    if idx == k+1:
        if len(minResult) == 0:
            minResult = s
        else:
            maxResult = s
        return

    for i in range(10):
        if not visited[i]:
            if idx == 0 or possible(s[len(s)-1], str(i), sign[idx-1]):
                visited[i] = True
                backTracking(idx+1, s+str(i))
                visited[i] = False


backTracking(0, '')
print(maxResult)
print(minResult)

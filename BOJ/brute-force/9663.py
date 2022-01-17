n = int(input())
arr = [0] * n
cnt = 0


def check(x):
    for i in range(x):
        if arr[x] == arr[i] or abs(arr[i]-arr[x]) == x-i:
            return False
    return True


def nQueen(x):
    global cnt
    if x == n:
        cnt += 1
        return
    for i in range(n):
        arr[x] = i
        if check(x):
            nQueen(x+1)


nQueen(0)
print(cnt)

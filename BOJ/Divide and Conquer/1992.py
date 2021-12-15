n = int(input())
arr = []

for _ in range(n):
    arr.append(list(map(int, input())))
ans = ''


def quadtree(x, y, n):
    global ans
    check = arr[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if check != arr[i][j]:
                check = -2
                break

    if check == -2:
        n = n//2
        ans += '('
        quadtree(x, y, n)

        quadtree(x, y+n, n)

        quadtree(x+n, y, n)

        quadtree(x+n, y+n, n)
        ans += ')'

    elif check == 1:
        ans += '1'
    else:
        ans += '0'


quadtree(0, 0, n)

print(ans)

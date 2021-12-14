n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

one, zero, m_one = 0, 0, 0


def paper(x, y, n):
    global one, zero, m_one
    check = arr[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if check != arr[i][j]:
                check = -2
                break

    if check == -2:
        n = n//3
        # 1
        paper(x, y, n)
        # 2
        paper(x, y+n, n)
        # 3
        paper(x, y+n*2, n)
        # 4
        paper(x+n, y, n)
        # 5
        paper(x+n, y+n, n)
        # 6
        paper(x+n, y+n*2, n)
        # 7
        paper(x+n*2, y, n)
        # 8
        paper(x+n*2, y+n, n)
        # 9
        paper(x+n*2, y+n*2, n)

    elif check == 1:
        one += 1
    elif check == 0:
        zero += 1
    else:
        m_one += 1


paper(0, 0, n)
print(m_one)
print(zero)
print(one)

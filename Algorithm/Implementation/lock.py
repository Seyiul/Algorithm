def solution(key, lock):

    def rotation(a):
        n, m = len(a), len(a[0])
        new_a = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                new_a[j][n-i-1] = a[i][j]
        return new_a

    def check_key(new_lock):
        length = len(new_lock) // 3
        for i in range(length, length * 2):
            for j in range(length, length * 2):
                if new_lock[i][j] != 1:
                    return False
        return True

    n = len(lock)
    m = len(key)
    new_lock = [[0] * (n*3) for _ in range(n * 3)]

    for i in range(n):
        for j in range(n):
            new_lock[i+n][j+n] = lock[i][j]

    for i in range(4):
        key = rotation(key)

        for x in range(n*2):
            for y in range(n*2):
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] += key[i][j]

                if check_key(new_lock) == True:
                    return True

                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] -= key[i][j]

    return False

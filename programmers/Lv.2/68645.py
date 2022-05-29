def solution(n):

    answer = []
    snail = [[0] * i for i in range(1, n+1)]

    dx = [1, 0, -1]
    dy = [0, 1, -1]

    num_range = sum(range(1, n+1))
    idx = 0
    x, y = 0, 0
    snail[0][0] = 1
    num = 2
    while num <= num_range:
        nx, ny = x + dx[idx], y + dy[idx]

        if 0 <= nx < n and 0 <= ny < len(snail[nx]) and snail[nx][ny] == 0:
            snail[nx][ny] = num
            num += 1
            x, y = nx, ny
        else:
            idx = (idx + 1) % 3

    return sum(snail, [])


print(solution(4))
print(solution(5))
print(solution(6))

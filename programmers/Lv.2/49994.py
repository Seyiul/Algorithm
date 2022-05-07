def solution(dirs):
    dir_idx = {'U': 0, 'R': 1, 'D': 2, 'L': 3}
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    road = set()
    x, y = 0, 0

    for d in dirs:

        nx, ny = x + dx[dir_idx[d]], y + dy[dir_idx[d]]

        if -5 <= nx <= 5 and -5 <= ny <= 5:
            road.add((x, y, nx, ny))
            road.add((nx, ny, x, y))

            x, y = nx, ny

    return len(road) // 2


print(solution("ULURRDLLU"))
print(solution("LULLLLLLU"))
print(solution("UDU"))
print(solution("LRLRL"))
print(solution("LLLLRLRLRLL"))
print(solution("UUUUDUDUDUUU"))

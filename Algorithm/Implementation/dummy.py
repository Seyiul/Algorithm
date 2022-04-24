n = int(input())
k = int(input())

data = [[0] * (n+1) for _ in range(n+1)]

for _ in range(k):
    a, b = map(int, input().split())
    data[a][b] = 1


l = int(input())
turns = []
for _ in range(l):
    sec, direction = input().split()
    turns.append((int(sec), direction))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def turn_direction(x):
    global cur_d
    if x == 'D':
        cur_d = (cur_d + 1) % 4
    else:
        cur_d = (cur_d - 1) % 4


head_x, head_y, cur_d = 1, 1, 1
data[head_x][head_y] = 2
time = 0
q = [(head_x, head_y)]
idx = 0
while True:
    nx = head_x + dx[cur_d]
    ny = head_y + dy[cur_d]

    if 1 <= nx <= n and 1 <= ny <= n and data[nx][ny] != 2:
        # 사과가 없는 경우
        if data[nx][ny] == 0:
            data[nx][ny] = 2
            q.append((nx, ny))
            px, py = q.pop(0)
            data[px][py] = 0

        # 사과가 있는 경우
        if data[nx][ny] == 1:
            data[nx][ny] = 2
            q.append((nx, ny))

    # 벽이나 몸통에 부딪힌 경우
    else:
        time += 1
        break

    head_x, head_y = nx, ny
    time += 1
    if idx < l and time == turns[idx][0]:
        turn_direction(turns[idx][1])
        idx += 1

print(time)

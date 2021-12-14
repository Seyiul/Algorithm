import math


def distance(nx, ny, mx, my):
    return math.sqrt(math.pow(mx-nx, 2) + math.pow(my-ny, 2))


ax, ay, bx, by, cx, cy, dx, dy = map(int, input().split())

interval = 1000000
dx1 = (bx-ax)/interval
dy1 = (by-ay)/interval
dx2 = (dx-cx)/interval
dy2 = (dy-cy)/interval

min = distance(ax, ay, cx, cy)

for i in range(1, 1000000):
    tmp = distance(ax+dx1*i, ay+dy1*i, cx+dx2*i, cy+dy2*i)

    if tmp < min:
        min = tmp

print(min)

# def threeSearch(left, right):
#     while abs(right - left) > 1e-9:
#         left3 = (2 * left + right) / 3
#         right3 = (left + 2 * right) / 3
#         if dist(left3) > dist(right3):
#             left = left3
#         else:
#             right = right3
#     return dist(left)


# def dist(t):
#     mx = ax * t + bx * (1 - t)
#     my = ay * t + by * (1 - t)
#     kx = cx * t + dx * (1 - t)
#     ky = cy * t + dy * (1 - t)
#     return ((kx - mx) ** 2 + (ky - my) ** 2) ** 0.5


# ax, ay, bx, by, cx, cy, dx, dy = map(int, input().split())
# print("%.16f" % threeSearch(0, 1))  # 비율을 1을 기준으로 했으므로

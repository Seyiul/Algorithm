import sys
from itertools import combinations

n, m = map(int, input().split())
cities = []
for _ in range(n):
    cities.append(list(map(int, input().split())))

houses = []
chickens = []

for i in range(n):
    for j in range(n):
        # 집 좌표 저장하기
        if cities[i][j] == 1:
            houses.append([i+1, j+1])
        # 치킨집 좌표 저장하기
        elif cities[i][j] == 2:
            chickens.append([i+1, j+1])

min_distance = sys.maxsize

for ch in combinations(chickens, m):
    sum = 0
    for h in houses:
        sum += min([abs(h[0]-i[0]) + abs(h[1]-i[1]) for i in ch])
    if sum < min_distance:
        min_distance = sum


print(min_distance)

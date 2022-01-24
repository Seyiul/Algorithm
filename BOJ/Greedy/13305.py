n = int(input())
road = list(map(int, input().split()))
station = list(map(int, input().split()))

minVal = station[0]
sum = 0
for i in range(n-1):
    if minVal > station[i]:
        minVal = station[i]
    sum += (minVal * road[i])

print(sum)

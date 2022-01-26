n, k = map(int, input().split())

jewel = []
bag = []
take = [False] * (n)

for _ in range(n):
    jewel.append(list(map(int, input().split())))
for _ in range(k):
    bag.append(int(input()))

jewel.sort(key=lambda x: (-x[1], x[0]))
bag.sort()

ans = 0
for i in bag:
    for j in range(len(jewel)):
        if i >= jewel[j][0] and take[j] == False:
            ans += jewel[j][1]
            take[j] = True

print(ans)

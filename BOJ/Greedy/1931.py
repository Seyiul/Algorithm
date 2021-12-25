n = int(input())
meeting = []
for _ in range(n):
    meeting.append(tuple(map(int, input().split())))

meeting.sort(key=lambda x: (x[1], x[0]))

ans = end = 0
for i, j in meeting:
    if i >= end:
        end = j
        ans += 1

print(ans)

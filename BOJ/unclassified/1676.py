n = int(input())
f = 1
for i in range(1, n+1):
    f *= i
f = list(map(int, str(f)))
ans = 0
for i in f[::-1]:
    if i == 0:
        ans += 1
    else:
        break
print(ans)

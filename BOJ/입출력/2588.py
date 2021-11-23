a = int(input())
b = int(input())
ans = a*b

b = list(map(int, str(b)))
b = b[::-1]

for i in range(3):
    print(a*b[i])

print(ans)

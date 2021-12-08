e, s, m = map(int, input().split())
y = 1
a, b, c = 1, 1, 1
while [a, b, c] != [e, s, m]:
    a += 1
    b += 1
    c += 1
    if a > 15:
        a = 1
    if b > 28:
        b = 1
    if c > 19:
        c = 1

    y += 1

print(y)

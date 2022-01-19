a, b, v = map(int, input().split())
d = (v-b)/(a-b)
print(int(d) if d == int(d) else int(d)+1)

a, b = map(int, (input().split()))
list = [i for i in range(1, a+1)]
i = 0
ans = []
while len(list):
    i += b-1
    if i >= len(list):
        i %= len(list)
    ans.append(str(list.pop(i)))

print('<', ', '.join(ans), '>', sep='')

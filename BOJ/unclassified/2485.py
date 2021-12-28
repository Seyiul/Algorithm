def gcd(x, y):
    while(y):
        x, y = y, x % y
    return x


n = int(input())
tree = []

for _ in range(n):
    tree.append(int(input()))

between = []

for i in range(n-1):
    between.append(tree[i+1]-tree[i])

g = between[0]
for i in range(1, len(between)):
    g = gcd(g, between[i])

print(len(range(tree[0], tree[-1]+1, g))-len(tree))

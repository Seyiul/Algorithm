def gcd(a, b):
    while(b):
        a, b = b, a % b
    return a


a, b = map(int, input().split())
gcd = gcd(a, b)
print(gcd)
print((a*b)//gcd)

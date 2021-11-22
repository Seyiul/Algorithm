def convert(n, base):
    T = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    num = 0
    base = int(base)
    for idx, i in enumerate(n):
        num += T.index(i) * (base**(len(n)-idx-1))
    return num


n, b = input().split()
print(convert(n, b))

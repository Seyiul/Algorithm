def convert(n, base):
    T = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    q, r = divmod(n, base)
    if q == 0:
        return T[r]
    else:
        return convert(q, base) + T[r]


n, b = map(int, (input().split()))
print(convert(n, b))

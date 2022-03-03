n, k = map(int, input().split())
p = 1000000007

F = [1 for _ in range(n+1)]

for i in range(2, n+1):
    F[i] = F[i-1] * i % p


def power(a, b):
    if b == 0:
        return 1

    if b % 2 == 0:
        return (power(a, b//2) ** 2) % p
    else:
        return ((power(a, b//2) ** 2) * a) % p


A = F[n]
B = (F[n-k] * F[k]) % p


print((A % p) * (power(B, p-2) % p) % p)

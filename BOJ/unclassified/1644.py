n = int(input())


def primeNum(n):
    num = set(range(2, n+1))
    m = int(n**0.5)
    for i in range(2, m+1):
        if i in num:
            num -= set(range(2*i, n+1, i))
    return num


def PrimeSum(c, start, end):
    if sum(c[start:end]) == n:
        return True


cnt = 0
prime = list(primeNum(n))

start = 0
end = 0

while end <= len(prime):
    tmp_sum = sum(prime[start:end])

    if tmp_sum == n:
        cnt += 1
        end += 1
    elif tmp_sum < n:
        end += 1
    else:
        start += 1

print(cnt)

import sys

num = 2000000
arr = [False, False] + [True for _ in range(num-1)]
primes = []
for i in range(2, num+1):
    if arr[i]:
        primes.append(i)
        for k in range(i+i, num, i):
            arr[k] = False


def isPrime(n):
    if n > num:
        for prime in primes:
            if prime >= n:
                break
            elif n % prime == 0:
                return False
        return True

    else:
        return arr[n]


T = int(sys.stdin.readline())

for _ in range(T):
    A, B = map(int, sys.stdin.readline().split(" "))
    s = A+B

    if s < 4:
        print("NO")

    elif s % 2 == 0:
        print("YES")

    else:
        if isPrime(s-2):
            print("YES")
        else:
            print("NO")

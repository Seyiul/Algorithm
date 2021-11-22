n = int(input())
if n == 1:
    exit()
else:
    isPrime = [True]*(n+1)

    for i in range(2, int(n**0.5)):
        if isPrime[i] == True:
            for j in range(i*2, n, i):
                if isPrime[j] == True:
                    isPrime[j] = False
    while n > 1:
        for i in range(2, n+1):
            if isPrime[i]:
                if n % i == 0:
                    n = n//i
                    print(i)
                    break

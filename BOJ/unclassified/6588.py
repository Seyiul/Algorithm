r = 1000000
isPrime = [True]*r

for i in range(2, int(r**0.5)):
    if isPrime[i] == True:
        for j in range(i*2, r, i):
            if isPrime[j] == True:
                isPrime[j] = False

n = int(input())
while n != 0:
    for i in range(3, n+1):
        if isPrime[i]:
            if isPrime[n-i]:
                print('{} = {} + {}'.format(n, i, n-i))
                break

    n = int(input())

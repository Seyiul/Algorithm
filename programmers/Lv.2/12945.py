def fib(n):
    d = [0] * (n+1)
    d[1] = 1
    d[2] = 1
    for i in range(3,n+1):
        d[i] = d[i-1] + d[i-2]
    return d[n]
def solution(n):
    return fib(n)%1234567
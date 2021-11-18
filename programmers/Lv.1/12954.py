def solution(x, n):
    return list(map(lambda i : (i*x) + x , range(n)))
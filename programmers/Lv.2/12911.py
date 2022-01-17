def solution(n):
    num = n+1
    while format(n, 'b').count('1') != format(num, 'b').count('1'):
        num += 1
    return num

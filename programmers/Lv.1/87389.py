def solution(n):
    answer = 99999999
    for i in range(1,n+1):
        if n%i == 1:
            if answer >= i:
                answer = i
    return answer
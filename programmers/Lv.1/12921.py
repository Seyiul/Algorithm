def solution(n):
    num=set(range(2,n+1))
    m = int(n**0.5)
    for i in range(2,m+1):
        if i in num:
            num-=set(range(2*i,n+1,i))
    return len(num)
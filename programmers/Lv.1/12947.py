def solution(x):
    num = sum(list(map(int,str(x))))
    return True if x%num==0 else False
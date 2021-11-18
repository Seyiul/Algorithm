def solution(s):
    result = []
    s = list(s)
    
    for i in s:
        if len(result) == 0:
            result.append(i)
        elif result[-1] == i:
            result.pop()
        elif result[-1] != i:
            result.append(i)
    

    return 1 if len(result)==0 else 0
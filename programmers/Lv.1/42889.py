def solution(N, stages):
    answer = []
    fail = 0
    for i in range(1,N+1):
        if len(stages)-fail ==0:
            answer.append(0)
        else:
            answer.append(stages.count(i)/(len(stages)-fail))
        fail += stages.count(i)
    
    result = list(zip(answer,range(1,len(answer)+1)))
    result = sorted(result, key = lambda x : x[0] , reverse = True)
    
    return [i[1] for i in result]
def solution(answers):
    std1 = [1,2,3,4,5]
    std2 = [2,1,2,3,2,4,2,5]
    std3 = [3,3,1,1,2,2,4,4,5,5]
    answer = [0,0,0]
    result = []
    
    for ans in range(len(answers)):
        if answers[ans] == std1[ans%len(std1)]:
            answer[0] += 1
        if answers[ans] == std2[ans%len(std2)]:
            answer[1] += 1
        if answers[ans] == std3[ans%len(std3)]:
            answer[2] += 1
    
    high_score = max(answer)
    
    for n in range(len(answer)):
        if high_score == answer[n]:
            result.append(n+1)
    
    return result
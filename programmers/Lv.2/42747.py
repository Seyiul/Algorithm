def solution(citations):
    answer = 0
    for i in range(max(citations), 0, -1):
        if len([num for num in citations if num >= i]) >= i:
            answer = i
            break
    return answer

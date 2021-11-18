def solution(A,B):
    answer = 0
    A.sort()
    B.sort()
    while len(A):
        answer += A.pop() * B.pop(0)
    return answer
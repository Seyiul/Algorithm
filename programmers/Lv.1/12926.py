def solution(s, n):
    answer = ''
    s = list(s)
    for i in s:
        if i.isalpha():
            if i.isupper():
                answer += chr((ord(i)-ord('A')+n)%26+ord('A'))
            else:
                answer += chr((ord(i)-ord('a')+n)%26+ord('a'))
        else:
            answer += i
        
    return answer
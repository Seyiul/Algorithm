def solution(s):
    answer = []
    
    for i in s.split(' '):
        word = ''
        for j in range(len(i)):
            if j == 0:
                word += i[j].upper()
            else:
                word += i[j].lower()
        answer.append(word)
    
    return ' '.join(answer)
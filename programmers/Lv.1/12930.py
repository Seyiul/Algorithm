def solution(s):
    answer = []
    s = s.split(' ')
    
    for words in s:
        word = ''
        for i in range(len(words)):
            if i%2 == 0:
                word += words[i].upper()
            else:
                word += words[i].lower()
        answer.append(word)
                
    return ' '.join(answer)
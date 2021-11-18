def solution(s):
    word = ['zero','one','two','three','four','five','six','seven','eight','nine','ten']
    answer = ''
    num = ''
    for i in list(s):
        if i.isalpha():
            num += i
            if num in word:
                answer += str(word.index(num))
                num = ''
        else:
            answer += i
    
    return int(answer)
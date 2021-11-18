def solution(s):
    slice = []
    
    if len(s) == 1:
        return 1
    for i in range(1,len(s)):
        list = [s[n:n+i] for n in range(0,len(s),i)]
        slice.append(list)
        
    answer = []
    for s in slice:
        result = ''
        count = 1
        word = ''
        for n in range(len(s)-1):
            if len(word) == 0:
                word = s[n]
                
            if word == s[n+1]:
                count += 1
            else:
                result += word
                if count != 1:
                    result += str(count)
                word = s[n+1]
                count = 1
        result += word
        if count != 1:
            result += str(count)
        
        answer.append(result)
        
    
    return len(min(answer, key = len))
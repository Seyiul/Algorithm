def solution(numbers, hand):
    answer = ''
    
    key = [1,2,3,4,5,6,7,8,9,'*',0,'#']
    x = [0,1,2,3]
    y = [0,1,2]
    list = []
    
    for i in x:
        for j in y:
            list.append([i,j])
            
    keypad = {key:value for key, value in zip(key,list)}
    
    current_left = '*'
    current_right = '#'
    
    for num in numbers:
        if num == 1 or num == 4 or num == 7:
            answer += 'L'
            current_left = num
        elif num == 3 or num == 6 or num == 9:
            answer += 'R'
            current_right = num
        else:
            dist_left = abs(keypad[current_left][1]- keypad[num][1]) + abs(keypad[current_left][0] - keypad[num][0])
            dist_right = abs(keypad[current_right][1] - keypad[num][1]) + abs(keypad[current_right][0] - keypad[num][0])
            if dist_left > dist_right:
                answer += 'R'
                current_right = num
            elif dist_right > dist_left:
                answer += 'L'
                current_left = num
            else:
                if hand == 'right':
                    answer += 'R'
                    current_right = num
                else:
                    answer += 'L'
                    current_left = num
    
    
    return answer
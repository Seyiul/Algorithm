def solution(a, b):
    answer = ''
    total = 0
    day = ['SUN','MON','TUE','WED','THU','FRI','SAT']    
    
    for i in range(1,a):
        if i == 2:
            total += 29
        elif i in [4,6,9,11]:
            total += 30
        else:
            total += 31
    
    total += b
    
    return day[(5+total)%7-1]
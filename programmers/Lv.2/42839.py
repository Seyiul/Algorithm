from itertools import permutations
def is_prime(n):
    if n<= 1:
        return False
    m = int(n**0.5)
    for i in range(2,m+1):
        if n%i == 0:
            return False
    return True
def solution(numbers):
    answer = 0
    number = set()
    
    for i in range(1,len(list(numbers))+1):
        num = set(map(int,map(''.join,permutations(numbers,i))))
        for i in num:
            number.add(i)
        
    for i in list(number):
        if is_prime(i):
            answer += 1
            
    return answer
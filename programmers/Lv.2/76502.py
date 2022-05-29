from collections import deque
def solution(s):
    answer = 0
    def right_parentheses(str):
        left = []
        for i in str:
            if i == '(' or i == '[' or i == '{':
                left.append(i)
            else:
                if len(left) == 0:
                    return False
                if left[-1] == '(' and i == ')':
                    left.pop()
                elif left[-1] == '{' and i == '}':
                    left.pop()
                elif left[-1] == '[' and i == ']':
                    left.pop()
                else:
                    return False
        
        if len(left) == 0:
            return True
        else:
            return False
        
    
    for i in range(len(s)):
        if right_parentheses(s[i:]+s[:i]) == True:
            answer += 1
                
    return answer
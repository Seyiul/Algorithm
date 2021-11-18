def lcm(a,b):
    for i in range(max(a,b),(a*b)+1):
        if i%a==0 and i%b==0:
            return i
def solution(arr):
    answer = lcm(arr[0],arr[1])
    for i in range(2,len(arr)):
        answer = lcm(answer,arr[i])
        
    return answer
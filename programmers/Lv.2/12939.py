def solution(s):
    nums = s.split(' ')
            
    nums = list(map(int,nums))
    
    return str(min(nums))+' '+str(max(nums))
from collections import Counter
def solution(nums):
    pick = len(nums)//2
    count = Counter(nums)
    
    if len(count) >= pick:
        return pick
    else:
        return len(count)
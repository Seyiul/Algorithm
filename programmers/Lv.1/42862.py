def solution(n, lost, reserve):   
  
    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]
    
    answer = n - len(lost)

    for i in _lost:
        if i-1 in _reserve:
            _reserve.remove(i-1)
            answer += 1
        elif i+1 in _reserve:
            _reserve.remove(i+1)
            answer += 1
            
    return answer
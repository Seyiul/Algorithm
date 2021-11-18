def solution(lottos, win_nums):
    rank = [6,6,5,4,3,2,1]
    count_win = 0
    count_zero = lottos.count(0)
    for win in win_nums:
        if win in lottos:
            count_win += 1
    
    return [rank[count_win + count_zero],rank[count_win]]
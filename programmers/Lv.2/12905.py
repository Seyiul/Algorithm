def solution(board):
    
    answer = 1 if 1 in board[0] or 1 in board[-1] else 0
    
    for i in range(1,len(board)):
        for j in range(1,len(board[i])):
            if board[i][j] == 1:
                board[i][j] = min(board[i-1][j], board[i-1][j-1], board[i][j-1]) + 1
            if answer < board[i][j]:
                answer = board[i][j]
    return answer ** 2
# [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]	
import numpy as np
def solution(board, moves):
    
    new_board = [[0 for col in range(len(board))] for row in range(len(board))]
    
    for i in range(len(board)):
        for j in range(len(board)):
            new_board[i][j] = board[j][i]
        
    board = new_board
    
    answer = 0
    doll = []
    for i in range(len(board)):
        board[i] = [item for item in board[i] if item != 0] # 0 없애기
        
    for move in moves:
        if len(board[move-1]) == 0:
            continue
        
        pick = board[move-1].pop(0)
        doll.append(pick)
            
        if len(doll)>1 and doll[-1] == doll[-2]:
            doll = doll[:-2]
            answer += 2
    return answer
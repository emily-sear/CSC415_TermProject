# https://github.com/ltbringer/tic_tac_toe/blob/master/agent.py

import random as rand
import copy
class Player:
    def __init__(self, exp_rate=0.3):
        self.learning_rate = 0.2
        self.exp_rate = exp_rate
        self.states_value = {}
    
    def play(self, board):
        count = 0
        possibleMoves = []
        
        # get a list of all the possible moves that the board has 
        for i in range(3):
            for j in range(3):
                if(board[i][j] == 0):
                    possibleMoves.append(count)
                count += 1
        move = -1 # default move
        
        for num in[-1, 1]:
            for i in possibleMoves:
                boardCopy = copy.deepcopy(board) # makes a clone of the board so you don't change the actual board
                # place our num into the first empty position
                if i == 0:
                    boardCopy[0][0] = num
                elif i == 1:
                    boardCopy[0][1] = num
                elif i == 2:
                    boardCopy[0][2] = num
                elif i == 3:
                    boardCopy[1][0] = num
                elif i == 4:
                    boardCopy[1][1] = num
                elif i == 5:
                    boardCopy[1][2] = num
                elif i == 6: 
                    boardCopy[2][0] = num
                elif i == 7: 
                    boardCopy[2][1] = num
                elif i == 8:
                    boardCopy[2][2] = num
                
                if self.isWinner(boardCopy) == num:
                    move = i
                    return move # either wins or blocks the win for the other player 
        
        # check to see if the corners are open 
        cornersOpen = []
        for i in possibleMoves:
            if i in [0,2,6,8]:
                cornersOpen.append(i)
                
        if len(cornersOpen) > 0:
            moveNum = rand.randint(0, len(cornersOpen) - 1)
            return cornersOpen[moveNum]
        
        # try & take the center 
        if 5 in possibleMoves:
            return 5
        
        edgesOpen = []
    
        for i in possibleMoves:
            if i in [1, 3, 5, 7]:
                edgesOpen.append(i)
        if len(edgesOpen) > 0:
            moveNum = rand.randint(0, len(edgesOpen) - 1)
            move = edgesOpen[moveNum]
        return move            
                
    def isWinner(self, board):
        # 1 meaning player 1 wins 
        # -1 meaning player 2 wins 
        # 2 meaning cats game 
        # 0 meaning the game is not over yet 
        
        # check rows
        for i in range(3):
            count = 0
            for j in range(3):
                if(board[i][j] == 1):
                    count += 1
                elif(board[i][j] == -1):
                    count -= 1
            if(count == 3):
                return 1
            elif(count == -3):
                return -1
        
        # check cols 
        for i in range(3):
            count = 0
            for j in range(3):
                if(board[j][i] == 1):
                    count += 1
                elif(board[j][i] == -1):
                    count -= 1
            if(count == 3):
                return 1
            elif(count == -3):
                return -1
        
        # check diganols 
        if((board[0][0] == 1 and board[1][1] == 1 and board[2][2] == 1) or (board[0][2] == 1 and board[1][1] == 1 and board[2][0] == 1)):
            return 1
        elif((board[0][0] == -1 and board[1][1] == -1 and board[2][2] == -1) or (board[0][2] == -1 and board[1][1] == -1 and board[2][0] == -1)):
            return -1
        check = True
        for i in range(3):
            for j in range(3):
                if(board[i][j] == 0):
                    check = False
        
        if(check):
            return 2
        return 0
        
        
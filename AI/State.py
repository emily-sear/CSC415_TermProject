from Player import *
class State:
    def __init__(self, player1, player2):
        self.board = [[0, 0 , 0], [0, 0 , 0], [0, 0 ,0]]
        self.player1 = player1
        self.player2 = player2
        self.turn = 1
    def showBoard(self):
        # p1: x  p2: o
        for i in range(0, 3):
            print('-------------')
            out = '| '
            for j in range(0, 3):
                if self.board[i][j] == 1:
                    token = 'x'
                if self.board[i][j] == -1:
                    token = 'o'
                if self.board[i][j] == 0:
                    token = ' '
                out += token + ' | '
            print(out)
        print('-------------')
           
    def play(self):
        check = True 
        while check:
            if(self.turn == 1):
                play = self.player1.play(self.board)
                if play == -1:
                    check = False
                elif play == 0:
                    self.board[0][0] = 1
                elif play == 1:
                    self.board[0][1] = 1
                elif play == 2:
                    self.board[0][2] = 1
                elif play == 3:
                    self.board[1][0] = 1
                elif play == 4:
                    self.board[1][1] = 1
                elif play == 5:
                    self.board[1][2] = 1
                elif play == 6: 
                    self.board[2][0] = 1
                elif play == 7: 
                    self.board[2][1] = 1
                elif play == 8:
                    self.board[2][2] = 1             
                self.showBoard()
                self.turn = -1
            else:
                play = self.player2.play(self.board)
                if play == -1:
                    check = False
                elif play == 0:
                    self.board[0][0] = -1
                elif play == 1:
                    self.board[0][1] = -1
                elif play == 2:
                    self.board[0][2] = -1
                elif play == 3:
                    self.board[1][0] = -1
                elif play == 4:
                    self.board[1][1] = -1
                elif play == 5:
                    self.board[1][2] = -1
                elif play == 6: 
                    self.board[2][0] = -1
                elif play == 7: 
                    self.board[2][1] = -1
                elif play == 8:
                    self.board[2][2] = -1
                self.showBoard()
                self.turn = 1
            
            win = self.checkWinner()
            if(win == 1):
                print("Player 1 wins")
                check = False
            elif(win == -1):
                print("Player 2 wins")
                check = False 
            elif(win == 2):
                print("Cats game")
                check = False
            
            
                
    
    def checkWinner(self):
        # 1 meaning player 1 wins 
        # -1 meaning player 2 wins 
        # 2 meaning cats game 
        # 0 meaning the game is not over yet 
        
        
        # check rows
        for i in range(3):
            count = 0
            for j in range(3):
                if(self.board[i][j] == 1):
                    count += 1
                elif(self.board[i][j] == -1):
                    count -= 1
            if(count == 3):
                return 1
            elif(count == -3):
                return -1
        
        # check cols 
        for i in range(3):
            count = 0
            for j in range(3):
                if(self.board[j][i] == 1):
                    count += 1
                elif(self.board[j][i] == -1):
                    count -= 1
            if(count == 3):
                return 1
            elif(count == -3):
                return -1
        
        # check diganols 
        if((self.board[0][0] == 1 and self.board[1][1] == 1 and self.board[2][2] == 1) or (self.board[0][2] == 1 and self.board[1][1] == 1 and self.board[2][0] == 1)):
            return 1
        elif((self.board[0][0] == -1 and self.board[1][1] == -1 and self.board[2][2] == -1) or (self.board[0][2] == -1 and self.board[1][1] == -1 and self.board[2][0] == -1)):
            return -1
        check = True
        for i in range(3):
            for j in range(3):
                if(self.board[i][j] == 0):
                    check = False
        
        if(check):
            return 2
        return 0

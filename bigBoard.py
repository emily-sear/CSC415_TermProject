from State import *
from Player import *
from HumanPlayer import *
import random
import numpy as np


class BigBoard: 
    def __init__(self, p1, humanPlayer):
        self.p1 = p1
        self.humanPlayer = humanPlayer
        
        self.turn = -1
        
        self.bigBoard = [[0,0,0],[0,0,0],[0,0,0]]
        
        self.board1 =  State(p1, humanPlayer)
        self.board2 =  State(p1, humanPlayer)
        self.board3 =  State(p1, humanPlayer)
        self.board4 =  State(p1, humanPlayer)
        self.board5 =  State(p1, humanPlayer)
        self.board6 =  State(p1, humanPlayer)
        self.board7 =  State(p1, humanPlayer)
        self.board8 =  State(p1, humanPlayer)
        self.board9 =  State(p1, humanPlayer)
    
    def train(self, rounds=1000):
        p2 = Player("p2")
        
        print("Board 1 Training")
        self.board1.train(p2, rounds)
        print("Board 2 Training")
        self.board2.train(p2, rounds*2)
        print("Board 3 Training")
        self.board3.train(p2, rounds*3)
        print("Board 4 Training")
        self.board4.train(p2, rounds*4)
        print("Board 5 Training")
        self.board5.train(p2, rounds*5)
        print("Board 6 Training")
        self.board6.train(p2, rounds*6)
        print("Board 7 Training")
        self.board7.train(p2, rounds*7)
        print("Board 8 Training")
        self.board8.train(p2, rounds*8)
        print("Board 9 Training")
        self.board9.train(p2, rounds*9)
    
    def play(self):
        check = True
        while check:
            rand = random.randint(1,9)
            print(rand)
            
            if(rand == 1 and self.board1.winner() == 0):
                print("Board 1: " )
                self.board1.showBoard()
                if(self.turn == 1):
                    self.bigBoard[0][0] = self.board1.play2(self.turn)
                    self.turn = -1
                else: 
                    self.bigBoard[0][0] = self.board1.play2(self.turn)
                    self.turn = 1
            elif(rand == 2 and self.board2.winner() == 0):
                print("Board 2: " )
                self.board2.showBoard()
                if(self.turn == 1):
                    self.bigBoard[0][1] = self.board2.play2(self.turn)
                    self.turn = -1
                else: 
                    self.bigBoard[0][1] = self.board2.play2(self.turn)
                    self.turn = 1
            elif(rand == 3 and self.board3.winner() == 0):
                print("Board 3: " )
                self.board3.showBoard()
                if(self.turn == 1):
                    self.bigBoard[0][2] = self.board3.play2(self.turn)
                    self.turn = -1
                else: 
                    self.bigBoard[0][2] = self.board3.play2(self.turn)
                    self.turn = 1
            elif(rand == 4 and self.board4.winner() == 0):
                print("Board 4: " )
                self.board4.showBoard()
                if(self.turn == 1):
                    self.bigBoard[1][0] = self.board4.play2(self.turn)
                    self.turn = -1
                else: 
                    self.bigBoard[1][0] = self.board4.play2(self.turn)
                    self.turn = 1
            elif(rand == 5 and self.board5.winner() == 0):
                print("Board 5: " )
                self.board5.showBoard()
                if(self.turn == 1):
                    self.bigBoard[1][1] = self.board5.play2(self.turn)
                    self.turn = -1
                else: 
                    self.bigBoard[1][1] = self.board5.play2(self.turn)
                    self.turn = 1
            elif(rand == 6 and self.board6.winner() == 0):
                print("Board 6: " )
                self.board6.showBoard()
                if(self.turn == 1):
                    self.bigBoard[1][2] = self.board6.play2(self.turn)
                    self.turn = -1
                else: 
                    self.bigBoard[1][2] =  self.board6.play2(self.turn)
                    self.turn = 1
            elif(rand == 7 and self.board7.winner() == 0):
                print("Board 7: " )
                self.board7.showBoard()
                if(self.turn == 1):
                    self.bigBoard[2][0] = self.board7.play2(self.turn)
                    self.turn = -1
                else: 
                    self.bigBoard[2][0] =self.board7.play2(self.turn)
                    self.turn = 1
            elif(rand == 8 and self.board8.winner() == 0):
                print("Board 8: " )
                self.board8.showBoard()
                if(self.turn == 1):
                    self.bigBoard[2][1] = self.board8.play2(self.turn)
                    self.turn = -1
                else: 
                    self.bigBoard[2][1] =self.board8.play2(self.turn)
                    self.turn = 1
            elif(rand == 9 and self.board9.winner() == 0):
                print("Board 9: " )
                self.board9.showBoard()
                if(self.turn == 1):
                    self.bigBoard[2][2] =self.board9.play2(self.turn)
                    self.turn = -1
                else: 
                    self.bigBoard[2][2] = self.board9.play2(self.turn)
                    self.turn = 1

            if(self.winner() == 1):
                print("Player 1 wins!")
                print(self.bigBoard)
                check = False
            elif(self.winner() == -1):
                print("Player 2 wins!!")
                print(self.bigBoard)
                check = False
            elif(self.winner() == 2):
                print("Cats game!")
                print(self.bigBoard)
                check = False
                
    def winner(self):
        # row
        count = 0
        for i in range(3):
            for j in range(3):
                count += self.bigBoard[i][j]
            if count == 3:
                return 1
            if count == -3:
                return -1
        count = 0
        # col
        for i in range(3):
            for j in range(3):
                count += self.bigBoard[j][i]
            if count == 3:
                return 1
            if count == -3:
                return -1
        # diagonal
        diag_sum1 = 0
        for i in range(3):
            diag_sum1 += self.bigBoard[i][i]
        diag_sum2 = 0
        for i in range(3):
            diag_sum2 += self.bigBoard[i][2-i]
        diag_sum = max(abs(diag_sum1), abs(diag_sum2))
        if diag_sum == 3:
            if diag_sum1 == 3 or diag_sum2 == 3:
                return 1
            else:
                return -1

        # tie
        # no available positions
        if len(self.availablePositions()) == 0:
            self.isEnd = True
            return 2
        
        # not end
        self.isEnd = False
        return 0

    def availablePositions(self):
        positions = []
        count = 0
        for i in range(3):
            for j in range(3):
                if self.bigBoard[i][j] == 0:
                    positions.append(count)
                count += 1
        return positions

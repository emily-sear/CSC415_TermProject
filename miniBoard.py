import pygame
from x import *
from o import * 


class MiniBoard:
    def __init__(self, window, startX, startY):
        # creating the squares for the gameboard 
        
        self.background = pygame.draw.rect(window, (0, 0, 0), ((startX + 2), (startY + 2), 146, 146))
        
        self.first = pygame.draw.rect(window, (255, 255, 255), (startX + 7.5, startY + 7.5, 40, 40))
        self.second = pygame.draw.rect(window, (255, 255, 255), (startX + 55, startY + 7.5, 40, 40))
        self.third = pygame.draw.rect(window, (255, 255, 255), (startX + 102.5, startY + 7.5, 40, 40))

        self.fourth = pygame.draw.rect(window, (255, 255, 255), (startX + 7.5, startY + 55, 40, 40))
        self.fifth = pygame.draw.rect(window, (255, 255, 255), (startX + 55, startY + 55, 40, 40))
        self.sixth = pygame.draw.rect(window, (255, 255, 255), (startX + 102.5, startY + 55, 40, 40))
        
        self.seventh = pygame.draw.rect(window, (255, 255, 255), (startX + 7.5, startY + 102.5, 40, 40))
        self.eighth = pygame.draw.rect(window, (255, 255, 255), (startX + 55, startY + 102.5, 40, 40))
        self.ninth = pygame.draw.rect(window, (255, 255, 255), (startX + 102.5, startY + 102.5, 40, 40))
    
    def getMiniGameBoard(self):
        return self.gameboard
    
    def updateMiniGameBoard(self, gameboard):
        self.gameboard = gameboard
    
    def moveMiniHumanMade(self, window, pos, drawObject):
        if self.first.collidepoint(pos) and self.gameboard[0][0] == '':
                if drawObject == 'x':
                    x = X(window, self.first.x + 5, self.first.y + 5, self.first.height - 10, self.first.width - 10)
                    self.gameboard[0][0] = 'X'
                    drawObject = 'o'
                else:
                    o = O(window, self.first.x + 20, self.first.y + 20)
                    self.gameboard[0][0] = 'O'
                    drawObject = 'x'
                firstOpen = False
        if self.second.collidepoint(pos)  and self.gameboard[0][1] == '':
            if drawObject == 'x':
                x = X(window, self.second.x + 5, self.second.y + 5, self.second.height - 10, self.second.width - 10)
                self.gameboard[0][1] = 'X'
                drawObject = 'o'
            else:
                o = O(window, self.second.x + 20 , self.second.y + 20)
                self.gameboard[0][1] = 'O'
                drawObject = 'x'
            secondOpen = False
        if self.third.collidepoint(pos)  and self.gameboard[0][2] == '':
            if drawObject == 'x':
                x = X(window, self.third.x + 5, self.third.y + 5, self.third.height - 10, self.third.width - 10)
                self.gameboard[0][2] = 'X'
                drawObject = 'o'
            else:
                o = O(window, self.third.x + 20, self.third.y + 20)
                self.gameboard[0][2] = 'O'
                drawObject = 'x'
            thirdOpen = False
        if self.fourth.collidepoint(pos)  and self.gameboard[1][0] == '':
            if drawObject == 'x':
                x = X(window, self.fourth.x + 5, self.fourth.y + 5, self.fourth.height - 10, self.fourth.width - 10)
                self.gameboard[1][0] = 'X'
                drawObject = 'o'
            else:
                o = O(window, self.fourth.x + 20, self.fourth.y + 20)
                self.gameboard[1][0] = 'O'
                drawObject = 'x' 
            fourthOpen = False 
        if self.fifth.collidepoint(pos) and self.gameboard[1][1] == '':
            if drawObject == 'x':
                x = X(window, self.fifth.x + 5, self.fifth.y + 5, self.fifth.height - 10, self.fifth.width - 10)
                self.gameboard[1][1] = 'X'
                drawObject = 'o'
            else:
                o = O(window, self.fifth.x + 20, self.fifth.y + 20)
                self.gameboard[1][1] = 'O'
                drawObject = 'x' 
            fifthOpen = False
        if self.sixth.collidepoint(pos)  and self.gameboard[1][2] == '':
            if drawObject == 'x':
                x = X(window, self.sixth.x + 5, self.sixth.y + 5, self.sixth.height - 10, self.sixth.width - 10)
                self.gameboard[1][2] = 'X'
                drawObject = 'o'
            else:
                o = O(window, self.sixth.x + 20, self.sixth.y + 20)
                self.gameboard[1][2] = 'O'
                drawObject = 'x'  
            sixthOpen = False              
        if self.seventh.collidepoint(pos)  and self.gameboard[2][0] == '':
            if drawObject == 'x':
                x = X(window, self.seventh.x + 5, self.seventh.y + 5, self.seventh.height - 10, self.seventh.width - 10)
                self.gameboard[2][0] = 'X'
                drawObject = 'o'
            else:
                o = O(window, self.seventh.x + 20, self.seventh.y + 20)
                self.gameboard[2][0] = 'O'
                drawObject = 'x'
            seventhOpen = False
        if self.eighth.collidepoint(pos)  and self.gameboard[2][1] == '':
            if drawObject == 'x':
                x = X(window, self.eighth.x + 5, self.eighth.y + 5, self.eighth.height - 10, self.eighth.width - 10)
                self.gameboard[2][1] = 'X'
                drawObject = 'o'
            else:
                o = O(window, self.eighth.x + 20, self.eighth.y + 20)
                self.gameboard[2][1] = 'O'
                drawObject = 'x' 
            eighthOpen = False             
        if self.ninth.collidepoint(pos) and self.gameboard[2][2] == '':
            if drawObject == 'x':
                x = X(window, self.ninth.x + 5, self.ninth.y + 5, self.ninth.height - 10, self.ninth.width - 10)
                self.gameboard[2][2] = 'X'
                drawObject = 'o'
            else:
                o = O(window, self.ninth.x + 20, self.ninth.y + 20)
                self.gameboard[2][2] = 'O'
                drawObject = 'x' 
            ninthOpen = False  
        return drawObject
    
    def miniAIMoveMade(self, window, num, drawObject):
        if num == 0 and self.gameboard[0][0] == '':
                if drawObject == 'x':
                    x = X(window, self.first.x + 5, self.first.y + 5, self.first.height - 10, self.first.width - 10)
                    self.gameboard[0][0] = 'X'
                    drawObject = 'o'
                else:
                    o = O(window, self.first.x + 20, self.first.y + 20)
                    self.gameboard[0][0] = 'O'
                    drawObject = 'x'
                firstOpen = False
        if num == 1 and self.gameboard[0][1] == '':
            if drawObject == 'x':
                x = X(window, self.second.x + 5, self.second.y + 5, self.second.height - 10, self.second.width - 10)
                self.gameboard[0][1] = 'X'
                drawObject = 'o'
            else:
                o = O(window, self.second.x + 20 , self.second.y + 20)
                self.gameboard[0][1] = 'O'
                drawObject = 'x'
            secondOpen = False
        if num == 2 and self.gameboard[0][2] == '':
            if drawObject == 'x':
                x = X(window, self.third.x + 5, self.third.y + 5, self.third.height - 10, self.third.width - 10)
                self.gameboard[0][2] = 'X'
                drawObject = 'o'
            else:
                o = O(window, self.third.x + 20, self.third.y + 20)
                self.gameboard[0][2] = 'O'
                drawObject = 'x'
            thirdOpen = False
        if num == 3 and self.gameboard[1][0] == '':
            if drawObject == 'x':
                x = X(window, self.fourth.x + 5, self.fourth.y + 5, self.fourth.height - 10, self.fourth.width - 10)
                self.gameboard[1][0] = 'X'
                drawObject = 'o'
            else:
                o = O(window, self.fourth.x + 20, self.fourth.y + 20)
                self.gameboard[1][0] = 'O'
                drawObject = 'x' 
            fourthOpen = False 
        if num == 4 and self.gameboard[1][1] == '':
            if drawObject == 'x':
                x = X(window, self.fifth.x + 5, self.fifth.y + 5, self.fifth.height - 10, self.fifth.width - 10)
                self.gameboard[1][1] = 'X'
                drawObject = 'o'
            else:
                o = O(window, self.fifth.x + 20, self.fifth.y + 20)
                self.gameboard[1][1] = 'O'
                drawObject = 'x' 
            fifthOpen = False
        if num == 5 and self.gameboard[1][2] == '':
            if drawObject == 'x':
                x = X(window, self.sixth.x + 5, self.sixth.y + 5, self.sixth.height - 10, self.sixth.width - 10)
                self.gameboard[1][2] = 'X'
                drawObject = 'o'
            else:
                o = O(window, self.sixth.x + 20, self.sixth.y + 20)
                self.gameboard[1][2] = 'O'
                drawObject = 'x'  
            sixthOpen = False              
        if num == 6 and self.gameboard[2][0] == '':
            if drawObject == 'x':
                x = X(window, self.seventh.x + 5, self.seventh.y + 5, self.seventh.height - 10, self.seventh.width - 10)
                self.gameboard[2][0] = 'X'
                drawObject = 'o'
            else:
                o = O(window, self.seventh.x + 20, self.seventh.y + 20)
                self.gameboard[2][0] = 'O'
                drawObject = 'x'
            seventhOpen = False
        if num == 7 and self.gameboard[2][1] == '':
            if drawObject == 'x':
                x = X(window, self.eighth.x + 5, self.eighth.y + 5, self.eighth.height - 10, self.eighth.width - 10)
                self.gameboard[2][1] = 'X'
                drawObject = 'o'
            else:
                o = O(window, self.eighth.x + 20, self.eighth.y + 20)
                self.gameboard[2][1] = 'O'
                drawObject = 'x' 
            eighthOpen = False             
        if num == 8 and self.gameboard[2][2] == '':
            if drawObject == 'x':
                x = X(window, self.ninth.x + 5, self.ninth.y + 5, self.ninth.height - 10, self.ninth.width - 10)
                self.gameboard[2][2] = 'X'
                drawObject = 'o'
            else:
                o = O(window, self.ninth.x + 20, self.ninth.y + 20)
                self.gameboard[2][2] = 'O'
                drawObject = 'x' 
            ninthOpen = False  
        return drawObject
                
    def gameMiniBoardFull(self):
        check = True
        for row in self.gameboard:
            for column in row: 
                if column == "":
                    check = False
        return check
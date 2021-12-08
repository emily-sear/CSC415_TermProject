import pygame
class Board:
    def __init__(self, window):
        # creating the squares for the gameboard 
        
        self.background = pygame.draw.rect(window, (0, 0, 0), (0,0,550,550))
        
        self.first = pygame.draw.rect(window, (255, 255, 255), (25, 25, 150, 150))
        self.second = pygame.draw.rect(window, (255, 255, 255), (200, 25, 150, 150))
        self.third = pygame.draw.rect(window, (255, 255, 255), (375, 25, 150, 150))

        self.fourth = pygame.draw.rect(window, (255, 255, 255), (25, 200, 150, 150))
        self.fifth = pygame.draw.rect(window, (255, 255, 255), (200, 200, 150, 150))
        self.sixth = pygame.draw.rect(window, (255, 255, 255), (375, 200, 150, 150))

        self.seventh = pygame.draw.rect(window, (255, 255, 255), (25, 375, 150, 150))
        self.eighth = pygame.draw.rect(window, (255, 255, 255), (200, 375, 150, 150))
        self.ninth = pygame.draw.rect(window, (255, 255, 255), (375, 375, 150, 150))

        self.gameboard = [['','',''],['', '', ''],['', '', '']]
    
    def getGameBoard(self):
        return self.gameboard
    
    def moveMade(self, row, column, person):
        self.gameboard[row][column] = person
    
    def gameBoardFull(self):
        check = True
        for row in self.gameboard:
            for column in row: 
                if column == "":
                    check = False
        return check
# Emily Sear CSC 415 
# game board made with help from https://www.youtube.com/watch?v=Gv8hsNsX5G4&t=0s
# pygame docs found here https://www.pygame.org/docs/ref/draw.html


import pygame
from pygame import draw
from pygame.constants import K_SPACE
from board import *
from x import *
from o import *
from checker import *
from winScreen import *
from miniBoard import *
import random




pygame.init()
window = pygame.display.set_mode((550, 550)) # dimensions of the window
pygame.display.set_caption("Tic Tac Toe")
GAME_FONT = pygame.freetype.SysFont("Seaford Display", 50)

board = Board(window)
miniBoard1 = MiniBoard(window, 25, 25)
miniBoard2 = MiniBoard(window, 200, 25) 
miniBoard3 = MiniBoard(window, 375, 25)
miniBoard4 = MiniBoard(window, 25, 200)
miniBoard5 = MiniBoard(window, 200, 200)
miniBoard6 = MiniBoard(window, 375, 200)
miniBoard7 = MiniBoard(window, 25, 375)
miniBoard8 = MiniBoard(window, 200, 375)
miniBoard9 = MiniBoard(window, 375, 375)

# running game 
run = True
drawObject = 'x'
firstOpen = True
secondOpen = True
thirdOpen = True
fourthOpen = True
fifthOpen = True
sixthOpen = True
seventhOpen = True
eighthOpen = True
ninthOpen = True

while run: 
    for event in pygame.event.get(): # keeps track of the mouse & keyboard inside the game 
        a = []
        if event.type == pygame.QUIT: # when you click the x, it closes the game 
            run = False
        if event.type == pygame.KEYDOWN:
            pygame.time.delay(100)
            if event.key == pygame.K_RETURN:
                rand = random.randint(1, 9)
            print(rand)
        if event.type == pygame.MOUSEBUTTONUP: # this will be used as a "click"

            pygame.time.delay(100)
            pos = pygame.mouse.get_pos() # everytime that the mouse is clicked, it will store the position
            if rand == 1 and firstOpen:
                # miniBoard1.background = pygame.draw.rect(window, (0, 255, 0), (27, 27, 146, 146))
                drawObject = miniBoard1.moveMiniMade(window, pos, drawObject)
                a = miniBoard1.getMiniGameBoard()
            if rand == 2 and secondOpen:
                drawObject = miniBoard2.moveMiniMade(window, pos, drawObject)
                a = miniBoard2.getMiniGameBoard()
            if rand == 3 and thirdOpen:
                drawObject = miniBoard3.moveMiniMade(window, pos, drawObject)
                a = miniBoard3.getMiniGameBoard()
            if rand == 4 and fourthOpen:
                drawObject = miniBoard4.moveMiniMade(window, pos, drawObject)
                a = miniBoard4.getMiniGameBoard()
            if rand == 5 and fifthOpen:
                drawObject = miniBoard5.moveMiniMade(window, pos, drawObject)
                a = miniBoard5.getMiniGameBoard()
            if rand == 6 and sixthOpen:
                drawObject = miniBoard6.moveMiniMade(window, pos, drawObject)
                a = miniBoard6.getMiniGameBoard()            
            if rand == 7 and seventhOpen:
                drawObject = miniBoard7.moveMiniMade(window, pos, drawObject)
                a = miniBoard7.getMiniGameBoard()
            if rand == 8 and eighthOpen:
                drawObject = miniBoard8.moveMiniMade(window, pos, drawObject)
                a = miniBoard8.getMiniGameBoard()        
            if rand == 9 and ninthOpen:
                drawObject = miniBoard9.moveMiniMade(window, pos, drawObject)
                a = miniBoard9.getMiniGameBoard()
        print(a)
        if checkWin(a) == 'X' or checkWin(a) == 'O':
            if(checkWin(a) == 'X'):
                if rand == 1: 
                    board.moveMade( 0, 0, 'X')
                    miniBoard1.background = pygame.draw.rect(window, (0, 255, 0), ((25 + 2), (25 + 2), 146, 146))
                elif rand == 2: 
                    board.moveMade( 0, 1, 'X')
                    miniBoard2.background = pygame.draw.rect(window, (0, 255, 0), ((200 + 2), (25 + 2), 146, 146))
                elif rand == 3: 
                    board.moveMade( 0, 2, 'X')
                    miniBoard3.background = pygame.draw.rect(window, (0, 255, 0), ((375 + 2), (25 + 2), 146, 146))
                elif rand == 4: 
                    board.moveMade(1, 0, 'X')
                    miniBoard4.background = pygame.draw.rect(window, (0, 255, 0), ((25 + 2), (200 + 2), 146, 146))
                elif rand == 5:
                    board.moveMade(1, 1, 'X')
                    miniBoard5.background = pygame.draw.rect(window, (0, 255, 0), ((200 + 2), (200 + 2), 146, 146))
                elif rand == 6:
                    board.moveMade(1, 2, 'X')
                    miniBoard6.background = pygame.draw.rect(window, (0, 255, 0), ((375 + 2), (200 + 2), 146, 146))
                elif rand == 7:
                    board.moveMade(2, 0, 'X')
                    miniBoard7.background = pygame.draw.rect(window, (0, 255, 0), ((25 + 2), (375 + 2), 146, 146))
                elif rand == 8:
                    board.moveMade(2, 1, 'X')
                    miniBoard8.background = pygame.draw.rect(window, (0, 255, 0), ((200 + 2), (375 + 2), 146, 146))
                else: 
                    board.moveMade(2, 2, 'X')
                    miniBoard9.background = pygame.draw.rect(window, (0, 255, 0), ((375 + 2), (375+ 2), 146, 146))
            elif checkWin(a) == 'O': 
                if rand == 1: 
                    board.moveMade( 0, 0, 'O')
                    miniBoard1.background = pygame.draw.rect(window, (255, 0, 0), ((25 + 2), (25 + 2), 146, 146))
                elif rand == 2: 
                    board.moveMade( 0, 1, 'O')
                    miniBoard2.background = pygame.draw.rect(window, (255, 0, 0), ((200 + 2), (25 + 2), 146, 146))
                elif rand == 3: 
                    board.moveMade( 0, 2, 'O')
                    miniBoard3.background = pygame.draw.rect(window, (255, 0, 0), ((375 + 2), (25 + 2), 146, 146))
                elif rand == 4: 
                    board.moveMade(1, 0, 'O')
                    miniBoard4.background = pygame.draw.rect(window, (255, 0, 0), ((25 + 2), (200 + 2), 146, 146))
                elif rand == 5:
                    board.moveMade(1, 1, 'O')
                    miniBoard5.background = pygame.draw.rect(window, (255, 0, 0), ((200 + 2), (200 + 2), 146, 146))
                elif rand == 6:
                    board.moveMade(1, 2, 'O')
                    miniBoard6.background = pygame.draw.rect(window, (255, 0, 0), ((375 + 2), (200 + 2), 146, 146))
                elif rand == 7:
                    board.moveMade(2, 0, 'O')
                    miniBoard7.background = pygame.draw.rect(window, (255, 0, 0), ((25 + 2), (375 + 2), 146, 146))
                elif rand == 8:
                    board.moveMade(2, 1, 'O')
                    miniBoard8.background = pygame.draw.rect(window, (255, 0, 0), ((200 + 2), (375 + 2), 146, 146))
                else: 
                    board.moveMade(2, 2, 'O')
                    miniBoard9.background = pygame.draw.rect(window, (255, 0, 0), ((375 + 2), (375 + 2), 146, 146))
            else:
                if rand == 1: 
                    board.moveMade( 0, 0, 'C')
                    miniBoard1.background = pygame.draw.rect(window, (0, 0, 255), ((25 + 2), (25 + 2), 146, 146))
                elif rand == 2: 
                    board.moveMade( 0, 1, 'C')
                    miniBoard2.background = pygame.draw.rect(window, (0, 0, 255), ((25 + 2), (200 + 2), 146, 146))
                elif rand == 3: 
                    board.moveMade( 0, 2, 'C')
                    miniBoard3.background = pygame.draw.rect(window, (0, 0, 255), ((25 + 2), (375 + 2), 146, 146))
                elif rand == 4: 
                    board.moveMade(1, 0, 'C')
                    miniBoard4.background = pygame.draw.rect(window, (0, 0, 255), ((25 + 2), (200 + 2), 146, 146))
                elif rand == 5:
                    board.moveMade(1, 1, 'C')
                    miniBoard5.background = pygame.draw.rect(window, (0, 0, 255), ((200 + 2), (200 + 2), 146, 146))
                elif rand == 6:
                    board.moveMade(1, 2, 'C')
                    miniBoard6.background = pygame.draw.rect(window, (0, 0, 255), ((375 + 2), (200 + 2), 146, 146))
                elif rand == 7:
                    board.moveMade(2, 0, 'C')
                    miniBoard7.background = pygame.draw.rect(window, (0, 0, 255), ((25 + 2), (375 + 2), 146, 146))
                elif rand == 8:
                    board.moveMade(2, 1, 'C')
                    miniBoard8.background = pygame.draw.rect(window, (0, 0, 255), ((200 + 2), (375 + 2), 146, 146))
                else: 
                    board.moveMade(2, 2, 'C')
                    miniBoard9.background = pygame.draw.rect(window, (0, 0, 255), ((375 + 2), (375 + 2), 146, 146))
        b = board.getGameBoard()
        
        if checkWin(b) == 'X' or checkWin(b) == 'O' or board.gameBoardFull():
            if(checkWin(b) == 'X'):
                win = winScreen(window)
                text_surface, rect = GAME_FONT.render("X Wins!", (255, 255, 255))
                replay_button, rect_replay = pygame.freetype.SysFont("Seaford Display", 30).render("Replay", (0, 0 ,0))
                quit_button, rect_quit = pygame.freetype.SysFont("Seaford Display", 30).render("Quit", (0, 0 ,0))

                window.blit(text_surface, (175, 250))
                window.blit(replay_button, (125, 400))
                window.blit(quit_button, (340, 400))
            elif (checkWin(a) == 'O'):
                win = winScreen(window)
                text_surface, rect = GAME_FONT.render("O Wins!", (255, 255, 255))
                replay_button, rect_replay = pygame.freetype.SysFont("Seaford Display", 30).render("Replay", (0, 0 ,0))
                quit_button, rect_quit = pygame.freetype.SysFont("Seaford Display", 30).render("Quit", (0, 0 ,0))

                window.blit(text_surface, (175, 250))
                window.blit(replay_button, (125, 400))
                window.blit(quit_button, (340, 400))
            else:
                win = winScreen(window)
                text_surface, rect = GAME_FONT.render("Cats Game!", (255, 255, 255))
                replay_button, rect_replay = pygame.freetype.SysFont("Seaford Display", 30).render("Replay", (0, 0 ,0))
                quit_button, rect_quit = pygame.freetype.SysFont("Seaford Display", 30).render("Quit", (0, 0 ,0))

                window.blit(text_surface, (150, 250))
                window.blit(replay_button, (125, 400))
                window.blit(quit_button, (340, 400))
            if(win.quit_button.collidepoint(pos)):
                run = False
            elif(win.replay_button.collidepoint(pos)):
                board = Board(window)
                drawObject = 'x'
                firstOpen = True
                secondOpen = True
                thirdOpen = True
                fourthOpen = True
                fifthOpen = True
                sixthOpen = True 
                seventhOpen = True
                eighthOpen = True
                ninthOpen = True
                    
                
    pygame.display.update()


a = board.getGameBoard()
print(a)
print(checkWin(a))

pygame.quit()
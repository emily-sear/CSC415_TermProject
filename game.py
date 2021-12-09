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
from Player import * 
from State import *
from HumanPlayer import * 
import random

pygame.init()
window = pygame.display.set_mode((550, 550)) # dimensions of the window
pygame.display.set_caption("Tic Tac Toe")
GAME_FONT = pygame.freetype.SysFont("Seaford Display", 50)

p1 = Player()
p2 = HumanPlayer()
state = State(p1, p2)
state.play()

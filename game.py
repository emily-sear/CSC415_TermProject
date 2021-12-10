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
from bigBoard import *
import random


if __name__ == "__main__":
    # training
    p1 = Player("p1")

    p2 = HumanPlayer("human")

    board = BigBoard(p1, p2)
    board.train(10000)
    board.play()
    
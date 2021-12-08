import pygame
import math
from math import *

class X:
    def __init__(self, window, x, y, height, width):
        self.x1 = pygame.draw.aaline(window, (0,0,0), [x,y], [x+width, y+height], 5)
        self.x2 = pygame.draw.aaline(window, (0,0,0), [x+width, y], [x, y+height], 5)
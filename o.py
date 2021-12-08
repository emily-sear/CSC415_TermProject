import pygame 
class O:
    def __init__(self, window, x, y):
        self.x = pygame.draw.circle(window, (0, 0, 0), (x,y), 17.5, 1)
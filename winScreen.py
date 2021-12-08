import pygame
class winScreen:
    def __init__(self, window):
        # creating the squares for the gameboard 
        self.background = pygame.draw.rect(window, (0, 0, 0), (0,0,550,550))
        
        self.replay_button = pygame.draw.rect(window, (255, 255, 255), (100, 375, 140, 70))
        self.quit_button = pygame.draw.rect(window, (255,255,255), (300, 375, 140, 70))
        
        
import pygame
from game_config import *
import Move

class Player:

    def __init__(self,x):
        
        self.rect = pygame.Rect(x,GameConfig.Y_PLATFORM,GameConfig.PLAYER_W,GameConfig.PLAYER_H)
        self.move = Move()

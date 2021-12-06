from game_config import *
import pygame

class GameState:

    def __init__(self):
        pass

    def draw(self,window) :
        window.blit(GameConfig.BACKGROUND_IMG,(0,0))
        pygame.display.update()
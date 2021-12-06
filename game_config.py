import pygame

class GameConfig:

    def init():
        GameConfig.BACKGROUND_IMG = pygame.image.load('res/background.png')



    #constantes du jeu
    WINDOW_H = 640
    WINDOW_W = 960

    PLAYER_W = 64
    PLAYER_H = 64

    Y_PLATFORM = 516
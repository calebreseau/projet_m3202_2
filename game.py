# import des modules et des autres fichiers
import pygame
from game_config import *
from game_state import *


game_state = GameState()

# fonctions utiles pour la gestion du jeu (affichage de message, rejouer, etc.)
# Boucle de jeu
def game_loop(window):
    quitting = False
    while not quitting :
        game_state.draw(window)
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                quitting = True

# Fonction principale
def main() :
#...
    pygame.init()
    GameConfig.init()
    window = pygame.display.set_mode((GameConfig.WINDOW_W,GameConfig.WINDOW_H))
    pygame.display.set_caption("Projet M3202")
    game_loop(window)
    pygame.quit()
    quit()
# Lancement de la fonction principale
main()
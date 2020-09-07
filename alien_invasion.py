# 01 crear ventana fondo negro dimensiones 1200x800 titulo cabeza ventana


import sys
import pygame

class AlienInvasion:

    def __init__(self):

        pygame.init()

        self.settings = Settings()
        self.screen = pygame.display.set_mode(( self.settings.width, self.settings.height ))
        pygame.display.set_caption("Alien Invasion")
        




    def run_game(self):

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.settings.bg_color)        
            pygame.display.flip()
                    


        



if __name__  == '__main__':

    ai = AlienInvasion()
    ai.run_game()

    

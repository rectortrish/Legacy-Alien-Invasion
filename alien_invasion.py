#Mrs. Rector - Alien Invasion Game Main File

#Creating a pygame window and responding to user input

import sys
import pygame

from settings import Settings

class AlienInvasion:
    # Overall class to manage game assests and behavior

    def __init__(self):
        #initialize the game, and create the resources

        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode ((self.settings.screen_width, self.settings.screen_height))
        
        pygame.display.set_caption ("Alien Invasion")
        

    def run_game (self):
        #Start the main loop for the game.

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill (self.settings.bg_color)

            pygame.display.flip()


if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
    


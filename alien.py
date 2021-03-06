#Alien Class

import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    #A class to represent a single alien in the fleet

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        #Load the alien image and set its rect attribute

        self.image = pygame.image.load("Images/alien.bmp")
        self.rect = self.image.get_rect()

        #Start each new alien near the left of the screen

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    

    def check_edges (self):
        #Return true if at edge

        self_rect = self.screen.get_rect()
        if self.rect.right >= self_rect.right or self.rect.left <= 0:
            return True

    def update(self):
    #moving the alien to the right

        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        
        self.rect.x = self.x

    

    

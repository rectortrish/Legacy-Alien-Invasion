# This is the ship class


import pygame

class Ship:
    #A class to manage the ship

    def __init__ (self, ai_game):
        #initialize the ship and set its starting position

        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        #Load the ship image and get its rect

        self.image = pygame.image.load("Images/ship.bmp")
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

        #Set a movement flag
        self.x = float(self.rect.x)
        
        self.moving_right = False
        self.moving_left = False
        

    def update(self):
        #Update the ship's position based on movement flags.
        
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x +=  self.settings.ship_speed

        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        self.rect.x = self.x
        
        

    def blitme (self):
        #draw the ship at its current location

        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)









        

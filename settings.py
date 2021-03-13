# Create a settings class

# A class to store all settings for Alien Invasion

class Settings:

    def __init__(self):
        #initialize the game's settings
        #Screen settings

        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed = 1.5

        self.alien_speed = 1.0
        self.fleet_direction = 1

        

        #Bullet settings

        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 3
        

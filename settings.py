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
        self.ship_limit = 3
        self.alien_speed = 1.0

        self.fleet_drop_speed = 10
        
        self.speedup_scale = 1.1
        self.score_scale = 1.5
        
        
        self.fleet_direction = 1
        
        self.initialize_dynamic_settings()

        

        #Bullet settings

        self.bullet_speed = 1.5      
        self.bullet_width = 300 #Reset bullet width at end of game      
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 3


    def initialize_dynamic_settings(self):
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0

        self.alien_points = 50

        self.fleet_direction = 1

    def increase_speed (self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)


        

        
        

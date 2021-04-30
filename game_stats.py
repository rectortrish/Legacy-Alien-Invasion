#Game stats

class GameStats:
    #Track stats for alien invasion

    def __init__(self, ai_game):
        #initialize stats
        self.settings = ai_game.settings
        self.reset_stats()
        self.high_score = 0
        
        self.game_active = False

        

    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
        self.score = 0

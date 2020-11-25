"""GameStats"""
class GameStats():
    """Track statics for Alien invasion"""
    def __init__(self, ai_setting):
        """Initialize statistics."""
        self.ai_setting = ai_setting
        self.reset_stats()

        # Active state
        self.game_active = False

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ship_left = self.ai_setting.ship_limit
        self.score = 0
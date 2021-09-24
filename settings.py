"""A class store all settings for Alien invasion."""
class Settings():
    """A class store all settings for Alien invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 920
        self.screen_height = 600
        # set the background color
        self.bg_color = (230, 230, 230)

        # ship setting
        #self.ship_speed_factor = 1.5
        self.ship_limit = 3

        # Bullet settings
        #self.bullet_speed_factor = 3
        self.bullet_width = 600
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullet_allow = 3

        # Alien setting
        #self.alien_speed_factor = 1
        self.alien_drop_speed = 40
        # The fleet of 1 represents right, -1 represents left
        #self.fleet_direction = 1

        #The game speed up
        self.speedup_scale = 1.1

        # how qickly the alien point value increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throught the game"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

        # The fleet of 1 represents right, -1 represents left
        self.fleet_direction = 1

        #scoring
        self.alien_point = 1

    def increase_speed(self):
        """Increase speed settings."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_point = int(self.alien_point * self.score_scale)
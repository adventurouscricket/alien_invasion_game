"""A class store all settings for Alien invasion."""
class Settings():
    """A class store all settings for Alien invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 800
        self.screen_height = 600
        # set the background color
        self.bg_color = (230, 230, 230)

        # ship setting
        self.ship_speed_factor = 1.5

        # Bullet settings
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullet_allow = 3
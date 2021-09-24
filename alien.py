"""Alien"""
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet."""
    
    def __init__(self, ai_setting, screen):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = screen
        self.ai_setting = ai_setting

        #Load the ailen image and load its rect attribute.
        self.image = pygame.image.load("part2/alien_invasion_game/images/alien.bmp")
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #store the alien's exact position.
        self.x = float(self.rect.x)


    def blit_me(self):
        """Draw the alien at its current location."""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Move the alien right"""
        self.x += self.ai_setting.alien_speed_factor * self.ai_setting.fleet_direction
        self.rect.x = self.x

    def check_edges(self):
        """ Return true if it reach the edge"""
        result = False
        screen_rect = self.screen.get_rect()
        if screen_rect.right <= self.rect.right or self.rect.left < 0:
            result = True
        return result
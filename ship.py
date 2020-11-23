""" Alien ship """
import pygame

class Ship():
    """ Alien ship """
    def __init__(self, ai_setting, screen):
        """Initialize the ship and set its start position."""
        self.screen = screen
        self.ai_setting = ai_setting

        # load the ship image ad get its rect.
        self.image = pygame.image.load("part2/alien_invasion_game/images/ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # start each new ship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # store a decimal value for the ship's center
        self.center = float(self.rect.centerx)

        # Movement flags
        self.moving_right = False
        self.moving_left = False

    def blit_me(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Update the ship's position based on the movement flag."""

        # Update the ship's center value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            #self.rect.centerx += 1
            self.center += self.ai_setting.ship_speed_factor
        elif self.moving_left and self.rect.left > 0:
            #self.rect.centerx -= 1
            self.center -= self.ai_setting.ship_speed_factor

        # Update rect object from self.center.
        self.rect.centerx = self.center

    def center_ship(self):
        """Center the ship"""
        self.center = self.screen_rect.centerx

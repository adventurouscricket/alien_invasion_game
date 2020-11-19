import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf

TITLE = "Alien invasion"

def main():
    """Initialize game and create a screen object."""
    pygame.init()
    ai_setting = Settings()
    screen = pygame.display.set_mode((ai_setting.screen_width, ai_setting.screen_height))
    pygame.display.set_caption(TITLE)

    # make a ship
    ship = Ship(screen)

    # Start the main loop for the game.
    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_setting, screen, ship)


main()

"""Main"""
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from score_board import ScoreBoard

TITLE = "Alien invasion"

def main():
    """Initialize game and create a screen object."""
    pygame.init()
    ai_setting = Settings()
    screen = pygame.display.set_mode((ai_setting.screen_width, ai_setting.screen_height))
    pygame.display.set_caption(TITLE)

    # make a ship
    ship = Ship(ai_setting, screen)

    # make a group store bullet in.
    bullets = Group()

    #make a group store alien
    aliens = Group()

    # create a fleet of aliens
    gf.create_fleet(ai_setting, screen, aliens, ship)

    # create a game static
    stats = GameStats(ai_setting)

    #create a score board
    sb = ScoreBoard(screen, ai_setting, stats)

    #make a button
    play_button = Button(ai_setting, screen, "Play")

    # Start the main loop for the game.
    while True:
        gf.check_events(ai_setting, screen, ship, aliens, bullets, stats ,play_button)
        if  stats.game_active:
            ship.update()
            gf.update_bullets(ai_setting, screen, stats, sb, ship, bullets, aliens)
            gf.update_aliens(ai_setting, aliens, ship, stats, bullets, screen)
        gf.update_screen(ai_setting, screen, ship, bullets, aliens, stats, play_button, sb)


main()

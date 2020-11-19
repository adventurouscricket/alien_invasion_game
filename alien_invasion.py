import sys
import pygame

TITLE = "Alien invasion"

def main():
    '''Initialize game and create a screen object.'''
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption(TITLE)

    # Start the main loop for the game.
    while True:

        # wait for keybord or mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Make the most recently drawn screen visible.
        pygame.display.flip()


main()

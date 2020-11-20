"""Functions for the game"""
import sys
import pygame
from bullet import Bullet

def check_events(ai_setting, screen, ship, bullets):
    """wait for keybord or mouse events"""
    # wait for keybord or mouse events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_setting, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        
def check_keydown_events(event, ai_setting, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_setting, screen, ship, bullets)

def fire_bullet(ai_setting, screen, ship, bullets):
    """Fire a bullet if limit not reached yet."""
    # creat a new bullet and add it to the bullets group.
    if len(bullets) < ai_setting.bullet_allow :
        bullet = Bullet(ai_setting, screen, ship)
        bullets.add(bullet)

def check_keyup_events(event, ship):        
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def update_screen(ai_setting, screen, ship, bullets):
    # Redraw the screen during each pass through the loop.
    screen.fill(ai_setting.bg_color)

    # Redraw all bullets behind the ship and aliens
    for bullet in bullets:
        bullet.draw_bullet()

    ship.blit_me()

    # Make the most recently drawn screen visible.
    pygame.display.flip()

def update_bullets(bullets):
    """Update position of bullets and get rid of old bullets."""
    # Update bullet positions.
    bullets.update()
    remove_bullet(bullets)

def remove_bullet(bullets):
    """Get rid of bullets that have disappeared."""
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    
    print(len(bullets))
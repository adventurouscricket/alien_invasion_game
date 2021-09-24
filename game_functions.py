"""Functions for the game"""
import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep

def check_events(ai_setting, screen, ship, aliens, bullets, stats ,play_button):
    """wait for keybord or mouse events"""
    # wait for keybord or mouse events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_setting, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_setting, screen, stats ,ship, aliens, bullets, play_button, mouse_x, mouse_y)

def check_play_button(ai_setting, screen, stats ,ship, aliens, bullets, play_button, mouse_x, mouse_y):
    """Start a new game when the player clicks Play."""
    if play_button.rect.collidepoint(mouse_x, mouse_y) and not stats.game_active:
        #reset the game setting
        ai_setting.initialize_dynamic_settings()

        #hide the mouse cursor
        pygame.mouse.set_visible(False)
        
        #Reset the game statistics
        stats.reset_stats()
        stats.game_active = True

        #Empty the list of aliens & bullets
        aliens.empty()
        bullets.empty()

        #Create a new fleet and center the ship
        create_fleet(ai_setting, screen, aliens, ship)
        ship.center_ship()

def check_keydown_events(event, ai_setting, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_setting, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit

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

def update_screen(ai_setting, screen, ship, bullets, aliens, stats, play_button, sb):
    # Redraw the screen during each pass through the loop.
    screen.fill(ai_setting.bg_color)

    # Redraw all bullets behind the ship and aliens
    for bullet in bullets:
        bullet.draw_bullet()

    ship.blit_me()
    #alien.blit_me()
    aliens.draw(screen)

    sb.show_score()

    #Draw the button when the game is inactive
    if not stats.game_active:
        play_button.draw_button()

    # Make the most recently drawn screen visible.
    pygame.display.flip()

def update_bullets(ai_setting, screen, stats, sb, ship, bullets, aliens):
    """Update position of bullets and get rid of old bullets."""
    # Update bullet positions.
    bullets.update()
    check_alien_bullet_conllision(ai_setting, screen, stats, sb, ship, bullets, aliens)
    remove_bullet(bullets)

    if len(aliens) == 0:
        # Destroy existing bullets and create new fleet.
        bullets.empty()
        ai_setting.increase_speed()
        create_fleet(ai_setting, screen, aliens, ship)

def check_alien_bullet_conllision(ai_setting, screen, stats, sb, ship, bullets, aliens):
    """Check for any bullets that have hit aliens.
       If so, get rid of the bullet and the alien.
    """
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if collisions:
        for alien_lst in collisions.values():
            #stats.score += ai_setting.alien_point
            stats.score += ai_setting.alien_point * len(alien_lst)
            sb.prep_score()

def remove_bullet(bullets):
    """Get rid of bullets that have disappeared."""
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    
    #print(len(bullets))

def get_number_aliens_x(ai_setting, alien_width):
    """Determine the number of aliens that fit in a row."""
    avaiable_space_x = ai_setting.screen_width - 2 * alien_width
    number_aliens_x = int(avaiable_space_x / (2 * alien_width))
    return number_aliens_x

def get_number_rows(ai_setting, ship_height, alien_height):
    '''Determine the number of rows of aliens'''
    aviable_space_y = ai_setting.screen_height - 3 * alien_height - ship_height
    number_rows = int(aviable_space_y / (2 * alien_height))

    return number_rows

def create_alien(ai_setting, screen, aliens, alien_width, alien_number, row_number):
    #crate a alien
        alien = Alien(ai_setting, screen)
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number

        aliens.add(alien)
        

def create_fleet(ai_setting, screen, aliens, ship):
    ''' Create a full fleet of aliens.'''
    alien = Alien(ai_setting, screen)
    alien_width = alien.rect.width
    number_aliens_x = get_number_aliens_x(ai_setting, alien_width)
    number_rows = get_number_rows(ai_setting, ship.rect.height, alien.rect.height)

    #create the first row of aliens
    for row in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_setting, screen, aliens, alien_width, alien_number,row)

def check_fleet_edges(ai_setting, aliens):
    """If any alien reach the edge then drop down the fleet"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_setting, aliens)
            break

def change_fleet_direction(ai_setting, aliens):
    """Drop the entire fleet and change the fleet's direction."""
    for alien in aliens.sprites():
        alien.rect.y += ai_setting.alien_drop_speed
    
    ai_setting.fleet_direction *= -1

def update_aliens(ai_setting, aliens, ship, stats, bullets, screen):
    """Update position of aliens
        Check if the fleet is at an edge,
        and then update the postions of all aliens in the fleet.
    """
    check_fleet_edges(ai_setting, aliens)
    aliens.update()

    # Check collision between ship and any aliens
    if pygame.sprite.spritecollideany(ship, aliens):
        #print("Shut down")
        ship_hit(ai_setting, aliens, ship, stats, bullets, screen)

    # Look for aliens hitting the bottom of the screen.
    check_alien_bottom(ai_setting, stats, screen, ship, aliens, bullets)

def ship_hit(ai_setting, aliens, ship, stats, bullets, screen):
    """Respond to ship being hit by alien."""
    if stats.ship_left > 0:
        #Decrement ships_left
        stats.ship_left -= 1

        # Distroy aliens and bullets
        aliens.empty()
        bullets.empty()

        # Create a new fleet & center the ship
        create_fleet(ai_setting, screen, aliens, ship)
        ship.center_ship()

        # Pause
        sleep(0.5)
    else:
        stats.game_active = False
        #show the mouse cursor
        pygame.mouse.set_visible(True)
                                

def check_alien_bottom(ai_setting, stats, screen, ship, aliens, bullets):
    """Check if any aliens have reached the bottom of the screen."""
    screen_rect = screen.get_rect()
    for alien in aliens:
        if alien.rect.bottom >= screen_rect.bottom:
            # Treat this the same as if the ship got hit.
            ship_hit(ai_setting, aliens, ship, stats, bullets, screen)
"""Button class"""
import pygame

class Button():

    def __init__(self, ai_setting, screen, content):
        """Initialize button attributes"""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        #set demensions and properties for button
        self.width, self.height = 50, 29
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Set the button's rect object and center it
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # The button's content
        self.prep_content(content)

    def prep_content(self, content):
        """Center content on the button"""
        self.content_image = self.font.render(content, True, self.text_color, self.button_color)
        self.content_image_rect = self.content_image.get_rect()
        self.content_image_rect.center = self.rect.center

    def draw_button(self):
        """Draw the button"""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.content_image, self.content_image_rect)
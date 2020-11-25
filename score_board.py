"""Score board class"""
import pygame

class ScoreBoard():
    """A class to report scoring information."""
    def __init__(self, screen, ai_setting, stats):
        """Initialize scorekeeping"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_setting = ai_setting
        self.stats = stats

        #font setting
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        #Prepare the initail score image
        self.prep_score()

    def prep_score(self):
        """Turn the score into a rendered image"""
        #score_str = str(self.stats.score)

        round_score = int(round(self.stats.score, -1))
        score_str = "{:,}".format(round_score)

        self.score_img = self.font.render(score_str, True, self.text_color, self.ai_setting.bg_color)

        #display the score at the top-right of the screen
        self.score_rect = self.score_img.get_rect()
        self.score_rect.top = 20
        self.score_rect.right = self.screen_rect.right - 20

    def show_score(self):
        """Draw sorce to screen"""
        self.screen.blit(self.score_img, self.score_rect)
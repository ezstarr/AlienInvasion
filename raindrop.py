import pygame
from pygame.sprite import Sprite


class Raindrop(Sprite):
    """Initializes Raindrop Class"""
    def __init__(self, ai_game):
        """Initialize super (sprite) class"""
        super().__init__()
        # Initializes game settings
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Initializes raindrop image
        self.image = pygame.image.load('images/raindrop.png')
        self.rect = self.image.get_rect()

        # Start each raindrop near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Create self.x to be used on line 133 in alien_invasion.py
        self.x = float(self.rect.x)

    def check_edges(self):
        """Return True if raindrop is at edge of screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.top <= screen_rect.bottom: # or self.rect.left <= 0:
            return True

    def update(self):
        """Move the alien to the right or left."""
        self.x += (self.settings.droplets_speed * self.settings.droplet_direction)
        self.rect.x = self.x
        print("update")
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
        self.y = float(self.rect.y)

    def check_edges(self):
        """Return True if raindrop.BOTTOM falls below screen"""
        screen_rect = self.screen.get_rect()
            # <rect(x, y, width, height)>
            # screen_rect = <rect(0, 0, 1200, 800)>
            # screen_rect.bottom = 800
            # self.rect = <rect(50, 50, 50, 50)>
            # self.rect.bottom = 100
        # If top of raindrop hits bottom of screen
        if self.rect.y >= screen_rect.bottom: # or self.rect.left <= 0:
            print("CHECK EDGES =================")
            return True

    def update(self):
        """Moves raindrops down by distance of droplets_speed
        self.y + speed"""
        self.y += self.settings.droplets_speed
        self.rect.y = self.y

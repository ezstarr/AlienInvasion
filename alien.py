import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """A class to represent a single alien in the fleet."""
    def __init__(self, ai_game):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position.
        self.x = float(self.rect.x)

    def check_edges(self):
        """Return True if alien is at edge of screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """Move the alien to the right or left."""
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x

class Star(Sprite):
    """Exercise 13.1 - create a grid of stars"""
    def __init__(self, ai_game):
        """Initialize and position first star"""
        super().__init__()
        self.screen = ai_game.screen

        # Load star image and set rect attribute.
        self.image = pygame.image.load('images/star.png').convert_alpha()
        self.rect = self.image.get_rect()

        # Position each star
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the star's x-coordinate(horizontal position)
        self.x = float(self.rect.x)


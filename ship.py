import pygame

class Ship:
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Movement flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False


    def update(self):
        """Update the ships position based on the movement flag."""
        if self.moving_right:
            self.rect.x += 1
            if self.rect.right > self.screen_rect.right:
                self.rect.right = self.screen_rect.right
        if self.moving_left:
            self.rect.x -= 1
            if self.rect.left < self.screen_rect.left:
                self.rect.left = self.screen_rect.left
        if self.moving_up:
            self.rect.y -= 1
            if self.rect.top < self.screen_rect.top:
                self.rect.top = self.screen_rect.top
        if self.moving_down:
            self.rect.y += 1
            if self.rect.bottom > self.screen_rect.bottom:
                self.rect.bottom = self.screen_rect.bottom


    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)


class BudgieCutOut:

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('images/budgiecutout.png')
        image_scale_factor = 0.4
        self.image = pygame.transform.scale(self.image,
                                            (self.image.get_width() * image_scale_factor,
                                             self.image.get_height() * image_scale_factor))
        self.rect = self.image.get_rect()

        # start the budgie at the left
        self.rect.left = self.screen_rect.left
        print(self.screen_rect)
        print(self.rect)

        # Movement flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False


    def update(self):
        if self.moving_right:
            self.rect.x += 1
            if self.rect.right > self.screen_rect.right:
                self.rect.right = self.screen_rect.right
        if self.moving_left:
            self.rect.x -= 1
            if self.rect.left < self.screen_rect.left:
                self.rect.left = self.screen_rect.left
        if self.moving_up:
            self.rect.y -= 1
            if self.rect.top < self.screen_rect.top:
                self.rect.top = self.screen_rect.top
        if self.moving_down:
            self.rect.y += 1
            if self.rect.bottom > self.screen_rect.bottom:
                self.rect.bottom = self.screen_rect.bottom

        # if object boundary is LESS THAN screen boundary, moving flag becomes false
        # V update this
       #if self.rect = self.screen_rect.left (1, -1 to -1199)
       # if coordinate of rect = (1, -1 to -1199)
       #  set coordingate to ()


    def blitme(self):
        self.screen.blit(self.image, self.rect)


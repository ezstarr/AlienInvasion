import sys
import pygame
from settings import Settings
from ship import Ship, BudgieCutOut


class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()
        # self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
        self.budgie = BudgieCutOut(self)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # helper methods begin with an underscore.
            self._check_events()
            self.ship.update()
            self.budgie.update()
            self._update_screen()

    def _check_events(self):
        """Respond to key-presses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # Checks KEYDOWN function
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            # Checks KEYUP function
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            # print(str(event))

    def _check_keydown_events(self, event):
        """Respond to key presses."""
        if event.key == pygame.K_RIGHT:
            self.budgie.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.budgie.moving_left = True
        elif event.key == pygame.K_UP:
            self.budgie.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.budgie.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()


    def _check_keyup_events(self, event):
        """Respond to key releases"""
        if event.key == pygame.K_RIGHT:
            self.budgie.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.budgie.moving_left = False
        elif event.key == pygame.K_UP:
            self.budgie.moving_up = False
        elif event.key == pygame.K_DOWN:                
            self.budgie.moving_down = False







                # # Cancel budgie movement
                # if event.key == pygame.K_r:
                #     self.budgie.moving_right = False
                # if event.key == pygame.K_w:
                #     self.budgie.moving_left = False


    def _update_screen(self):
        """Redraws the screen during each pass through the loop"""
        self.screen.fill(self.settings.bg_color)
        self.ship.update()
        self.budgie.update()
        self.ship.blitme()
        self.budgie.blitme()
        # Make the most recently drawn screen visible.
        pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()

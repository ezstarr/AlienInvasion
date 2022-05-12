import sys
import pygame
from settings import Settings
from ship import Ship, BudgieCutOut
from bullet import Bullet
from alien import Alien, Star
from raindrop import Raindrop
from random import randint
import random


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
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.raindrops = pygame.sprite.Group()
        self._create_fleet()
        self.stars = pygame.sprite.Group()
        self._create_stargrid()
        self._create_droplets()

        self.budgie = BudgieCutOut(self)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # helper methods begin with an underscore.
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self.budgie.update()
            self._update_screen()
            self._update_aliens()
            self._update_raindrops()

    def _create_alien(self, alien_number, row_number):
        """Create an alien and place it in the row."""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _create_fleet(self):
        """Create the fleet of aliens."""
        # Make an alien.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien.rect.width)
        number_aliens_x = available_space_x // (2 * alien_width)

        # Determine the number of rows of aliens that fit on the screen.
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)

        # Create a full fleet of aliens.
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _check_fleet_edges(self):
        """Respond appropriately if any aliens reached an edge."""
        for alien in self.aliens:
            if alien.check_edges():
                self._change_fleet_direction()
                print("change fleet direction")
                break

    def _change_fleet_direction(self):
        """Drop entire fleet and change fleet direction."""
        for alien in self.aliens:
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1
        print("change fleet direction")

    def _update_aliens(self):
        """Check if fleet is at the edge,
        then update the positions of all the aliens in the fleet."""
        self._check_fleet_edges()
        self.aliens.update()

    def _create_star(self, star_numberr, row_numberr):
        """Create a star, add it to the row."""
        star = Star(self)
        star_width, star_height = star.rect.size
        star.rect.x = ((star_width * 2) * star_numberr) + randint(-80, 80)
        star.rect.y = ((star_height + 2) * row_numberr) + randint(-80, 80)
        self.stars.add(star)

        # random_number = randint(-200, 200)
        # star.x = star_width + random_number + star_numberr
        # # star.y = star_height + random_number
        # star.rect.x = star.x
        # star.rect.y = star.y
        # # star.rect.y = star.rect.height + random_number * star.rect.height * row_numberr
        # self.stars.add(star)

    def _create_stargrid(self):
        """Exercise 13.1"""
        # Make a star
        star = Star(self)
        star_width, star_height = star.rect.size
        available_space_xx = self.settings.screen_width
        random_x = randint(1,4)
        number_stars_xx = available_space_xx // star_width

        # Find how many rows of stars can fit on screen
        available_space_yy = self.settings.screen_height
        random_number = randint(1, 4)
        number_rowss = available_space_yy // star_height

        # Create the grid of stars.
        for row_numberr in range(number_rowss):
            for star_numberr in range(number_stars_xx):
                self._create_star(star_numberr, row_numberr)

# =========================== COPIED FROM ALIEN ==============================

    def _create_raindrop(self, raindrop_number, d_row_number):
        """Create a raindrop and place it in the row."""
        raindrop = Raindrop(self)
        raindrop_width, raindrop_height = raindrop.rect.size
        raindrop.rect.x = randint(-30, 30) + ((2 * raindrop_width) * raindrop_number)
        raindrop.y = randint(-30, 30) + ((2 * raindrop.rect.height) * d_row_number)
        self.raindrops.add(raindrop)

    def _create_droplets(self):
        """Create the grid of raindrop."""
        # Make a raindrop.
        raindrop = Raindrop(self)
        raindrop_width, raindrop_height = raindrop.rect.size
        available_space_x = self.settings.screen_width - (2 * raindrop.rect.width)
        number_raindrop_x = available_space_x // (2 * raindrop_width)

        # Determine the number of rows of aliens that fit on the screen.
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - (3 * raindrop_height) - ship_height)
        number_rows = available_space_y // (2 * raindrop_height)

        # Create a full fleet of aliens.
        for d_row_number in range(number_rows):
            for raindrop_number in range(number_raindrop_x):
                self._create_raindrop(raindrop_number, d_row_number)

    def _check_droplets_edges(self):
        """Reset raindrop coordinate to 0 if check_edges returns True"""
        for raindrop in self.raindrops.sprites():
            if raindrop.check_edges():
                raindrop.y = - raindrop.rect.height + randint(-30, 130)
                raindrop.x = raindrop.x + randint(-30, 130)
                raindrop.falling_speed_offset = random.uniform(-0.3, 0.3)

    def _update_raindrops(self):
        """Check if fleet is at the edge,
        then update the positions of all the aliens in the fleet."""
        self._check_droplets_edges()
        self.raindrops.update()

# ================ END OF COPY=================

    def _check_events(self):
        """Respond to key-presses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # Checks KEYDOWN function
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
                print(event.type)
            # Checks KEYUP function
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to key presses."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Respond to key releases"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:                
            self.ship.moving_down = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        # Update bullet positions.
        self.bullets.update()
        # Get rid of bullets that have disappeared
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        # Check for any bullets that have hit aliens.
        # If so, get rid of the bullet and add the alien.
        # compares positions of arg 1 & 2. True tells pygame to delete the bullets and aliens.

        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, False, True)
        if not self.aliens:
            # Destroy existing bullets and create a new fleet.
            self.bullets.empty()
            self._create_fleet()


    def _update_screen(self):
        """Redraws the screen during each pass through the loop"""
        self.screen.fill(self.settings.bg_color)
        self.ship.update()
        # self.budgie.update()
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        # self.raindrops.draw(self.screen)
        # self.stars.draw(self.screen)
        # self.budgie.blitme()
        # Make the most recently drawn screen visible.
        pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()

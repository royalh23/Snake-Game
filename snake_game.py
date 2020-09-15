import pygame
import sys

from random import randint

from settings import Settings 
from snake import Snake
from food import Food 

class SnakeGame:
    '''The main class of the game.'''

    def __init__(self):
        '''Initialize the game assets, screen, etc.'''
        pygame.init()
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode((self.settings.screen_width,
                            self.settings.screen_height))
        pygame.display.set_caption("Snake Game")

        self.snake_parts = pygame.sprite.Group() #Will do some refactoring here.
        self.snake_part = Snake(self)  # Will move this part elsewhere.
        self.snake_parts.add(self.snake_part)
        
        self.foods = pygame.sprite.Group()
        self.food = Food(self)          # Will do some refactoring here as well.
        self.foods.add(self.food)       # Will move this part elsewhere.
       
    def run_game(self):
        '''The main loop of the game.'''
        while True:
            self._check_events()
            self._update_snake_parts()
            self._update_screen()

    def _check_events(self):
        '''Check all the events.'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        '''Check keydown events.'''
        if event.key == pygame.K_UP or event.key == pygame.K_w:
            self.snake_part.m_up = True
        elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
            self.snake_part.m_down = True
        elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
            self.snake_part.m_left = True
        elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            self.snake_part.m_right = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        '''Check keyup events.'''
        if event.key == pygame.K_UP or event.key == pygame.K_w:
            self.snake_part.m_up = False
        elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
            self.snake_part.m_down = False
        elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
            self.snake_part.m_left = False
        elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            self.snake_part.m_right = False

    def _check_snake_food_collisions(self):
        '''Check the collisions between the snake and foods.'''
        pass
      
    def _update_snake_parts(self):
        '''Update all the parts of the snake.'''
        self.snake_parts.update()
        
    def _update_screen(self):
        '''Update the screen.'''
        self.screen.fill(self.settings.bg_color)

        # Draw snake parts to the screen.
        for snake_part in self.snake_parts.sprites():
            snake_part.draw_part()

        # Draw foods to the screen.
        self.food.draw_food()

        pygame.display.flip()

if __name__ == '__main__':
    sg = SnakeGame()
    sg.run_game()
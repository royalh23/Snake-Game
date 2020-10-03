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

        self.snake = Snake(self)
        
        self.foods = pygame.sprite.Group()
        self.food = Food(self)         # Will do some refactoring here as well.
        self.foods.add(self.food)      # Will move this part elsewhere.
       
    def run_game(self):
        '''The main loop of the game.'''
        while True:
            self._check_events()
            self._update_snake()
            self._update_screen()
            self._check_snake_food_collisions()  # Will move this elsewhere.                             

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
            self.snake.m_up = True
        elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
            self.snake.m_down = True
        elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
            self.snake.m_left = True
        elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            self.snake.m_right = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        '''Check keyup events.'''
        if event.key == pygame.K_UP or event.key == pygame.K_w:
            self.snake.m_up = False
        elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
            self.snake.m_down = False
        elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
            self.snake.m_left = False
        elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            self.snake.m_right = False

    def _check_snake_food_collisions(self):
        '''Check the collisions between the snake and foods.'''
        for food in self.foods.sprites():
            if self.snake.rect.colliderect(food):
                self._food_eaten(food) # Will add some comments here.
                
    def _food_eaten(self, food):
        '''Respond to the situation in which food is eaten.'''
        self.foods.empty()
        food = Food(self)
        self.foods.add(food)   # Will add some comments here as well.
        food.spawn_food()

    def _update_snake(self):
        '''Update the snake.'''
        self.snake.update()
        
    def _update_screen(self):
        '''Update the screen.'''
        self.screen.fill(self.settings.bg_color)

        # Draw the snake to the screen.
        self.snake.draw_snake()

        # Draw foods to the screen.
        for food in self.foods.sprites():
            food.draw_food()

        pygame.display.flip()

if __name__ == '__main__':
    sg = SnakeGame()
    sg.run_game()
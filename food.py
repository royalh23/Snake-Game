import pygame
from random import randint

class Food:
    '''A class to manage the foods.'''

    def __init__(self, sg):
        '''Initialize the food rect, food color, and other assets.'''
        self.screen = sg.screen
        self.settings = sg.settings
        self.color = self.settings.food_color
        
        self.rect = pygame.Rect(0, 0, self.settings.food_width,
                        self.settings.food_height)

        # Initialize the food at a random position.
        self.spawn_food()
    
    def spawn_food(self):
        '''Position the food at a random position.'''
        self.rect.x = randint(0, self.settings.screen_width)
        self.rect.y = randint(0, self.settings.screen_height)

    def draw_food(self):
        '''Draw the food to the screen.'''
        pygame.draw.rect(self.screen, self.color, self.rect)

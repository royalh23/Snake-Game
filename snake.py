import pygame
import sys

from pygame.sprite import Sprite 

class Snake(Sprite):
    '''A class to manage the snake.'''

    def __init__(self, sg):
        '''Initialize the snake's location, size, etc.'''
        super().__init__()
        self.screen = sg.screen
        self.settings = sg.settings
        self.color = self.settings.snake_color
        self.screen_rect = self.screen.get_rect()
        
        # Create the snake's rect object and position it.
        self.rect = pygame.Rect(0,0, self.settings.snake_width,
                            self.settings.snake_height)
        self.rect.center = self.screen_rect.center

        # Get the precise coordinates of the snake.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Set movement flags.
        self.m_right = False
        self.m_left = False
        self.m_up = False
        self.m_down = False

    def update(self):
        '''Update the position of the snake.'''
        if self.m_right and self.rect.right < self.screen_rect.right:                    
            self.x += self.settings.snake_speed
        if self.m_left and self.rect.left > self.screen_rect.left:
            self.x -= self.settings.snake_speed
        if self.m_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.snake_speed
        if self.m_up and self.rect.top > self.screen_rect.top:
            self.y -= self.settings.snake_speed

        self.rect.x = self.x
        self.rect.y = self.y
        
    def draw(self):
        '''Draw the snake to the screen.'''
        pygame.draw.rect(self.screen, self.color, self.rect)
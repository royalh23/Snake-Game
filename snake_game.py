import pygame
import sys

from settings import Settings 
from snake import Snake

class SnakeGame:
    '''The main class of the game.'''

    def __init__(self):
        '''Initialize the game assets, screen, etc.'''
        pygame.init()
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode((self.settings.screen_width,
                            self.settings.screen_height))
        pygame.display.set_caption("Snake Game")

        self.snake_parts = pygame.sprite.Group()
        self.snake_part = Snake(self)
        self.snake_parts.add(self.snake_part)

    def run_game(self):
        '''The main loop of the game.'''
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)
            
            self.snake_parts.update()
            self._update_screen()

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

    def _update_screen(self):
        '''Update the screen.'''
        self.screen.fill(self.settings.bg_color)

        for snake_part in self.snake_parts.sprites():
            snake_part.draw()

        pygame.display.flip()

if __name__ == '__main__':
    sg = SnakeGame()
    sg.run_game()
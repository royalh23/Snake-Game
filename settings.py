class Settings:
    '''Class for game settings.'''

    def __init__(self):
        '''Initialize the game settings.'''

        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (119, 181, 254)  # Blue color

        # Snake settings
        self.snake_width = 20
        self.snake_height = 20
        self.snake_color = (255, 255, 0)  # Yellow color
        self.snake_speed = 1

        # Food settings
        self.food_width = 10
        self.food_height = 10
        self.food_color = (139, 69, 19)  # Brown color
import pygame

class PlayRect():
    
    def __init__(self, screen, pong_settings):
        self.screen = screen
        self.pong_settings = pong_settings
        self.rect_x = 350
        self.rect_y = 590
        self.moving_right = False
        self.moving_left = False
     
    def update(self):
        if (self.moving_right and self.rect_x < (self.pong_settings.screen_width
        - self.pong_settings.rect_width)):
            self.rect_x += self.pong_settings.rect_xinc
        if self.moving_left and self.rect_x > 0:
            self.rect_x -= self.pong_settings.rect_yinc
            
    def draw_rect(self):
        pygame.draw.rect(self.screen,
                         self.pong_settings.rect_color,
                            (self.rect_x,
                             self.rect_y,
                             self.pong_settings.rect_width,
                             self.pong_settings.rect_height
                            )
                         )
    
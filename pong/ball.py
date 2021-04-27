from time import sleep

import pygame
from random import randint, choice

class Ball():
    def __init__(self, screen, pong_settings):
        """初始化小球并设置其初始位置"""
        self.screen = screen
        self.pong_settings = pong_settings
        self.ball_r = self.pong_settings.ball_r
        self.ball_start()
        
    def ball_start(self):
        """start ball"""
        self.ball_x = randint(self.ball_r,
                self.pong_settings.screen_width - self.ball_r)
        self.ball_y = randint((self.ball_r + 50), 100)
        self.ball_ysgn = 1
        self.xsgn_random()
        self.scale = self.pong_settings.scale
        
    def xsgn_random(self):
        """xsgn random"""
        self.ball_xsgn = choice([-1, 0, 1])
        
    def ysgn_random(self):
        """ysgn random"""
        self.ball_ysgn = choice([-1, 1])
        
    def check_edge(self, stats, sb):
        """ check edge """
        self.check_leftright_edge()
        self.check_up_edge()
        self.check_down_edge(stats, sb)
        
    def check_leftright_edge(self):
        """ left right edge """
        if (self.ball_x <= self.ball_r or
            self.ball_x >= (self.pong_settings.screen_width - self.ball_r)):
            self.ball_xsgn *= -1
            self.ysgn_random()
        
    def check_up_edge(self):
        """ up edge """ 
        if self.ball_y <= 0:
            self.xsgn_random()
            self.ball_ysgn *= -1
            
    def check_down_edge(self, stats, sb):
        """ down edge """    
        if self.ball_y > self.pong_settings.screen_height - self.ball_r:
            stats.left -= 1
            sb.prep_left()
            
            if stats.left > 0:                
                sleep(0.5)
            
                self.ball_start()
            else:
                stats.game_active = False
                pygame.mouse.set_visible(True)
        
    def update(self, stats, sb):
        """move ball"""
        self.check_edge(stats, sb)
        self.ball_x += (self.ball_xsgn * self.pong_settings.ball_xinc * self.scale)
        self.ball_y += (self.ball_ysgn * self.pong_settings.ball_yinc * self.scale)
                
    def draw_ball(self):
        # 画出小球
        pygame.draw.circle(self.screen, self.pong_settings.ball_color, 
                    (self.ball_x, self.ball_y), self.pong_settings.ball_r, 0)
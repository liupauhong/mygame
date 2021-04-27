import sys

import pygame

from settings import Settings
import game_function as gf
from ball import Ball
from play_rect import PlayRect
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button

def run_game():
    
    pygame.init()
    pong_settings = Settings()
    screen = pygame.display.set_mode(
        (pong_settings.screen_width, pong_settings.screen_height))
    pygame.display.set_caption("Pong")
    
    play_button = Button(screen, pong_settings, "Play")
    
    
    # 创建一个小球
    ball = Ball(screen, pong_settings)
    
    # 创建一个挡板
    rect = PlayRect(screen, pong_settings)
    
    # 创建一个用于储存游戏的统计信息实例
    stats = GameStats(pong_settings)
    # 创建记分牌
    sb = Scoreboard(screen, pong_settings, stats)
    
    while True:       
        gf.check_events(ball, rect, stats, play_button)
        
        if stats.game_active:
            ball.update(stats, sb)
            rect.update()
            gf.check_colliderect(ball, rect, stats, sb)
            
        gf.update_screen(screen, pong_settings, ball, rect, sb, stats, play_button)
        
run_game()
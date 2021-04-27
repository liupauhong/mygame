import sys

import pygame

def check_keydown_events(event, rect):
    """key down"""
    if event.key == pygame.K_q:
        sys.exit()
    elif event.key == pygame.K_LEFT:
        rect.moving_left = True
    elif event.key == pygame.K_RIGHT:
        rect.moving_right = True

def check_keyup_events(event, rect):
    """key up"""
    if event.key == pygame.K_LEFT:
        rect.moving_left = False
    elif event.key == pygame.K_RIGHT:
        rect.moving_right = False

def check_play_button(ball, stats, play_button, mouse_x, mouse_y):
    """响应Play 按钮单击"""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y) 
    if button_clicked  and not stats.game_active:
        pygame.mouse.set_visible(False)
        ball.ball_start()
        stats.reset_stats()
        stats.game_active = True
        
def check_events(ball, rect, stats, play_button):
    """响应按键和鼠标事件"""
    # 监视键盘和鼠标事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()            
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, rect)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, rect)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ball, stats, play_button, mouse_x, mouse_y)

def check_colliderect(ball, rect, stats, sb):
    """是否击中
    ball_rect = pygame.Rect(ball.ball_x - ball.ball_r, ball.ball_y - ball.ball_r,
                            2 * ball.ball_r, 2 * ball.ball_r)
    rect_rect = pygame.Rect(rect.rect_x,
                            rect.rect_y,
                            rect.pong_settings.rect_width,
                            rect.pong_settings.rect_height)
    if pygame.Rect.colliderect(ball_rect, rect_rect):
        ball.ball_ysgn *= -1
        ball.xsgn_random()
    """
    if ((rect.rect_y - ball.ball_y) < ball.ball_r and
    rect.rect_x < ball.ball_x < (rect.rect_x + rect.pong_settings.rect_width)):
        stats.score += 1
        ball.scale += 1
        ball.ball_ysgn *= -1
        ball.xsgn_random()
        sb.prep_score()
        
def update_screen(screen, pong_settings, ball, rect, sb, stats, play_button):
    """更新屏幕图像，并切换到新屏幕"""
    screen.fill(pong_settings.bg_color)
    ball.draw_ball()
    rect.draw_rect()
    sb.show_sb()
    
    if not stats.game_active:
        play_button.draw_button()
    
    # 让最近绘制的屏幕可见
    pygame.display.flip()
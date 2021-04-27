import pygame.font

class Scoreboard():
    """score"""
    
    def __init__(self, screen, pong_settings, stats):
        """"初始化显示得分涉及的信息"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.pong_settings = pong_settings
        self.stats = stats
        
        # 显示得分信息时使用的字体设置
        self.text_color = 'blue'
        self.font = pygame.font.SysFont(None, 40)
        
        # 准备初始得分图像
        self.prep_score()
        # 准备生命图像
        self.prep_left()
        
    def prep_score(self):
        """将得分转化为一副渲染的图像"""
        score_str = 'Score:' + str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color,
            self.pong_settings.bg_color)
        
        # 将得分放在屏幕右上角
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
    
    def prep_left(self):
        """将生命转化为一副渲染的图像"""
        left_str = 'Lives:' + str(self.stats.left)
        self.left_image = self.font.render(left_str, True, self.text_color,
            self.pong_settings.bg_color)
        
        # 将生命放在屏幕左上角
        self.left_rect = self.left_image.get_rect()
        self.left_rect.left = 20
        self.left_rect.top = 20
        
    def show_sb(self):
        """在屏幕上显示得分"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.left_image, self.left_rect)
        
        
        
class Settings():
    """Pong Settings"""
    
    def __init__(self):
        """初始化"""
        # 屏幕设置
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = 'white'
        
        # 球的静态设置
        self.ball_r = 7
        self.ball_color = 'red'
        self.ball_xinc = 0.05
        self.ball_yinc= 0.05
        
        # 挡板设置
        self.rect_width = 120
        self.rect_height = 10
        self.rect_color = 'black'
        self.rect_xinc = 1
        self.rect_yinc = 1
        
        # 加速度设置
        self.scale = 1
        
        # 生命设置
        self.left = 3
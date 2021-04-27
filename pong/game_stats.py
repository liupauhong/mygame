class GameStats():
    """跟踪游戏的统计信息"""
    
    def __init__(self, pong_settings):
        """初始化统计信息"""
        self.game_active = False
        self.pong_settings = pong_settings
        self.reset_stats()
        
    def reset_stats(self):
        """初始化在游戏期间可能变化的统计信息"""
        self.left = self.pong_settings.left
        self.score = 0

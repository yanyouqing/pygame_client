# coding:utf-8
import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    # 初始化游戏，并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    # 创建一个窗口
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    # 设置窗口标题
    pygame.display.set_caption("Alien Invasion")
    # 创建一艘飞船
    ship = Ship(screen)

    # 开始游戏的主循环
    while True:
        # 监控退出事件
        gf.check_events()
        gf.update_scree(ai_settings, screen, ship)


# 运行主程序
run_game()

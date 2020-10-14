# coding:utf-8
import sys
import pygame


def check_events():
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def update_scree(ai_settings, screen, ship):
    # 给窗口设置背景颜色
    screen.fill(ai_settings.bg_color)
    # 将飞船显示在窗口中
    ship.blitme()
    # 让最近绘制的屏幕可见
    pygame.display.flip()

# coding:utf-8
from sys import exit
import pygame
from pygame.locals import *

# 指定图像文件名称
background_image_filename = 'images/sushiplate.jpg'
mouse_image_filename = 'images/fugu.png'

# 初始化pygame
pygame.init()
# 创建一个窗口
screen = pygame.display.set_mode((640, 480), 0, 32)
# 设置窗口标题
pygame.display.set_caption('Hello,World')
background = pygame.image.load(background_image_filename).convert()
mouse_cursor = pygame.image.load(mouse_image_filename).convert_alpha()

# 游戏主循化123
while True:
    for event in pygame.event.get():
        # 接收到退出事件后，退出程序
        if event.type == QUIT:
            exit()
        # 将背景图画上去
        screen.blit(background, (0, 0))
        # 获取鼠标的坐标
        x, y = pygame.mouse.get_pos()
        # print(x, y)
        # 计算光标的左上角位置
        x -= mouse_cursor.get_width() / 2
        y -= mouse_cursor.get_height() / 2
        screen.blit(mouse_cursor, (x, y))
        # 把光标画上去
        pygame.display.flip()
        # 刷新画面
        pygame.display.update()

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
pygame.display.set_caption('hello world')
# 游戏主循化
while True:
    for event in pygame.event.get():
        # 接收到退出事件后，退出程序
        if event.type == QUIT:
            exit()
        screen.blit()
        pygame.display.flip()


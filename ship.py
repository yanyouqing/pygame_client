# coding:utf-8
import pygame


class Ship():
    def __init__(self, screen):
        # 初始化飞船，并设置其起始位置
        self.screen = screen
        # 加载飞船图片，并获取其外接矩形
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # 将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        # 在指定位置绘制飞船
        self.screen.blit(self.image, self.rect)


if __name__ == '__main__':
    pic = pygame.image.load('images/ship.png')
    rect = pic.get_rect()
    a = rect.centerx
    b = rect.bottom
    print(rect)
    print(a, b)

#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time : 2020/04/24 20:57
# @Email : lukeqinlu@yeah.net
# @Author : Luke
# @File : Pygame.py
# @notice ：


import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode(800, 600)
    pygame.display.set_caption('大球吃小球')
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


if __name__ == '__main__':
    main()



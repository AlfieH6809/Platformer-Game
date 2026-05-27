# Pygame Init + Import

import pygame, sys

pygame.init()
screen = pygame.display.set_mode((1080, 960))

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT: #user closes Pygame
            sys.exit()



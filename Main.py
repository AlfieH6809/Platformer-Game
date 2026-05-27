# Pygame Init + Import

import pygame, sys

pygame.init()
screen = pygame.display.set_mode((1080, 960))
pygame.display.set_caption("Programming Assignment") # Window Title

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT: #user closes Pygame
            sys.exit()


# Variables (Screen Width + Height saved as variables so that can be referenced)

Game_Width = 1080 #Width of Screen
Game_Height = 960

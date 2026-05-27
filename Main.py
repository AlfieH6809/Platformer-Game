# Pygame Init + Import

import pygame, sys

pygame.init()

game_width = 1080
game_height = 960

screen = pygame.display.set_mode((game_width, game_height))
pygame.display.set_caption("Programming Assignment") # Window Title

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT: #user closes Pygame
            sys.exit()







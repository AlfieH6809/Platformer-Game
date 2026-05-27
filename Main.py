# pygame Init + Import

import pygame, sys

# Variables for Screen Height + Width
game_width = 1080 #Screen Width
game_height = 960 # Screen Height

pygame.init()
screen = pygame.display.set_mode((game_width, game_height))
pygame.display.set_caption("Programming Assignment") # Window Title
clock = pygame.time.Clock() # Frame Rate

#left (x), top(y), width, height
player = pygame.Rect(150, 150, 50, 50)

def draw():
    screen.fill("Blue")
    pygame.draw.rect(screen,(2, 239, 238), player)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #user closes Pygame
            pygame.quit()
            sys.exit()

        draw()
        pygame.display.update()
        clock.tick(60) #Run the game at 60FPS - Updates the screen at a rate of 60 frames per second








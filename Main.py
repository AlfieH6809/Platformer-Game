# pygame Init + Import

import pygame, sys

# Variables for Screen Height + Width
game_width = 512 #Screen Width
game_height = 512 # Screen Height

# Images
background_image = pygame.image.load("Assets/Background Images/parallax-mountain-bg.png")
background_image2 = pygame.image.load("Assets/Background Images/parallax-mountain-montain-far.png")
background_image3 = pygame.image.load("Assets/Background Images/parallax-mountain-mountains.png")
background_image4 = pygame.image.load("Assets/Background Images/parallax-mountain-foreground-trees.png")
background_image5 = pygame.image.load("Assets/Background Images/parallax-mountain-trees.png")
player_image = pygame.image.load("Assets/")

pygame.init()
screen = pygame.display.set_mode((game_width, game_height))
pygame.display.set_caption("Programming Assignment") # Window Title
clock = pygame.time.Clock() # Frame Rate

#left (x), top(y), width, height
player = pygame.Rect(150, 150, 50, 50)

def draw():
    screen.fill("Blue")
    screen.blit(background_image, (0, 0))
    pygame.draw.rect(screen,(2, 239, 238), player)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #user closes pygame
            pygame.quit()
            sys.exit()

    #KEYDOWN = Key pressed, KeyUP = Key pressed or released
    # if event.type == pygame.KEYDOWN:
    #     if event.key in (pygame.K_UP, event.key == pygame.K_w): #Moving Up with Up Arrow or W
    #         player.y -= 5
    #     if event.key in (pygame.K_DOWN, event.key == pygame.K_s): #Moving Up with Down Arrow or S
    #         player.y += 5
    #     if event.key in (pygame.K_RIGHT, event.key == pygame.K_d): #Moving Up with Right Arrow or D
    #         player.x += 5
    #     if event.key in (pygame.K_LEFT, event.key == pygame.K_a): #Moving Up with Left Arrow or a
    #         player.x -= 5

    keys = pygame.key.get_pressed() # Movement - Moving Up, Down, Left and Right
    if keys[pygame.K_UP or pygame.K_w]:
        player.y -= 5
    if keys[pygame.K_DOWN or pygame.K_s]:
        player.y += 5
    if keys[pygame.K_RIGHT or pygame.K_d]:
        player.x += 5
    if keys[pygame.K_LEFT or pygame.K_a]:
        player.x -= 5


    draw()
    pygame.display.update()
    clock.tick(60) #Run the game at 60FPS - Updates the screen at a rate of 60 frames per second








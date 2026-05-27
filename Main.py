# pygame Init + Import

import pygame, sys

# Variables - Screen Width/Height, Player Variables
game_width = 640 #Screen Width
game_height = 360 # Screen Height
BG_Width = game_width
BG_Height = game_height
Player_X = game_width / 2
Player_Y = game_height / 2
Player_Width = 42
Player_Height = 48


# Image Assets
background_image = pygame.image.load("Assets/Background Images/parallax-mountain-bg.png")
background_image = pygame.transform.scale(background_image, (BG_Width, BG_Height)) #Adjusting BG Size
background_image2 = pygame.image.load("Assets/Background Images/parallax-mountain-montain-far.png")
background_image2 = pygame.transform.scale(background_image2, (BG_Width, BG_Height)) #Adjusting BG Size
background_image3 = pygame.image.load("Assets/Background Images/parallax-mountain-mountains.png")
background_image3 = pygame.transform.scale(background_image3, (BG_Width, BG_Height)) #Adjusting BG Size
background_image4 = pygame.image.load("Assets/Background Images/parallax-mountain-foreground-trees.png")
background_image4 = pygame.transform.scale(background_image4, (BG_Width, BG_Height)) #Adjusting BG Size
background_image5 = pygame.image.load("Assets/Background Images/parallax-mountain-trees.png")
background_image5 = pygame.transform.scale(background_image5, (BG_Width, BG_Height)) #Adjusting BG Size
player_image = pygame.image.load("Assets/Character Sprite/Magier.png")
player_image = pygame.transform.scale(player_image, (Player_Width, Player_Height)) # Adjusting Size



pygame.init()
screen = pygame.display.set_mode((game_width, game_height))
pygame.display.set_caption("Programming Assignment") # Window Title
pygame.display.set_icon(player_image)
clock = pygame.time.Clock() # Frame Rate

class Player(pygame.Rect):
    def __init__(self):
        pygame.rect.__init__(self)
        self.image = player_image


#left (x), top(y), width, height
player = pygame.Rect(150, 150, 50, 50)

def draw():
    # screen.fill("Blue")
    screen.blit(background_image, (0, 0))
    screen.blit(background_image2, (0, 0))
    screen.blit(background_image3, (0, 0))
    screen.blit(background_image4, (0, 0))
    screen.blit(background_image5, (0, 0))
    screen.blit(player_image, (player.x, player.y))

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








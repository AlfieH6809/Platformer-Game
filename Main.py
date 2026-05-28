# pygame Init + Import

import pygame, sys, random

# Variables - Screen Width/Height, Player Variables
game_width = 640 #Screen Width
game_height = 360 # Screen Height
BG_Width = game_width
BG_Height = game_height
player_X = game_width / 2
player_Y = game_height / 2
player_width = 42
player_height = 48
Player_Speed = 5

# Enemy Variables
GHOST_WIDTH = 36
GHOST_HEIGHT = 30
GHOST_SPEED = 5
GhostX = random.randint(64, 576)
GhostY = random.randint(64, 296)
change_in_x_position_enemy = 0.4


# Load Background Assets
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
#Load Player Image
player_image = pygame.image.load("Assets/Character Sprite/Magier.png")
player_image = pygame.transform.scale(player_image, (player_width, player_height)) # Adjusting Size
# Load Ghost/Enemy Image
ghost_image = pygame.image.load("Assets//Enemy Sprites/ghost.png")
ghost_image = pygame.transform.scale(ghost_image, (GHOST_WIDTH, GHOST_HEIGHT))


pygame.init()
screen = pygame.display.set_mode((game_width, game_height))
pygame.display.set_caption("Programming Assignment") # Window Title
pygame.display.set_icon(player_image)
clock = pygame.time.Clock() # Frame Rate

# Load BGM
pygame.mixer.music.load('Assets/Sounds/BGM2.mp3')
pygame.mixer.music.play(-1, 0.0) # Loop Permanently, Start Track from Beginning
pygame.mixer.music.set_volume(0.2) # Set to an Appropriate Volume

class Player(pygame.Rect):
    def __init(self):
        pygame.Rect.__init__(self, player_X, player_Y, player_width, player_height)
        self.image = player_image


player = Player()






def draw():
    # screen.fill("Blue")
    screen.blit(background_image, (0, 0))
    screen.blit(background_image2, (0, 0))
    screen.blit(background_image3, (0, 0))
    screen.blit(background_image4, (0, 0))
    screen.blit(background_image5, (0, 0))
    screen.blit(player_image, player)
    screen.blit(ghost_image, (GhostX, GhostY))

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

    keys = pygame.key.get_pressed() # Player Movement Inputs + Game Screen Boundaries
    if keys[pygame.K_UP or pygame.K_w]:
        player.y = max(player.y - Player_Speed, 0)
    if keys[pygame.K_DOWN or pygame.K_s]:
        player.y = min(player.y + Player_Speed, game_height - player_height)
    if keys[pygame.K_RIGHT or pygame.K_d]:
        player.x = min(player.x + Player_Speed, game_width - player_width)
    if keys[pygame.K_LEFT or pygame.K_a]:
        player.x = max(player.x - Player_Speed, 0)

# Enemy/Ghost Movement
    GhostX += change_in_x_position_enemy

    # Boundary for Ghosts
    if GhostX <= 0:
        change_in_x_position_enemy = 0.4
        GhostY += random.randint(0, 68)
    elif GhostX >= 576:
        change_in_x_position_enemy = -0.4



    draw()
    pygame.display.update()
    clock.tick(60) #Run the game at 60FPS - Updates the screen at a rate of 60 frames per second








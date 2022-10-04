import pygame
pygame.init()

screen = pygame.display.set_mode((800,600))
#title
pygame.display.set_caption("Gamer")
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)
#Player
playerimg = pygame.image.load("man.png")
background = pygame.image.load("bg.png")
playerx = 200
playery = 50
keys = pygame.key.get_pressed()
def player():
    screen.blit(playerimg, (playerx, playery))
    pass
def dpressed():
    if keys[pygame.K_d]:
        global playerx
        playerx = playerx + 50
        pygame.display.update()
        if playerx == 550:
            playerx = -550

game = True
while game:
    screen.fill(( 0, 50, 0))
    player()
    pygame.display.update()
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

        dpressed()
        if keys[pygame.K_a]:
                playerx = playerx - 50
                pygame.display.update()
                if playerx == -550:
                    playerx = 550



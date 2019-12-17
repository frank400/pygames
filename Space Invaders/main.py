import  pygame
import random
#initialize pygame
pygame.init()

#create screen
screen=pygame.display.set_mode((800 , 600))

#Title andd tools
pygame.display.set_caption("space invaders")
icon=pygame.image.load("space-invaders.png")
pygame.display.set_icon(icon)

#player
player_img = pygame.image.load("space ship.png")
player_X = 370
player_Y = 480
player_X_changer=0

#enemy
enemyIMG=pygame.image.load("blue.png")
enemy_X=384
enemy_Y=10


def player(x,y):
    screen.blit(player_img, (x, y))

def enemy(x,y):
    screen.blit(enemyIMG, (x, y))



#game loop

running=True
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            running= False
        if event.type ==pygame.KEYDOWN:
            if event.key ==pygame.K_a:
                player_X_changer=-1.5
            if event.key == pygame.K_d:
                player_X_changer=1.5
        if event.type == pygame.KEYUP:
            if event.key ==pygame.K_a or event.key == pygame.K_d:
                player_X_changer=0


    player_X += player_X_changer
    if player_X <0:
        player_X=0
    elif player_X>740:
        player_X=740
    player(player_X,player_Y)
    enemy(enemy_X,enemy_Y)

    pygame.display.update()

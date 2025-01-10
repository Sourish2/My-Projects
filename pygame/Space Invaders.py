import math
import random
import pygame
from pygame import mixer

# initialize pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# caption and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('space-ship.png')
pygame.display.set_icon(icon)

# Background
background = pygame.image.load('background.png')

# player
playerimg = pygame.image.load('space-invaders (2).png')
playerX = 370
playerY = 480
playerX_change = 0

# enemy
enemyimg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyimg.append(pygame.image.load('alien.png'))
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(5)
    enemyY_change.append(40)


# bullet
bulletimg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletY_change = 10
# Ready- You can't see the bullet on the screen
# Fire- The Bullet in currently moving
bullet_state = 'ready'

#score
score_value=0
font= pygame.font.Font('freesansbold.ttf',32)
textX=10
textY=10

#game over font
over_font=pygame.font.Font('freesansbold.ttf',64)

def show_score(x,y):
    score = font.render('Score :' + str(score_value), True, (255,255,255))
    screen.blit(score,(x,y))

def game_over_text(x,y):
    over_text = over_font.render('GAME OVER',True,(255,255,255))
    screen.blit(over_text, (x, y))

def player(x, y):
    screen.blit(playerimg, (x, y))


def enemy(x, y):
    global num_of_enemies
    for i in range(num_of_enemies):
        screen.blit(enemyimg[i], (x[i], y[i]))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bulletimg, (x + 16, y + 20))


def iscollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow((enemyX - bulletX), 2) + math.pow((enemyY - bulletY), 2))
    if distance < 27:
        return True
    else:
        return False


# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # if keystroke is pressed check whether is right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -8
            elif event.key == pygame.K_RIGHT:
                playerX_change = 8
            if event.key == pygame.K_SPACE:
                if bullet_state == 'ready':
                    bullet_sound=mixer.Sound('laser.wav')
                    bullet_sound.play()
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                playerX_change = 0

    playerX += playerX_change
    for i in range(num_of_enemies):
        enemyX[i] += enemyX_change[i]

    # RGB(RGD Green BLue)
    screen.fill((255, 215, 0))
    # Background image
    screen.blit(background, (0, 0))
    player(playerX, playerY)
    enemy(enemyX, enemyY)
    show_score(textX,textY)
    if playerX > 736:
        playerX = 736
    elif playerX <= 0:
        playerX = 0
    #enemy movement
    for i in range(num_of_enemies):

        #Game Over
        if enemyY[i] >440:
            game_over_text(200,250)
            for j in range(num_of_enemies):
                enemyY[j]=2000
            break

        if enemyX[i] > 736:
            enemyX_change[i] = -5
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] <= 0:
            enemyX_change[i] = 5
            enemyY[i] += enemyY_change[i]
         # collision
        collision = iscollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
             bullet_state = 'ready'
             collision_sound=mixer.Sound('explosion.wav')
             collision_sound.play()
             bulletY = 480
             score_value += 1
             enemyX[i] = random.randint(0, 735)
             enemyY[i] = random.randint(50, 150)
    # bullet movement
    if bullet_state == "fire":
        bulletY -= bulletY_change
        fire_bullet(bulletX, bulletY)
    if bulletY <= 0:
        bulletY = 480
        bullet_state = 'ready'
    pygame.display.update()
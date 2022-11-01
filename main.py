# Brick Breaker Game

import pygame
import random
from pygame import mixer

# Initialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# background
background = pygame.image.load("assets/images/realBackground.png")

# Title and Icon
pygame.display.set_caption("Brick Breaker")
icon = pygame.image.load("assets/images/Brick Breaker Icon.png")
pygame.display.set_icon(icon)

# Paddle
paddleImage = pygame.image.load("assets/images/scaledPaddle.png")
paddleX = 335
paddleY = 550
paddleX_change = 0

# BrickCoordinates
brickX = []
brickY = []
brickX_change = []
brickY_change = []
numOfBricks = 600
numOfRows = 100

#Bricks
yellowBrickImage = pygame.image.load("assets/images/yellowBrick.png")
greenBrickImage = pygame.image.load("assets/images/greenBrick.png")
blueBrickImage = pygame.image.load("assets/images/blueBrick.png")
pinkBrickImage = pygame.image.load("assets/images/pinkBrick.png")

# ball
ballImage = pygame.image.load("assets/images/Ball.png")
ballX = 380
ballY = 280
ballX_change = 2.5
ballY_change = 2.5

#Score
scoreValue = 0
font = pygame.font.Font("assets/fonts/Neufreit-ExtraBold.otf",24)
textX = 10
textY = 10

#Game Over Sound
playGameOverSound = True
gameOverSound = mixer.Sound("assets/sounds/gameOverSoundEffect.wav")

def showScore(x,y):
    score = font.render("Score : " + str(scoreValue), True, (255,255,255))
    screen.blit(score,(x,y))

def gameOverText():
    # Game Over Text
    gameOverFont = pygame.font.Font("assets/fonts/Neufreit-ExtraBold.otf", 64)
    gameOverFont = gameOverFont.render("GAME OVER!", True, (255, 255, 255))
    screen.blit(gameOverFont, (200, 250))
    # Final Score Text
    finalScoreFont = pygame.font.Font("assets/fonts/Neufreit-ExtraBold.otf", 32)
    finalScoreFont = finalScoreFont.render("Final Score: " + str(scoreValue), True, (255, 255, 255))
    screen.blit(finalScoreFont, (300, 325))

def paddle(x, y):
    screen.blit(paddleImage, (x, y))

def yellowBrick(x, y, i):
    screen.blit(yellowBrickImage, (x, y))

def greenBrick(x, y, i):
    screen.blit(greenBrickImage, (x, y))

def blueBrick(x, y, i):
    screen.blit(blueBrickImage, (x, y))

def pinkBrick(x, y, i):
    screen.blit(pinkBrickImage, (x, y))

def ball(x, y):
    screen.blit(ballImage, (x, y))

#To pick random brick colours
colourOfBrick = []
for i in range(numOfBricks):
    colourOfBrick.append(random.randint(1,4))

brickXValue = 15
brickYValue = 0

for i in range(numOfRows):

    for j in range(numOfBricks):

        brickX.append(brickXValue)
        brickY.append(brickYValue)
        brickXValue += 130
        brickX_change.append(0.1)
        brickY_change.append(0.1)
        if len(brickX)%6 == 0:
            brickXValue = 15
        if len(brickY)%6 == 0:
            brickYValue -= 50  # row height


# Game Loop (makes sure game is always running)
running = True

while running:
    # background image
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # If keystroke is pressed check whether left or right
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                paddleX_change = -7
            if event.key == pygame.K_RIGHT:
                paddleX_change = 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                paddleX_change = 0

    # Checking boudries of paddle
    paddleX += paddleX_change

    if paddleX <= 0:
        paddleX = 0
    elif paddleX >= 669:
        paddleX = 669

    #Draw Rectangles around bricks
    brickRect = []
    for i in range(numOfBricks):
        brickRect.append(pygame.draw.rect(screen, (0, 0, 0), (brickX[i], brickY[i], 120, 42),1))

    for i in range(numOfBricks):
        #Game Over
        if brickY[i] >= 512:
            for j in range(numOfBricks):
                if playGameOverSound == True:
                    gameOverSound.play()
                brickX[j] = -2000
                ballX_change = 0
                ballY_change = 0
                playGameOverSound = False
            gameOverText()
        # Brick Movement
        brickY[i] += brickY_change[i]
        if brickY[i] <= 0:
            brickY_change[i] = 0.1
        # Makes brick show up on screen
        if colourOfBrick[i] == 1:
            yellowBrick(brickX[i], brickY[i], i)
        elif colourOfBrick[i] == 2:
            greenBrick(brickX[i], brickY[i], i)
        elif colourOfBrick[i] == 3:
            blueBrick(brickX[i], brickY[i], i)
        elif colourOfBrick[i] == 4:
            pinkBrick(brickX[i], brickY[i], i)


    # Ball Movement and boundary checking
    ballX += ballX_change

    if ballX <= 0:
        ballX_change *= -1
    elif ballX >= 760:
        ballX_change *= -1

    ballY += ballY_change

    if ballY <= 0:
        ballY_change *= -1
    elif ballY >= 560:
        ballX = 380
        ballY = 280
        scoreValue -= 3


    # Paddle and Ball Collision
    if ballY > 530 and ballY < 535 and (ballX+20) < paddleX + 131 and (ballX+20) > paddleX:
        paddleSound = mixer.Sound("assets/sounds/hitPaddleSoundEffect.wav")
        paddleSound.play()
        ballY_change *= -1

    paddle(paddleX, paddleY)
    ballCircle = pygame.draw.circle(screen, (0,0,0), (int(ballX+20),int(ballY+20)) ,20)
    ball(ballX, ballY)

    #Ball and Brick Collision
    for i in range (numOfBricks):
        if ballCircle.colliderect(brickRect[i]):
            if abs(ballCircle.top - brickRect[i].bottom < 10) and ballY_change < 0:
                brickSound = mixer.Sound("assets/sounds/hitBrickSoundEffect.wav")
                brickSound.play()
                brickX[i] = -600
                brickY[i] = -6000
                ballY_change *= -1
                scoreValue += 1

    showScore(textX,textY)
    pygame.display.update()

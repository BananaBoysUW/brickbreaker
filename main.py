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

#Brick Coordinates with Structure
# brickCoordinates = [[[30,30],[30,50],[50,80],[80,30]],
#                     [[50,100],[100,40],[40,65]],
#                     [[100,200],[200,80],[350,100]]]


# IN THE FINAL VERSION THIS ARRAY WILL BE GIVEN BY THE IMAGE ALGORITHM
# brickCoordinates = [[[200,200],[200,400],[250,400],[350,325],[450,400],[500,400],[500,200],[450,200],[450,325],[350,275],[250,325],[250,200]]]
brickCoordinates = [[[200,100],[200,200],[400,200],[400,100]],[[600,200],[700,200],[650,300]],[[250,250],[400,250],[450,350],[300,350]]]

print(brickCoordinates[0][0][0])
brickMasks = []

#To see how many times to iterate each loop

def getSizeOfNestedList(listOfElem):
    #Number of shapes
    count = 0
    # Iterate over the list
    for elem in brickCoordinates:
        # Check if type of element is list
        if type(elem) == list:  
            # Again call this function to get the size of this element
            count += getSizeOfNestedList(elem)
        else:
            count += 1    
    return count

length = len(brickCoordinates)
print('Number of shapes = ', length)


count = 0
for listElem in brickCoordinates:
    count += len(listElem)                    
print('Total Number of points in each shape : ', count)

count = count/len(brickCoordinates)
count = count - 1
points = int(count)


brickCoorX = []
brickCoorY = []

# How many shapes there are
for i in range(len(brickCoordinates)):
    for j in range(points + 1):  
        brickCoorX.append(brickCoordinates[i][j][0])
        brickCoorY.append(brickCoordinates[i][j][1])


print(*brickCoorX, sep = ", ")
print(*brickCoorY, sep = ", ")






# BrickCoordinates
# brickX = []
# brickY = []

brickX_change = []
brickY_change = []
numOfBricks = len(brickCoordinates)
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
ballX_change = 0.25
ballY_change = 0.25

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

# def yellowBrick(x, y, i):
#     screen.blit(yellowBrickImage, (x, y))

# def greenBrick(x, y, i):
#     screen.blit(greenBrickImage, (x, y))

# def blueBrick(x, y, i):
#     screen.blit(blueBrickImage, (x, y))

# def pinkBrick(x, y, i):
#     screen.blit(pinkBrickImage, (x, y))

def ball(x, y):
    screen.blit(ballImage, (x, y))

# #To pick random brick colours
colourOfBrick = []
for i in range(numOfBricks):
    colourOfBrick.append(random.randint(1,4))

brickXValue = 15
brickYValue = 0

# for i in range(numOfRows):

#     for j in range(numOfBricks):

#         brickX.append(brickXValue)
#         brickY.append(brickYValue)
#         brickXValue += 130
#         brickX_change.append(0.01)
#         brickY_change.append(0.01)
#         if len(brickX)%6 == 0:
#             brickXValue = 15
#         if len(brickY)%6 == 0:
#             brickYValue -= 50  # row height


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
                paddleX_change = -2
            if event.key == pygame.K_RIGHT:
                paddleX_change = 2
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                paddleX_change = 0

    # Checking boundaries of paddle
    paddleX += paddleX_change

    if paddleX <= 0:
        paddleX = 0
    elif paddleX >= 669:
        paddleX = 669

    #Draw Rectangles around bricks
    # brickRect = []
    brickPolygon = []
    for i in range(len(brickCoordinates)):
        # brickPolygon.append(pygame.draw.polygon(screen, (0, 0, 0), ((brickCoorX[i], brickCoorY[i]), (brickCoorX[i+1],brickCoorY[i+1]), (brickCoorX[i+2], brickCoorY[i+2]))))
        
        brickPolygon.append(pygame.draw.polygon(screen, (0, 0, 0), brickCoordinates[i]))
        # brickMasks.append(pygame.mask.Mask(brickCoorX[i],brickCoorY[i]))
        
    # #TESTING DRAWING POLYGONS
    # brickRect = []
    # for i in range(numOfBricks):
    #     brickRect.append(pygame.draw.polygon(screen, (0, 0, 0), ([brickCoordinates[0],brickCoordinates[1]]),1))



    for i in range(len(brickCoordinates)):
        #Game Over
        if brickCoorY[i] >= 512:
            for j in range(len(brickCoordinates)):
                if playGameOverSound == True:
                    gameOverSound.play()
                brickCoorX[j] = -2000
                ballX_change = 0
                ballY_change = 0
                playGameOverSound = False
            gameOverText()
        # # Brick Movement
        # brickCoorY[i] += brickY_change[i]
        # if brickCoorY[i] <= 0:
        #     brickY_change[i] = 0.01
        # Makes brick show up on screen
        # if colourOfBrick[i] == 1:
        #     yellowBrick(brickCoorX[i], brickCoorY[i], i)
        # elif colourOfBrick[i] == 2:
        #     greenBrick(brickCoorX[i], brickCoorY[i], i)
        # elif colourOfBrick[i] == 3:
        #     blueBrick(brickCoorX[i], brickCoorY[i], i)
        # elif colourOfBrick[i] == 4:
        #     pinkBrick(brickCoorX[i], brickCoorY[i], i)


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
    if ballY > 530 and ballY < 535 and (ballX+20) < paddleX + 138 and (ballX+20) > paddleX:
        paddleSound = mixer.Sound("assets/sounds/hitPaddleSoundEffect.wav")
        paddleSound.play()
        ballY_change *= -1

    paddle(paddleX, paddleY)
    ball(ballX, ballY)
    
    
    
    ballCircle = pygame.draw.circle(screen, (0,0,0), (int(ballX+20),int(ballY+20)) ,20)
    ballMask = pygame.mask.from_surface(screen)

    # # collision detection with masks
    # for i in range (brickMasks):
    #     result = ballMask.overlap(brickMasks[i])
    #     if result:
    #         brickMasks.pop(brickMasks[i]) 




    

    # #Ball and Brick Collision
    # for i in range (len(brickCoordinates)):
    #     if ballCircle.colliderect(brickPolygon[i]):
    #         if abs(ballCircle.top - brickPolygon[i].bottom < 10) and ballY_change < 0:
    #             brickSound = mixer.Sound("assets/sounds/hitBrickSoundEffect.wav")
    #             brickSound.play()
    #             brickCoorX[i] = -600
    #             brickCoorY[i] = -6000
    #             ballY_change *= -1
    #             scoreValue += 1

    showScore(textX,textY)
    pygame.display.update()

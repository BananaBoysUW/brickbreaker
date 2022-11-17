# import pygame
# import random

# # --- classes ---

# class Brick():

#     def __init__(self, x, y, image):
#         self.image = image
#         self.rect = self.image.get_rect(x=x, y=y)
#         self.x = x
#         self.y = y
#         self.x_change = 0
#         self.y_change = 1

#     def draw(self, screen):
#         self.rect.x = int(self.x)
#         self.rect.y = int(self.y)
#         screen.blit(self.image, self.rect)
#         pygame.draw.rect(screen, (0, 0, 0), self.rect, 1)

#     def update(self):
#         self.y += self.y_change
#         self.rect.y = int(self.y)

#         if self.rect.y <= 0:
#             self.y_change = 1
#         elif self.rect.y >= 500:
#             self.y_change = -1

# class Ball():

#     def __init__(self):
#         #self.image = pygame.image.load("Ball.png")

#         self.image = pygame.Surface((16, 16)).convert_alpha()
#         self.image.fill((0,0,0,0)) # transparent background
#         pygame.draw.circle(self.image, (255,255,255), (8, 8), 8)

#         self.rect = self.image.get_rect(centerx=380, centery=280)
#         self.x = 380
#         self.y = 280
#         self.x_change = 3
#         self.y_change = 3

#     def reset(self):
#         self.x = 380
#         self.y = 280

#     def draw(self, screen):
#         self.rect.centerx = int(self.x)
#         self.rect.centery = int(self.y)
#         screen.blit(self.image, self.rect)

#     def update(self):
#         # Ball Movement and boundary checking
#         self.x += self.x_change
#         self.rect.centerx = int(self.x)

#         if self.rect.left <= 0:
#             self.x_change *= -1
#         elif self.rect.right >= 800:
#             self.x_change *= -1

#         self.y += self.y_change
#         self.rect.centery = int(self.y)

#         if self.rect.top <= 0:
#             self.y_change *= -1
#         elif self.rect.bottom >= 600:
#             self.reset()

# class Paddle():

#     def __init__(self):
#         #self.image = pygame.image.load("scaledPaddle.png")
#         self.image = pygame.Surface((100, 30))
#         self.image.fill((255,0,0))

#         self.rect = self.image.get_rect(x=335, y=550)
#         self.x_change = 0
#         self.y_change = 0

#     def reset(self):
#         self.rect.x = 335
#         self.rect.y = 550

#     def draw(self, screen):
#         screen.blit(self.image, self.rect)

#     def update(self):
#         # Checking boudries of paddle
#         self.rect.x += self.x_change

#         if self.rect.left <= 0:
#             self.rect.left = 0
#         elif self.rect.right >= 800:
#             self.rect.right = 800

# class Score():

#     def __init__(self):
#         #self.font = pygame.font.Font("Neufreit-ExtraBold.otf", 24)
#         self.font = pygame.font.SysFont(None, 24)
#         self.value = 0
#         self.x = 10
#         self.y = 10

#     def reset(self):
#         self.value = 0

#     def draw(self, screen):
#         self.image = self.font.render("Score : " + str(self.value), True, (255,255,255))
#         self.rect = self.image.get_rect(x=self.x, y=self.y)
#         screen.blit(self.image, self.rect)

# # --- functions ---

# # empty

# # --- main ---

# pygame.init()
# screen = pygame.display.set_mode((800, 600))

# pygame.display.set_caption("Brick Breaker")
# #icon = pygame.image.load("Brick Breaker Icon.png")
# #pygame.display.set_icon(icon)

# # Background Image

# #background_image = pygame.image.load("realBackground.png")

# background_image = pygame.Surface((800,600))
# for y in range(5, 600, 25):
#     for x in range(5, 800, 25):
#         color = random.choice([(255,128,128), (128,255,128), (128,128,255)])
#         background_image.fill(color, [x,y,15,15])

# # Brick Images

# #brick_images = [
# #    pygame.image.load("yellowBrick.png"),
# #    pygame.image.load("greenBrick.png"),
# #    pygame.image.load("blueBrick.png"),
# #    pygame.image.load("pinkBrick.png"),
# #]

# brick_images = [
#     pygame.Surface((100, 30)),
#     pygame.Surface((100, 30)),
#     pygame.Surface((100, 30)),
#     pygame.Surface((100, 30)),
#     pygame.Surface((100, 30)),
#     pygame.Surface((100, 30)),
# ]    

# brick_images[0].fill((255,0,0))
# brick_images[1].fill((0,255,0))
# brick_images[2].fill((0,0,255))
# brick_images[3].fill((255,255,0))
# brick_images[4].fill((255,0,255))
# brick_images[5].fill((0,255,255))

# # Objects

# paddle = Paddle()
# ball   = Ball()
# score  = Score()

# # bricks
# rows_number = 5
# cols_number = 7

# all_bricks = []

# y = 0
# for row in range(rows_number):
#     x = 50
#     for col in range(cols_number):
#         color_image = random.choice(brick_images)
#         brick = Brick(x, y, color_image)
#         all_bricks.append(brick)
#         x += 100
#     y += 30

# # Game Loop

# clock = pygame.time.Clock()
# running = True

# while running:

#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#         # If keystroke is pressed check whether left or right
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_LEFT:
#                 paddle.x_change = -5
#             if event.key == pygame.K_RIGHT:
#                 paddle.x_change = 5
#         if event.type == pygame.KEYUP:
#             if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
#                 paddle.x_change = 0

#     # --- updates ---

#     paddle.update()
#     ball.update()

#     # Bricks Update
#     for brick in all_bricks:
#         brick.update()

#     # Ball and Paddle Collision
#     if ball.rect.colliderect(paddle):
#         ball.y_change *= -1

#     # Ball and Bricks Collision
#     for brick in all_bricks:
#         if ball.rect.colliderect(brick):
#             brick.x = -400
#             ball.y_change *= -1
#             score.value += 1

#     # --- draws ---

#     # To change background colour
#     # screen.fill((128, 128, 128)) # you don't need it if background fill all screen

#     # background image
#     screen.blit(background_image, (0, 0))

#     for brick in all_bricks:
#         brick.draw(screen)

#     paddle.draw(screen)
#     ball.draw(screen)

#     score.draw(screen)

#     pygame.display.flip()

#     clock.tick(60) # 60 FPS (Frames Per Second) on all computers

# # --- end ---

# pygame.quit() 

import pygame
import sys
import shapelogic

pygame.init()

screensize = width, height = 800, 595

screen = pygame.display.set_mode(screensize)



background_image =pygame.image.load("/Users/marceason/PycharmProjects/Tetris/Wooden_background.jpg").convert_alpha()

myshape = 0
stop_movement = 0
blit_count = 0
stored_shapes = pygame.sprite.Group()
stored_shapes_with_coords = []
extra_blit_required = False


index = 0
count = 0
listofshapes = []

class shapemanager():

    def __init__(self):

        self.listofshapes = []


    def create_another_instance(self):

        global count
        count += 1
        string = "Shape_{0},".format(count)

        another_shape = Shape(string)
        self.listofshapes.append(another_shape)
        global index
        object = self.listofshapes[index]
        index += 1
        return object


def load_shape(self):
    shape = self.create_another_instance()
    shape.load_shapes()







class Shape(pygame.sprite.Sprite):

    def __init__(self, name):
        pygame.sprite.Sprite.__init__(self)

        self.name = name
        self.x = 50
        self.y = 100
        self.move_event = pygame.USEREVENT + 1
        self.reached_bottom_event = pygame.USEREVENT + 2
        self.one_sec_timer = 1000
        self.half_sec_timer = 500

        self.reachbottomflag = False
        self.movement_possible = True

        self.image = pygame.image.load(
    "/Users/marceason/PycharmProjects/Tetris/Tetris_Shapes/Green_Shape_1_Position_1.png")
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()


    def move_shape(self):
        if self.movement_possible:
            key_input = pygame.key.get_pressed()
            if key_input[pygame.K_LEFT]:
                self.x -= 16
            if key_input[pygame.K_RIGHT]:
                self.x += 16
            if not self.reachbottomflag:
                if key_input[pygame.K_DOWN]:
                    self.y += 16


    def reachbottom(self):

        if self.y >= 560:
            self.reachbottomflag = True

    def no_movement_possible(self):

        self.movement_possible = False

def assign_shape():

global myshape
global stop_movement
myshape = sl.create_another_instance()
pygame.time.set_timer(myshape.move_event, myshape.one_sec_timer)
stop_movement = pygame.time.set_timer(myshape.reached_bottom_event, myshape.half_sec_timer)

def blit_used_shapes():

global screen
global blit_count
blit_count = len(stored_shapes_with_coords)
local_count = 0
while local_count < blit_count:
    screen.blit(stored_shapes_with_coords[local_count][0], (stored_shapes_with_coords[local_count][1], stored_shapes_with_coords[local_count][2]))
    local_count += 1


sl = shapemanager()





    ##### HERE IS THE PIXEL DETECTION #####
    result = pygame.sprite.spritecollide(myshape, stored_shapes, False, pygame.sprite.collide_mask)


## Main loop ##

assign_shape()

while True:

for event in pygame.event.get():
    if event.type == pygame.QUIT: sys.exit()
    screen.blit(background_image, (0, 0))
    screen.blit(myshape.image, (myshape.x, myshape.y))
    myshape.move_shape()



    key_input = pygame.key.get_pressed()
    if key_input[pygame.K_SPACE]:
        myshape.rotate_shape()


    myshape.reachbottom()
    if myshape.reachbottomflag:
        if event.type == myshape.reached_bottom_event:
            myshape.no_movement_possible()
            stored_shape_tuple = [myshape.image, myshape.x, myshape.y]
            stored_shapes_with_coords.append(stored_shape_tuple)
            stored_shapes.add(myshape)

            extra_blit_required = True

            assign_shape()
            ####### PIXEL DETECTION IS HERE IN FOR LOOP ####
            if result:
                print("this should only execute when two shapes touch!!")

    if extra_blit_required:
        blit_used_shapes()

    pygame.display.update()
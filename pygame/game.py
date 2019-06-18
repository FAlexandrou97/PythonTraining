import sys
import pygame
pygame.init()

size = width, height = 600, 400
right = [10, 0]
left = [-10, 0]
up = [0, -10]
down = [0, 10]
black = 0, 0, 0
boundaries = yMin, xMin, xMax, yMax = 0, 0, width-40, height-40
screen = pygame.display.set_mode(size)

frogImage = pygame.image.load("pygame/frog.png")
frogImage = pygame.transform.scale(frogImage, (40, 40))
frog = frogImage.get_rect()

while 1:
    #Capture all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            sys.exit()

    #Keyboard Controls
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            print("Going Left")
            #Boundaries
            if(frog.x > xMin):
                frog = frog.move(left)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            print("Going Right")
            if(frog.x < xMax):
                frog = frog.move(right)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            print("Going Up")
            if(frog.y > yMin):
                frog = frog.move(up)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            print("Going Down")
            if(frog.y < yMax):
                frog = frog.move(down)

    # ballrect = ballrect.move(speed)
    # if ballrect.left < 0 or ballrect.right > width:
    #     speed[0] = -speed[0]
    # if ballrect.top < 0 or ballrect.bottom > height:
    #     speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(frogImage, frog)
    pygame.display.flip()
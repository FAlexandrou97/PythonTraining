import sys
import pygame
pygame.init()

#Scene Setup

#Models/Images
size = width, height = 600, 400
black = 0, 0, 0
blue = 0, 0, 255
boundaries = yMin, xMin, xMax, yMax = 0, 0, width-40, height-40
screen = pygame.display.set_mode(size)
roadImage = pygame.image.load("pygame/road.png")
roadImage = pygame.transform.scale(roadImage, (width, height))
road = roadImage.get_rect(x=0, y=0)
#Frog image radius = 40px approx.
frogImage = pygame.image.load("pygame/frog.png")
frogImage = pygame.transform.scale(frogImage, (40, 40))
frog = frogImage.get_rect(x=width/2-20, y=height-40)
frogRadius = 40

#Frog Movement Ratio
right = [frogRadius, 0]
left = [-frogRadius, 0]
up = [0, -frogRadius]
down = [0, frogRadius]




#Main game loop
while 1:
    #Fill screen to "update scene"
    #screen.fill(black)
    screen.blit(roadImage, road)
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

    

    if(frog.colliderect(water)):
        print("collision")
    
    #Update the rest of the images after the background
    water = pygame.draw.rect(screen, blue, (0, 200, width, frogRadius))
    screen.blit(frogImage, frog)
    pygame.display.flip()
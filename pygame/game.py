import sys
import pygame
pygame.init()
pygame.mixer.init()

class Frog:
    screenSize = width, height = 600, 400
    #Class variables
    m_image = pygame.image.load("pygame/frog.png")
    m_Image = pygame.transform.scale(m_image, (40, 40))
    m_frog = m_image.get_rect(x=width/2-20, y=height-40)
    m_Radius = 40

    #Class Methods
    def Movement(self):
        frog = self.m_frog
        boundaries = yMin, xMin, xMax, yMax = 0, 0, width-40, height-40
        right = [self.m_Radius, 0]
        left = [-self.m_Radius, 0]
        up = [0, -self.m_Radius]
        down = [0, self.m_Radius]
        #Keyboard Controls
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            print("Going Left")
            #Boundaries
            if(frog.x > xMin):
                self.m_frog = frog.move(left)               
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            print("Going Right")
            if(frog.x < xMax):
                self.m_frog = frog.move(right)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            print("Going Up")
            if(frog.y > yMin):
                self.m_frog = frog.move(up)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            print("Going Down")
            if(frog.y < yMax):
                self.m_frog = frog.move(down)

         #Constructor
    def __init__(self):
        pass

#Scene Setup

#Colours (RGB)
black = 0, 0, 0
blue = 0, 0, 255

#Models/Images
screenSize = width, height = 600, 400
screen = pygame.display.set_mode(screenSize)
roadImage = pygame.image.load("pygame/road.png")
roadImage = pygame.transform.scale(roadImage, (width, height))
road = roadImage.get_rect(x=0, y=0)

#Music
pygame.mixer.music.load("pygame/music.mp3")
pygame.mixer.music.play()

#Frog Object
objFrog = Frog()

#Main game loop
while 1:
    #Fill screen to "update scene"
    screen.blit(roadImage, road)

    #Update the rest of the images after the background
    water = pygame.draw.rect(screen, blue, (0, 200, width, objFrog.m_Radius))
    screen.blit(objFrog.m_Image, objFrog.m_frog)

    #Capture all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            sys.exit()

        objFrog.Movement()
                
    if(objFrog.m_frog.colliderect(water)):
        print("collision")
    
    pygame.display.update()

import sys
import pygame
import os.path
pygame.init()
pygame.mixer.init()
pygame.font.init()

g_screenSize = width, height = 1024, 600


class Frog:
    # Class variables
    radius = 35
    image = pygame.image.load("pygame/frog.png")
    image = pygame.transform.scale(image, (radius, radius))
    rect = image.get_rect(x=width / 2 - radius, y=height - radius)

    # Class Methods
    def Movement(self, event):
        frog = self.rect
        boundaries = yMin, xMin, xMax, yMax = self.radius, 0, width-self.radius, height-self.radius
        right = [self.radius, 0]
        left = [-self.radius, 0]
        up = [0, -self.radius]
        down = [0, self.radius]
        # Keyboard Controls
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            print("Going Left")
            # Boundaries
            if(frog.x > xMin):
                self.rect = frog.move(left)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            print("Going Right")
            if(frog.x < xMax):
                self.rect = frog.move(right)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            print("Going Up")
            if(frog.y > yMin):
                self.rect = frog.move(up)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            print("Going Down")
            if(frog.y < yMax):
                self.rect = frog.move(down)

    def ResetPosition(self):
        self.rect.x = width / 2 - self.radius
        self.rect.y = height - self.radius

    # Constructor
    def __init__(self):
        pass


class Enemy(pygame.sprite.Sprite):
    '''
    Spawn an enemy
    '''
    radius = 70
    def __init__(self, x, y, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join('pygame/', img))
        self.image = pygame.transform.scale(self.image, (self.radius, self.radius))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def Movement(self, velocity, direction="right"):
        if direction == "right":
            self.rect = self.rect.move(velocity, 0)
        else:
            self.rect = self.rect.move(-velocity, 0)


def exitGame(event):
    if event.type == pygame.QUIT:
        sys.exit()
    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
        sys.exit()


def main():
    # Scene Setup

    # Colours (RGB)
    black = 0, 0, 0
    blue = 0, 0, 255

    # Models/Images
    screen = pygame.display.set_mode(g_screenSize)
    # Road
    roadImage = pygame.image.load("pygame/road.png")
    roadImage = pygame.transform.scale(roadImage, (width, int(height/3)))
    road = roadImage.get_rect(x=0, y=height * 0.542)
    # Water
    waterImage = pygame.image.load("pygame/water.png")
    waterImage = pygame.transform.scale(waterImage, (roadImage.get_width(), roadImage.get_height()))
    water = waterImage.get_rect(x=0, y=height * 0.14)
    # Grass
    grassImage = pygame.image.load("pygame/grass.jpg")
    listGrass = (grassImage.get_rect(x=0, y=height-175),
                grassImage.get_rect(x=200, y=height-175),
                grassImage.get_rect(x=400, y=height-175),
                grassImage.get_rect(x=600, y=height-175),
                grassImage.get_rect(x=800, y=height-175),
                grassImage.get_rect(x=0, y=height* 0.4),
                grassImage.get_rect(x=200, y=height* 0.4),
                grassImage.get_rect(x=400, y=height* 0.4),
                grassImage.get_rect(x=600, y=height* 0.4),
                grassImage.get_rect(x=800, y=height* 0.4))

    # Fonts
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    clock = pygame.time.Clock()

    # Music
    pygame.mixer.music.load("pygame/music.mp3")
    pygame.mixer.music.play()

    # Frog Object
    objFrog = Frog()

    # Enemy Object
        
    objEnemy = Enemy(x=0, y=450, img="enemy.png")
    objEnemy2 = Enemy(x=width, y=350, img="enemy.png")


    # Main game loop
    while 1:
        # Fill screen to "update scene"
        
        # 60fps cap
        textSurface = myfont.render((str(clock.get_fps())), True, black)
        clock.tick(60)

        # Update the rest of the images after the background
        screen.blit(textSurface, (50, 50))  # FPS
        for grass in listGrass:
            screen.blit(grassImage, grass)

        # Update road after grass to "cut" grass image size
        screen.blit(roadImage, road)

        screen.blit(waterImage, water)
        screen.blit(objFrog.image, objFrog.rect)
       
        screen.blit(objEnemy.image, objEnemy.rect)
        screen.blit(objEnemy2.image, objEnemy2.rect)


        # Capture all events
        for event in pygame.event.get():
            exitGame(event)
            objFrog.Movement(event)

        objEnemy.Movement(velocity=2, direction="right")
        objEnemy2.Movement(velocity=1, direction="left")


        # Collisions             
        if objFrog.rect.colliderect(water):
            print("collision")

        if objFrog.rect.colliderect(objEnemy.rect):
            objFrog.ResetPosition()

        pygame.display.update()


if __name__ == "__main__":
    main()

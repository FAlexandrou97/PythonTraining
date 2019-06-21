import sys
import pygame
import os.path
pygame.init()
pygame.mixer.init()
pygame.font.init()

g_screenSize = width, height = 600, 400


class Frog:
    # Class variables
    radius = 30
    image = pygame.image.load("frog.png")
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
    def __init__(self, x, y, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join('', img))
        self.image = pygame.transform.scale(self.image, (60, 60))
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
    roadImage = pygame.image.load("road.png")
    roadImage = pygame.transform.scale(roadImage, (width, height))
    road = roadImage.get_rect(x=0, y=0)

    # Fonts
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    clock = pygame.time.Clock()

    # Music
    pygame.mixer.music.load("music.mp3")
    pygame.mixer.music.play()

    # Frog Object
    objFrog = Frog()

    # Enemy Object
    objEnemy = Enemy(x=100, y=100, img="enemy.png")

    # Main game loop
    while 1:
        # Fill screen to "update scene"
        screen.blit(roadImage, road)
        # 60fps cap
        textSurface = myfont.render((str(clock.get_fps())), True, black)
        clock.tick(60)

        # Update the rest of the images after the background
        water = pygame.draw.rect(screen, blue, (0, 160, width, 40))
        screen.blit(objFrog.image, objFrog.rect)
        screen.blit(textSurface, (50, 50))
        screen.blit(objEnemy.image, objEnemy.rect)

        # Capture all events
        for event in pygame.event.get():
            exitGame(event)
            objFrog.Movement(event)

        objEnemy.Movement(2)

        # Collisions             
        if objFrog.rect.colliderect(water):
            print("collision")

        if objFrog.rect.colliderect(objEnemy.rect):
            objFrog.ResetPosition()

        pygame.display.update()


if __name__ == "__main__":
    main()

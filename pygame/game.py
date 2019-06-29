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


class MovingModel(pygame.sprite.Sprite):
    def __init__(self, x, y, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join('', img))
        self.image = pygame.transform.scale(self.image, (self.radius, self.radius))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def Movement(self, velocity, direction="right"):
        self.velocity = velocity
        if direction == "right":
            self.rect = self.rect.move(velocity, 0)
            if self.rect.x > width:
                self.rect.x = -100
        else:
            if self.rect.x < -100:
                self.rect.x = width + 100
            self.rect = self.rect.move(-velocity, 0)


class Turtle(MovingModel):
    radius = 40

    def __init__(self, x, y, img):
        MovingModel.__init__(self, x, y, img)
        self.image = pygame.transform.smoothscale(self.image, (self.radius, self.radius))


class Car(MovingModel):
    radius = 70


class Trunk(MovingModel):
    radius = 85

    def __init__(self, x, y, img):
        MovingModel.__init__(self, x, y, img)
        self.image = pygame.transform.smoothscale(self.image, (self.radius+50, self.radius-45))


class Fly(MovingModel):
    radius = 40

    def __init__(self, x, y, img):
        MovingModel.__init__(self, x, y, img)
        self.image = pygame.transform.smoothscale(self.image, (self.radius, self.radius))
        self.maxY = self.rect.y + 3
        self.minY = self.rect.y - 3
        self.velocity = 1
        self.alive = True

    # Override generic method
    def Movement(self, velocity):
        if self.alive:

            if self.rect.y >= self.maxY:
                self.velocity = 1 * -self.velocity

            elif self.rect.y <= self.minY:
                self.velocity = 1 * -self.velocity

            self.rect = self.rect.move(0, self.velocity)



def exitGame(event):
    if event.type == pygame.QUIT:
        sys.exit()
    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
        sys.exit()


'''
Source:
stackoverflow.com/questions/42821442/how-do-i-change-the-colour-of-an-image-in-pygame-without-changing-its-transparen
'''
def fill(surface, color):
    """Fill all pixels of the surface with color, preserve transparency."""
    w, h = surface.get_size()
    r, g, b, _ = color
    for x in range(w):
        for y in range(h):
            a = surface.get_at((x, y))[3]
            surface.set_at((x, y), pygame.Color(r, g, b, a))


def main():
    # Scene Setup

    # Colours (RGB)
    black = 0, 0, 0
    blue = 0, 0, 255

    # Models/Images
    screen = pygame.display.set_mode(g_screenSize)

    # Road
    roadImage = pygame.image.load("road.png")
    roadImage = pygame.transform.scale(roadImage, (width, int(height/3)))
    road = roadImage.get_rect(x=0, y=height * 0.542)

    # Water
    waterImage = pygame.image.load("water.png")
    waterImage = pygame.transform.scale(waterImage, (roadImage.get_width(), roadImage.get_height()))
    water = waterImage.get_rect(x=0, y=height * 0.14)

    # Grass
    grassImage = pygame.image.load("grass.jpg")
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

    greenGrassImage = pygame.image.load("grass_green.jpg")
    greenGrassTopImage = pygame.transform.smoothscale(greenGrassImage, (width, 10))
    greenGrassImage = pygame.transform.smoothscale(greenGrassImage, (130, 90))
    listGreenGrass = (greenGrassImage.get_rect(x=-40, y=0),
                      greenGrassImage.get_rect(x=155, y=0),
                      greenGrassImage.get_rect(x=345, y=0),
                      greenGrassImage.get_rect(x=545, y=0),
                      greenGrassImage.get_rect(x=740, y=0),
                      greenGrassImage.get_rect(x=935, y=0))
    greenGrassTop = greenGrassImage.get_rect(x=0, y=0)

    # Fonts
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    clock = pygame.time.Clock()

    # Music
    pygame.mixer.music.load("music.mp3")
    pygame.mixer.music.play()

    # Frog Object
    objFrog = Frog()

    # Car Object
    listObjectCar = (Car(x=0, y=460, img="carBlack.png"),
                       Car(x=400, y=460, img="carTruckRight.png"),
                       Car(x=width, y=410, img="carFast.png"),
                       Car(x=0, y=365, img="carWhiteRight.png"),
                       Car(x=width-100, y=320, img="carTruckLeft.png"),
                       Car(x=100, y=320, img="carWhiteLeft.png"))

    # Turtle Object
    listObjectTurtle = (Turtle(x=145, y=240, img="turtle.png"),
                        Turtle(x=190, y=240, img="turtle.png"),
                        Turtle(x=235, y=240, img="turtle.png"),
                        Turtle(x=545, y=240, img="turtle.png"),
                        Turtle(x=590, y=240, img="turtle.png"),
                        Turtle(x=45, y=140, img="turtle.png"),
                        Turtle(x=90, y=140, img="turtle.png"),
                        Turtle(x=135, y=140, img="turtle.png"),
                        Turtle(x=745, y=140, img="turtle.png"),
                        Turtle(x=790, y=140, img="turtle.png"))
                        
    # Trunk Object
    listObjectTrunk = (Trunk(x=width/2, y=190, img="trunk.png"),
                        Trunk(x=width+100, y=190, img="trunk.png"),
                        Trunk(x=width-100, y=90, img="trunk.png"),
                        Trunk(x=width/3, y=90, img="trunk.png"),
                        Trunk(x=width-200, y=90, img="trunk.png"))

    # Fly Object
    listObjectFly = (Fly(x=100, y=30, img="fly.png"),
                     Fly(x=295, y=30, img="fly.png"),
                     Fly(x=490, y=30, img="fly.png"),
                     Fly(x=685, y=30, img="fly.png"),
                     Fly(x=880, y=30, img="fly.png"))

    time = 0
    # Main game loop
    while 1:
        # Fill screen to "update scene"
        
        # 60fps cap
        textSurface = myfont.render((str(clock.get_fps())), True, black)
        clock.tick(60)

        # Update the rest of the images after the background

        for grass in listGrass:
            screen.blit(grassImage, grass)

        # Update road after grass to "cut" grass image size
        screen.blit(roadImage, road)

        # Update top Grass (Green)
        for greenGrass in listGreenGrass:
            screen.blit(greenGrassImage, greenGrass)

        screen.blit(greenGrassTopImage, greenGrassTop)

        screen.blit(waterImage, water)


        # Update Turtle
        for turtle in listObjectTurtle:
            turtle.Movement(velocity=2.5,direction="right")
            screen.blit(turtle.image, turtle.rect)

        # Update Trunk
        for trunk in listObjectTrunk:
            trunk.Movement(velocity=1.5, direction="left")
            screen.blit(trunk.image, trunk.rect)

        # Update Fly
        # Slow down movement because minimum velocity is 1
        time = time + clock.get_time()
        if time >= 100:
            for fly in listObjectFly:
                fly.Movement(velocity=1)
            time = 0

        for fly in listObjectFly:
            screen.blit(fly.image, fly.rect)

        # Update Frog
        screen.blit(objFrog.image, objFrog.rect)

        screen.blit(textSurface, (50, 50))  # FPS

        for car in listObjectCar:
            screen.blit(car.image, car.rect)

        # Capture all events
        for event in pygame.event.get():
            exitGame(event)
            objFrog.Movement(event)

        listObjectCar[0].Movement(velocity=2, direction="right")
        listObjectCar[1].Movement(velocity=2, direction="right")
        listObjectCar[2].Movement(velocity=10, direction="left")
        listObjectCar[3].Movement(velocity=3, direction="right")
        listObjectCar[4].Movement(velocity=4, direction="left")
        listObjectCar[5].Movement(velocity=4, direction="left")


        # COLLISION DETECTION - RESOLUTION 
        frogTurtleCollision = False
        frogTrunkCollision = False
        # Frog - Turtle
        for turtle in listObjectTurtle:
            if objFrog.rect.colliderect(water) and objFrog.rect.colliderect(turtle.rect):
                frogTurtleCollision = True
        # Frog - Trunk
        for trunk in listObjectTrunk:
            if objFrog.rect.colliderect(water) and objFrog.rect.colliderect(trunk.rect):
                frogTrunkCollision = True

        # Collision Resolutions
        if frogTurtleCollision:
            objFrog.rect = objFrog.rect.move(turtle.velocity,0)
        elif frogTrunkCollision:
            objFrog.rect = objFrog.rect.move(-trunk.velocity,0)
        
        # Frog - Water
        elif objFrog.rect.colliderect(water):
            print("collision")
            objFrog.ResetPosition()

        # Frog - Car
        for enemy in listObjectCar:
            if objFrog.rect.colliderect(enemy.rect):
                print("collision")
                objFrog.ResetPosition()

        # Frog - Fly
        for fly in listObjectFly:
            if objFrog.rect.colliderect(fly.rect):
                # Turn fly into green color
                fill(fly.image, pygame.Color(0, 128, 0))
                fly.alive = False

        # Reset Frog position when it goes off screen (staying on turtle for too long)
        if (objFrog.rect.x > width) or (objFrog.rect.x < 0):
            objFrog.ResetPosition()
    
        pygame.display.update()


if __name__ == "__main__":
    main()

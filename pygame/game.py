import sys
import pygame
import os.path
import random

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
    kills = 0
    life = 3

    # Class Methods
    def Movement(self, event):
        frog = self.rect
        boundaries = yMin, xMin, xMax, yMax = self.radius, self.radius, width - self.radius * 2, height - self.radius
        right = [self.radius, 0]
        left = [-self.radius, 0]
        up = [0, -self.radius]
        down = [0, self.radius]
        # Keyboard Controls
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            # Boundaries
            if (frog.x > xMin):
                self.rect = frog.move(left)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            if (frog.x < xMax):
                self.rect = frog.move(right)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            if (frog.y > yMin):
                self.rect = frog.move(up)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            if (frog.y < yMax):
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
    radius = 30

    def __init__(self, x, y, img):
        MovingModel.__init__(self, x, y, img)
        self.image = pygame.transform.smoothscale(self.image, (self.radius, self.radius))


class Car(MovingModel):
    radius = 70


class Trunk(MovingModel):
    radius = 85

    def __init__(self, x, y, img):
        MovingModel.__init__(self, x, y, img)
        self.image = pygame.transform.smoothscale(self.image, (self.radius + 50, self.radius - 45))


class Fly(MovingModel):
    radius = 40
    activeFlySequence = set([0, 1, 2, 3, 4])

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


def initialiseObjects():
    objFrog = Frog()

    # Car Object
    listObjectCar = (Car(x=0, y=460, img="carBlack.png"),
                     Car(x=400, y=460, img="carTruckRight.png"),
                     Car(x=width, y=410, img="carFast.png"),
                     Car(x=0, y=365, img="carWhiteRight.png"),
                     Car(x=width - 100, y=320, img="carTruckLeft.png"),
                     Car(x=100, y=320, img="carWhiteLeft.png"))

    # Turtle Object
    listObjectTurtle = (Turtle(x=145, y=252, img="turtle.png"),
                        Turtle(x=190, y=252, img="turtle.png"),
                        Turtle(x=235, y=252, img="turtle.png"),
                        Turtle(x=545, y=252, img="turtle.png"),
                        Turtle(x=590, y=252, img="turtle.png"),
                        Turtle(x=45, y=185, img="turtle.png"),
                        Turtle(x=90, y=185, img="turtle.png"),
                        Turtle(x=135, y=185, img="turtle.png"),
                        Turtle(x=745, y=185, img="turtle.png"),
                        Turtle(x=790, y=185, img="turtle.png"),
                        Turtle(x=30, y=115, img="turtle.png"),
                        Turtle(x=275, y=115, img="turtle.png"),
                        Turtle(x=565, y=115, img="turtle.png"),
                        Turtle(x=890, y=115, img="turtle.png"))

    # Trunk Object
    listObjectTrunk = (Trunk(x=width / 2, y=215, img="trunk.png"),
                       Trunk(x=width + 100, y=215, img="trunk.png"),
                       Trunk(x=width - 100, y=145, img="trunk.png"),
                       Trunk(x=width / 3, y=145, img="trunk.png"),
                       Trunk(x=width - 200, y=145, img="trunk.png"))

    # Fly Object
    listObjectFly = (Fly(x=100, y=60, img="fly.png"),
                     Fly(x=295, y=60, img="fly.png"),
                     Fly(x=490, y=60, img="fly.png"),
                     Fly(x=685, y=60, img="fly.png"),
                     Fly(x=880, y=60, img="fly.png"))

    return objFrog, listObjectCar, listObjectTurtle, listObjectTrunk, listObjectFly


def main():
    # Scene Setup

    # Colours (RGB)
    black = 0, 0, 0
    skyBlue = 77, 166, 255

    # Models/Images
    screen = pygame.display.set_mode(g_screenSize)
    pygame.display.set_caption('Frogger Made With Pygame')

    # Road
    roadImage = pygame.image.load("road.png")
    roadImage = pygame.transform.scale(roadImage, (width, int(height / 3)))
    road = roadImage.get_rect(x=0, y=height * 0.542)

    # Water
    waterImage = pygame.image.load("water.png")
    waterImage = pygame.transform.scale(waterImage, (roadImage.get_width(), roadImage.get_height() - 30))
    water = waterImage.get_rect(x=0, y=height * 0.14 + 30)

    # Grass
    grassImage = pygame.image.load("grass.jpg")
    listGrass = (grassImage.get_rect(x=0, y=height - 175),
                 grassImage.get_rect(x=200, y=height - 175),
                 grassImage.get_rect(x=400, y=height - 175),
                 grassImage.get_rect(x=600, y=height - 175),
                 grassImage.get_rect(x=800, y=height - 175),
                 grassImage.get_rect(x=0, y=height * 0.4),
                 grassImage.get_rect(x=200, y=height * 0.4),
                 grassImage.get_rect(x=400, y=height * 0.4),
                 grassImage.get_rect(x=600, y=height * 0.4),
                 grassImage.get_rect(x=800, y=height * 0.4))

    greenGrassImage = pygame.image.load("grass_green.jpg")
    greenGrassTopImage = pygame.transform.smoothscale(greenGrassImage, (200, 20))
    greenGrassImage = pygame.transform.smoothscale(greenGrassImage, (130, 90))
    listGreenGrass = (greenGrassImage.get_rect(x=-40, y=30),
                      greenGrassImage.get_rect(x=155, y=30),
                      greenGrassImage.get_rect(x=345, y=30),
                      greenGrassImage.get_rect(x=545, y=30),
                      greenGrassImage.get_rect(x=740, y=30),
                      greenGrassImage.get_rect(x=935, y=30))

    listGreenGrassTop = (greenGrassImage.get_rect(x=0, y=30),
                         greenGrassImage.get_rect(x=155, y=30),
                         greenGrassImage.get_rect(x=345, y=30),
                         greenGrassImage.get_rect(x=545, y=30),
                         greenGrassImage.get_rect(x=740, y=30),
                         greenGrassImage.get_rect(x=935, y=30))

    # Cookie
    cookieImage = pygame.image.load("cookie.png")
    cookieImage = pygame.transform.smoothscale(cookieImage, (200, 200))
    cookie = cookieImage.get_rect(x=width / 2 - 200, y=height / 2 - 100)

    # Fonts
    myfont = pygame.font.SysFont('Comic Sans MS', 25)
    pauseFont = pygame.font.SysFont('Comic Sans MS', 60)
    winFont = pygame.font.SysFont('Comic Sans MS', 32)

    # Music
    pygame.mixer.music.load("music.mp3")
    pygame.mixer.music.play()

    # Clock Object
    clock = pygame.time.Clock()

    # Main Character + Moving Objects
    objFrog, listObjectCar, listObjectTurtle, listObjectTrunk, listObjectFly = initialiseObjects()

    carDifficulty = 30
    timeCarMovement = 0
    timerGameTime = 0
    timeFlyMovement = 0
    timeFlySpawn = 0
    collisionTimer = 0
    randomFlySpawn = random.choice(tuple(Fly.activeFlySequence))

    # Game states
    ''' 0: Intro State
        1: Play State
        2: Pause State
        3: Win State
        4: Over State
        5: Cookie State'''
    gameState = 0
    gameWon = False
    wave = 1
    gameTime = 120
    gameTimeDecrease = 0
    showFPS = False

    # Main game loop
    while 1:

        # --INTRO STATE--
        if gameState == 0:
            # Update Intro State
            screen.fill(skyBlue)
            listIntroText = (winFont.render("FROGGER - Press Enter To Start", True, black),
                             winFont.render("Goal: Eat all flies and avoid getting drown or hit by cars!!", True,
                                            black),
                             winFont.render("Extra: Wave System with increasing difficulty", True, black),
                             winFont.render("Controls", True, black),
                             winFont.render("Arrow keys: Move frog", True, black),
                             winFont.render("P: Toggle Pause/Show Controls", True, black),
                             winFont.render("ESC: Exit Game", True, black),
                             winFont.render("F: Show FPS", True, black),
                             winFont.render("Enter/Return: Start Game/Advance to next wave", True, black))
            listDeveloperText = (
            myfont.render("The game was created for the summer hacker challenge 2019 of UCLan Cyprus", True, black),
            myfont.render("Student/Developer: Floris Alexandrou", True, black))

            h = 0
            for text in listIntroText:
                screen.blit(text, (100, h))
                h += 50
            h += 50
            for text in listDeveloperText:
                screen.blit(text, (100, h))
                h += 50
            pygame.display.update()

            # Intro State Transitions
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    gameState = 1

                exitGame(event)

        # --PLAY STATE--
        elif gameState == 1:
            # Update Play State

            # Fill screen to "update scene"
            screen.fill(black)
            pygame.draw.rect(screen, skyBlue, (0, 0, width, 30))

            # Render Fonts
            # 60fps cap
            fpsText = myfont.render("fps:" + str(int(clock.get_fps())), True, black)
            lifeText = myfont.render("Lives:" + str(objFrog.life), True, black)
            waveText = myfont.render("Wave:" + str(wave), True, black)
            gameTimeText = myfont.render("Time Remaining:" + str(gameTime), True, black)
            clock.tick(60)

            # Main Timer Countdown
            timerGameTime += clock.get_time()
            if timerGameTime >= 1000:
                gameTime -= 1
                timerGameTime = 0

            # Update the rest of the images after the background

            for grass in listGrass:
                screen.blit(grassImage, grass)

            # Update road after grass to "cut" grass image size
            screen.blit(roadImage, road)

            # Update top Grass (Green)
            for greenGrass, greenGrassTop in zip(listGreenGrass, listGreenGrassTop):
                screen.blit(greenGrassImage, greenGrass)
                screen.blit(greenGrassTopImage, greenGrassTop)

            # Render Water
            screen.blit(waterImage, water)

            # Update Turtle
            for turtle in listObjectTurtle:
                turtle.Movement(velocity=2, direction="right")
                screen.blit(turtle.image, turtle.rect)

            # Update Trunk
            for trunk in listObjectTrunk:
                trunk.Movement(velocity=2, direction="left")
                screen.blit(trunk.image, trunk.rect)

            # Update Fly
            timeFlyMovement += clock.get_time()
            timeFlySpawn += clock.get_time()

            # Fly Movement
            # Slow down movement because minimum velocity is 1
            if timeFlyMovement >= 100:
                for fly in listObjectFly:
                    fly.Movement(velocity=1)
                timeFlyMovement = 0

            # Fly random spawn
            if timeFlySpawn >= 5000:
                if len(Fly.activeFlySequence) > 0:
                    randomFlySpawn = random.choice(tuple(Fly.activeFlySequence))
                    timeFlySpawn = 0

            # Render Fly
            for fly in listObjectFly:
                if fly.alive:
                    # Render Random Fly
                    screen.blit(listObjectFly[randomFlySpawn].image,
                                listObjectFly[randomFlySpawn].rect)
                else:
                    # Render Dead Fly
                    screen.blit(fly.image, fly.rect)

            # Update Frog
            screen.blit(objFrog.image, objFrog.rect)

            # Update texts

            # FPS
            if showFPS:
                screen.blit(fpsText, (940, 0))

            # Frog Life
            screen.blit(lifeText, (5, 0))

            # Time
            screen.blit(gameTimeText, (210, 0))

            # Wave
            screen.blit(waveText, (100, 0))

            for car in listObjectCar:
                screen.blit(car.image, car.rect)

            # Car Movement
            timeCarMovement += clock.get_time()
            if timeCarMovement >= carDifficulty:
                timeCarMovement = 0
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
            if objFrog.rect.y < height / 2:  # if statement for increased efficiency
                for turtle in listObjectTurtle:
                    if objFrog.rect.colliderect(water) and objFrog.rect.colliderect(turtle.rect):
                        frogTurtleCollision = True
                        break

                # Frog - Trunk
                for trunk in listObjectTrunk:
                    if objFrog.rect.colliderect(water) and objFrog.rect.colliderect(trunk.rect):
                        frogTrunkCollision = True
                        break

                # Collision Resolutions
                if frogTurtleCollision:
                    objFrog.rect = objFrog.rect.move(turtle.velocity, 0)
                elif frogTrunkCollision:
                    objFrog.rect = objFrog.rect.move(-trunk.velocity, 0)

                # Frog - Water
                elif objFrog.rect.colliderect(water):
                    objFrog.life -= 1
                    objFrog.ResetPosition()

                # Frog - Fly
                # Check if frog collides with the random spawned fly
                collisionTimer += clock.get_time()
                if collisionTimer >= 200:  # Added to fix an error causing the collision to occur multiple times
                    if objFrog.rect.colliderect(listObjectFly[randomFlySpawn].rect):
                        collisionTimer = 0
                        # Turn fly into green color
                        fill(listObjectFly[randomFlySpawn].image, pygame.Color(0, 128, 0))
                        # Remove fly from random spawning set
                        Fly.activeFlySequence.discard(randomFlySpawn)
                        listObjectFly[randomFlySpawn].alive = False
                        objFrog.kills += 1
                        objFrog.ResetPosition()

            # Frog - Car
            if objFrog.rect.y > height / 2:  # if statement for increased efficiency
                for enemy in listObjectCar:
                    if objFrog.rect.colliderect(enemy.rect):
                        objFrog.life -= 1
                        objFrog.ResetPosition()
                        break

            # Reset Frog position when it goes out of bounds(e.g staying on turtle for too long)
            if (objFrog.rect.x > width - 10) or (objFrog.rect.x < -20):
                objFrog.life -= 1
                objFrog.ResetPosition()

            if (objFrog.rect.y < 100) and not (objFrog.rect.colliderect(listObjectFly[randomFlySpawn].rect)):
                objFrog.life -= 1
                objFrog.ResetPosition()

            pygame.display.update()

            # Capture all events (keyboard events)
            for event in pygame.event.get():
                exitGame(event)
                objFrog.Movement(event)

                if event.type == pygame.KEYDOWN and event.key == pygame.K_f:
                    if not showFPS:
                        showFPS = True
                    else:
                        showFPS = False

                # Play State Transitions
                if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                    gameState = 2

                if event.type == pygame.KEYDOWN and event.key == pygame.K_3:
                    gameState = 3

                if event.type == pygame.KEYDOWN and event.key == pygame.K_0:
                    gameState = 0

            if objFrog.life == 0:
                gameState = 4

            if gameTime <= 0:
                gameState = 4

            if objFrog.kills == 5:
                gameState = 3

            if wave == 5 and not gameWon:
                gameState = 5
                gameWon = True

        # --PAUSE STATE--
        elif gameState == 2:
            # Update Pause State
            pauseText = pauseFont.render("PAUSED", True, black)
            listControlsText = (winFont.render("Controls", True, black),
                                winFont.render("Arrow keys: Move frog", True, black),
                                winFont.render("P: Toggle Pause/Show Controls", True, black),
                                winFont.render("ESC: Exit Game", True, black),
                                winFont.render("F: Show FPS", True, black),
                                winFont.render("Enter/Return: Start Game/Advance to next wave", True, black))
            screen.blit(pauseText, (width / 2 - 125, height / 2 - 200))
            h = height / 2 - 100
            for text in listControlsText:
                screen.blit(text, (120, h))
                h += 50
            pygame.display.update()

            # Pause State Transitions
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                    gameState = 1
                exitGame(event)

        # --WIN STATE--
        elif gameState == 3:
            # Update Win State
            winText = (winFont.render("Congratulations for passing wave " + str(wave), True, black),
                       winFont.render("Press Enter to proceed to the next wave!!", True, black),
                       myfont.render("Notice: After each wave the cars move faster and the time decreases!!", True,
                                     black),
                       myfont.render("Reach wave 5 for a small surprise!", True, black))
            h = height / 2 - 75
            for text in winText:
                screen.blit(text, (100, h))
                h += 50
            pygame.display.update()
            # Win State Transitions
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    objFrog.ResetPosition()
                    if gameTimeDecrease < 45:
                        gameTimeDecrease += 15
                    if carDifficulty > 0:
                        carDifficulty -= 10
                    gameTime = 120 - gameTimeDecrease
                    wave += 1
                    gameState = 1
                    listObjectFly = (Fly(x=100, y=60, img="fly.png"),
                                     Fly(x=295, y=60, img="fly.png"),
                                     Fly(x=490, y=60, img="fly.png"),
                                     Fly(x=685, y=60, img="fly.png"),
                                     Fly(x=880, y=60, img="fly.png"))

        # --OVER STATE--
        elif gameState == 4:
            # Update Over State
            listOverText = (winFont.render("Game Over!! Thank you for playing :)", True, black),
                            winFont.render("You have reached Wave: " + str(wave), True, black),
                            winFont.render("Press R to restart game or ESC to quit", True, black))
            h = height / 2 - 150
            for text in listOverText:
                screen.blit(text, (250, h))
                h += 50
            pygame.display.update()

            # Over State Transitions
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                    gameState = 1
                    wave = 1
                    gameTime = 120
                    gameTimeDecrease = 0
                    objFrog, listObjectCar, listObjectTurtle, listObjectTrunk, listObjectFly = initialiseObjects()

                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    exitGame(event)

        elif gameState == 5:
            pass
            # Update Cookie state
            listCookieText = (winFont.render("GAME WON!!!", True, black),
                              winFont.render("Well Done! Here, take a cookie!", True, black))
            listAfterCookieText = (myfont.render("Thank you for your time spent!", True, black),
                                   myfont.render("The game's difficulty won't increase further", True, black),
                                   myfont.render("Press Enter to Continue", True, black))
            h = height / 2 - 190
            h2 = height - 210
            for text in listCookieText:
                screen.blit(text, (250, h))
                h += 50
            for text in listAfterCookieText:
                screen.blit(text, (250, h2))
                h2 += 50
            screen.blit(cookieImage, cookie)
            pygame.display.update()

            # Cookie State Transitions
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    gameState = 1


if __name__ == "__main__":
    main()

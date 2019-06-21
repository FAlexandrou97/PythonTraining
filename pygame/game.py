import sys
import pygame
pygame.init()
pygame.mixer.init()
pygame.font.init()

g_screenSize = width, height = 600, 400

class Frog:
    # Class variables
    m_radius = 40
    m_image = pygame.image.load("pygame/frog.png")
    m_image = pygame.transform.scale(m_image, (m_radius, m_radius))
    m_frog = m_image.get_rect(x=width/2-20, y=height-40)
    

    # Class Methods
    def Movement(self, event):
        frog = self.m_frog
        boundaries = yMin, xMin, xMax, yMax = 0, 0, width-40, height-40
        right = [self.m_radius, 0]
        left = [-self.m_radius, 0]
        up = [0, -self.m_radius]
        down = [0, self.m_radius]
        # Keyboard Controls
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            print("Going Left")
            # Boundaries
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

         # Constructor
    def __init__(self):
        pass


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
    roadImage = pygame.image.load("pygame/road.png")
    roadImage = pygame.transform.scale(roadImage, (width, height))
    road = roadImage.get_rect(x=0, y=0)

    # Fonts
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    clock = pygame.time.Clock()

    # Music
    pygame.mixer.music.load("pygame/music.mp3")
    pygame.mixer.music.play()

    # Frog Object
    objFrog = Frog()

    # Enemy
    enemyX = 0
    enemyVelocity = 0.2
    enemy = pygame.draw.rect(screen, black, (enemyX, height-80, 80, objFrog.m_radius))

    # Main game loop
    while 1:
        # Fill screen to "update scene"
        screen.blit(roadImage, road)
        # 60fps cap
        textsurface = myfont.render((str(clock.get_fps())), True, black)
        clock.tick(60)

        # Update the rest of the images after the background
        water = pygame.draw.rect(screen, blue, (0, 160, width, 40))
        enemy = pygame.draw.rect(screen, black, (enemyX, height-80, 80, objFrog.m_radius))
        screen.blit(objFrog.m_image, objFrog.m_frog)
        screen.blit(textsurface, (50,50))

        # Capture all events
        for event in pygame.event.get():
            exitGame(event)
            objFrog.Movement(event)


        enemyX = enemyX + enemyVelocity

        # Collisions             
        if(objFrog.m_frog.colliderect(water)):
            print("collision")

        pygame.display.update()

if __name__ == "__main__":
    main()
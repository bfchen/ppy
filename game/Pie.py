import  pygame, sys, math
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption("Draw shape")
myfont = pygame.font.Font(None, 50)
white = 255, 255, 255
blue = 0, 0, 200
textImage = myfont.render("Hello pygame", True, white)

# rect position and vel
posX = 300
posY = 250
velX = 2
velY = 1

while True:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            sys.exit()
    screen.fill(blue)
    screen.blit(textImage, (100, 100))
    
    # circle
    color = 255, 255, 0
    position = 300, 250
    print(type(position))
    radius = 100
    width = 10
    pygame.draw.circle(screen, color, position, radius, width)

    # rect, moving
    posX += velX
    posY += velY

    # keep rect on the screen
    if posX > 500 or posX < 0:
    	velX = -velX
    if posY > 400 or posY < 0:
    	velY = -velY

    # draw the rect
    color1 = 255, 0, 255
    width = 0 # solid fill
    pos = posX, posY, 100, 100
    pygame.draw.rect(screen, color1, pos, width)
    
    pygame.draw.line(screen, color, (100,150), (500, 400), 8)

    # arc
    startAngle = math.radians(0)
    endAngle = math.radians(180)
    arcPosition = 350, 150, 200, 200
    pygame.draw.arc(screen, color, arcPosition, startAngle, endAngle, 8)

    pygame.display.update()







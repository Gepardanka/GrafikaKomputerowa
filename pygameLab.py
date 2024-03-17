import pygame
import math

pygame.init()
win = pygame.display.set_mode((600, 600))
pygame.display.set_caption("First Game")

# deklarowanie kolorów
CZERWONY = (255, 0, 0)
ZIELONY = (0, 255, 0)
ZOLTY = (255, 255, 0)
FIOLETOWY = (128, 0, 128)
JASNY_NIEBIESKI = (0, 255, 255)
POMARANCZOWY = (255, 165, 0)
NIEBIESKI = (0, 0, 255)
SZARY = (128, 128, 128)
BIALY = (255, 255, 255)
CZARNY = (0, 0, 0)

basePolygon = [(-150, 0), (-75, -130), (75, -130), (150, 0), (75, 130), (-75, 130)]
pressed = 0
points = []

def scale_poly(pointList, x, y):
    scaledList = []
    for p in pointList:
        scaledList.append((p[0] * x, p[1] * y))
    return scaledList
def translate(pointList, x, y):
    scaledList = []
    for p in pointList:
        scaledList.append((p[0] + x, p[1] + y))
    return scaledList
def rotate(pointList, angle):
    scaledList = []
    for p in pointList:
        scaledList.append((p[0] * math.cos(angle) - p[1] * math.sin(angle), p[1] * math.cos(angle) + p[0] * math.sin(angle)))
    return scaledList
def kickX(pointList, x):
    scaledList = []
    for p in pointList:
        if p[1] > 0:
            scaledList.append((p[0] - x, p[1]))
        elif p[1] < 0:
            scaledList.append((p[0] + x, p[1]))
        else:
            scaledList.append((p[0], p[1]))      
    return scaledList
def mirror(pointList):
    scaledList = []
    for p in pointList:
        scaledList.append((-p[0], p[1]))
    return scaledList

run = True
while run:
    #tło:
    pygame.draw.rect(win, BIALY, (0, 0, 600, 600))
    pygame.draw.rect(win, ZOLTY, (10, 30, 580, 560))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            #1.
            if event.key == pygame.K_1:
                pressed = 1
            if event.key == pygame.K_2:
                pressed = 2
            if event.key == pygame.K_3:
                pressed = 3
            if event.key == pygame.K_4:
                pressed = 4
            if event.key == pygame.K_5:
                pressed = 5
            if event.key == pygame.K_6:
                pressed = 6
            if event.key == pygame.K_7:
                pressed = 7
            if event.key == pygame.K_8:
                pressed = 8
            if event.key == pygame.K_9:
                pressed = 9
            if event.key == pygame.K_0:
                pressed = 0

    if pressed == 1:
        points = scale_poly(basePolygon, 0.5, 0.5)
        points = translate(points, 300, 300)

    if pressed == 2 :
        points = rotate(basePolygon, -math.pi/4)
        points = translate(points, 300, 300)

    if pressed == 3:
        points = rotate(basePolygon, math.pi)
        points = scale_poly(points, 0.5, 1)
        points = mirror(points)
        points = translate(points, 300, 300)

    if pressed == 4:
        points = kickX(basePolygon, -20)
        points = translate(points, 300, 300)
    
    if pressed == 5:
        points = scale_poly(basePolygon, 1, 0.5)
        points = translate(points, 300, 95)
    
    if pressed == 6:
        points = kickX(basePolygon, -20)
        points = rotate(points, math.pi/2)
        points = translate(points, 300, 300)
    
    if pressed == 7:
        points = rotate(basePolygon, math.pi)
        points = scale_poly(points, 0.5, 1)
        points = translate(points, 300, 300)    

    if pressed == 8:
        points = scale_poly(basePolygon, 1, 0.5)
        points = rotate(points, math.pi/4)
        points = translate(points, 200, 400)

    if pressed == 9:
        points = kickX(basePolygon, -20)
        points = rotate(points, math.pi)
        points = translate(points, 450, 300)

    if pressed == 0:
        points = []
        triangle = [(1, 0), (0, 0), (0, 1)]
        tr1 = rotate(triangle, -math.pi/4)
        tr1 = scale_poly(tr1, 150, 150)
        tr1 = translate(tr1, 300, 300)
        pygame.draw.polygon(win, ZIELONY, tr1)

        tr2 = rotate(triangle, 3 * math.pi/4)
        tr2 = scale_poly(tr2, 150, 150)
        tr2 = translate(tr2, 300, 300)
        pygame.draw.polygon(win, ZIELONY, tr2)

        tr3 = rotate(triangle, 5 * math.pi/4)
        tr3 = scale_poly(tr3, 150, 150)
        tr3 = translate(tr3, 300, 300)
        pygame.draw.polygon(win, ZIELONY, tr3)
    
    if len(points) > 2:
        pygame.draw.polygon(win, ZIELONY, points)
    
    # wypisywanie tekstu
    font = pygame.font.SysFont('comicsans', 15)
    label = font.render(str(pressed) + '.', 1, (CZARNY))
    win.blit(label, (10, 8))
    pygame.display.update()


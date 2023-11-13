import pygame
from src import TkQuadTree

pygame.init()
screen = pygame.display.set_mode((1080, 720))
clock = pygame.time.Clock()
running = True

filename = "files/quadtree.txt"
quadTree_to_paint = TkQuadTree.fromFile(filename)

while running :

    for event in pygame.event.get() :
        if event.type == pygame.QUIT:
            running = False
    screen.fill("white")
    quadTree_to_paint.paint(screen)
    print("TEST")
    pygame.display.flip()
    clock.tick(60)
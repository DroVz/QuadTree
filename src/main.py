import pygame
from src import TkQuadTree

WIDTH_SCREEN = 1080
HEIGHT_SCREEN = 720

pygame.init()
screen = pygame.display.set_mode((WIDTH_SCREEN, HEIGHT_SCREEN))
clock = pygame.time.Clock()
running = True

filename = "files/quadtree_extra_color.txt"
quadTree_to_paint = TkQuadTree.fromFile(filename)


while running :

    for event in pygame.event.get() :
        if event.type == pygame.QUIT:
            running = False
    screen.fill("white")
    quadTree_to_paint.paint(screen)
    pygame.display.flip()
    clock.tick(60)

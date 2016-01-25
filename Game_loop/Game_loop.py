import pygame
from pygame.locals import*
from Button import *

pygame.init()

img = pygame.image.load('board.png')
lol = pygame.image.load("pawn.png")

navy = (0, 150, 200)
w = 800
h = 700
screen = pygame.display.set_mode((w, h))
screen.fill((navy))
running = 1


while running:
    screen.fill((navy))
    screen.blit(img,(0,0))
    screen.blit(lol,(0,0))
    pygame.display.flip()
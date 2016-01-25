import pygame
from pygame.locals import*
from Button import *

pygame.init()

board = pygame.image.load("Content\board.png")
yellowpawn = pygame.image.load("Content\yellowpawn.png")
greenpawn = pygame.image.load("Content\greenpawn.png")
redpawn = pygame.image.load("Content\redpawn.png")
bluepawn = pygame.image.load("Content\bluepawn.png")


navy = (0, 150, 200)
w = 800
h = 800
screen = pygame.display.set_mode((w, h))
screen.fill((navy))
running = 1


while running:
    screen.fill((navy))
    screen.blit(board,(0,0))
    screen.blit(yellowpawn,(650,5))
    screen.blit(greenpawn,(20,5))
    screen.blit(redpawn,(20,660))
    screen.blit(bluepawn,(650,660))
    pygame.display.flip()
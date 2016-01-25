import pygame
from Game_loop import *
from Game_menu import *
from Game_rules import *
from p_selection import *
from Pawn import *
 
pygame.init()
 
display_width = 1280
display_height = 720
 
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

navy = (0,150,200)

gray = (100,100,100)
dark_gray = (80,80,80)

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Survivor')
clock = pygame.time.Clock()

next = "menu"

def quitgame():
  pygame.quit()
  quit()

while next == "menu":
  print("1 komkommer is er 1 te veel.")
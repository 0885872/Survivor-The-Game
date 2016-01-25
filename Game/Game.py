import pygame#
import Game_menu
import Game_rules
import p_selection
import Pawn
 
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
  print("2 komkommer is er 1 te veel.")
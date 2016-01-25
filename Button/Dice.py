mport random
import pygame

class Dice:
  def __init__(self, x, y):
    self.X = x
    self.Y = y
    
  diceval = 0

  dice1 = pygame.image.load("Content\dice_1.png").convert_alpha()
  dice2 = pygame.image.load("Content\dice_2.png").convert_alpha()
  dice3 = pygame.image.load("Content\dice_3.png").convert_alpha()
  dice4 = pygame.image.load("Content\dice_4.png").convert_alpha()
  dice5 = pygame.image.load("Content\dice_5.png").convert_alpha()
  dice6 = pygame.image.load("Content\dice_6.png").convert_alpha()

  def dice(self, diceval):
    dthrow = random.randint(1,6)
    while diceval == dthrow:
      dthrow = random.randint(1,6)
    diceval = dthrow

    if dthrow == 1:
      #draw pic with 1 eye
      gameDisplay.blit(self.dice1, (self.X, self.Y))
    elif dthrow == 2:
      #draw pic with 2 eyes
      gameDisplay.blit(self.dice2, (self.X, self.Y))
    elif dthrow == 3:
      #draw pic with 3 eyes
      gameDisplay.blit(self.dice3, (self.X, self.Y))
    elif dthrow == 4:
      #draw lic with 4 eyes
      gameDisplay.blit(self.dice4, (self.X, self.Y))
    elif dthrow == 5:
      #draw pic with 5 eyes
      gameDisplay.blit(self.dice5, (self.X, self.Y))
    else:
      #draw pic with 6 eyes
      gameDisplay.blit(self.dice6, (self.X, self.Y))
    pygame.display.update()
    return diceval


  def throwdice(self):
    for x in range(0,8):
      diceval = self.dice(self.diceval)
      time.sleep(((x/1.5)**2*0.05))

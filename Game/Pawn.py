import pygame
from Tile import *
from Dice import *

class Pawn():
    def __init__(self, color, name, pos, next_pos, lifepoints, energypoints, moves_left):
      self.Color = color
      self.Name = name
      self.Pos = position
      self.Next_pos = next_pos
      self.Lifepoints = lifepoints
      self.Energypoints = energypoints
      self.Moves_left = moves_left
      

    def Update(self):
      return self
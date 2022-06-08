import pygame
from Player import *
from random import randint

class Platform():
    def __init__(self,x,y,width,height) -> None:
        self.x1=x
        self.y1=y
        self.x2=x+width
        self.y2=y+height

    def test(self, Player):
        if Player.x<self.x1 or Player.x>self.x2:
            return None
        if Player.y<=self.y1 and Player.y+Player.velocity>=self.y2:
            return self
        return None

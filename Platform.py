import pygame
from Player import *

platform_images = [pygame.image.load('platform tri edges.png'), pygame.image.load('platform rectangle.png')]

'''class Platform():
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
        return None'''

class Platform():
    def __init__(self, x, y):
        self.image = pygame.image.load('platform tri edges.png').convert()
        #self.rect = self.image.get_rect()
        self.y = y
        self.x1 = x
        self.x2= x+237
        self.hitbox = (self.x1 + 10, self.y, 237,22)

    def draw(self,window):
        self.hitbox = (self.x1 + 10, self.y, 237,22)
        pygame.draw.rect(window, (255,0,0), self.hitbox, 2)
        window.blit(self.image, (self.x1,self.y))

    '''def test(self, Player):
        if Player.x<self.x1 or Player.x>self.x2:
            return None
        if Player.y<=self.y and Player.y+Player.velocity>=self.y:
            return self
        return None'''

    def test(self, Player):
        if Player.x>self.x1 and Player.x<self.x2:
            if Player.y<=self.y or Player.y+Player.velocity>=self.y:
                return self
        return None


import pygame
from Platform import *
from Player import Player

platform_images = [pygame.image.load('platform tri edges.png'), pygame.image.load('platform rectangle.png')]

class Platforms():
    def __init__(self) -> None:
        self.container=[Platform(200, 300), Platform(400, 400), Platform(700, 500), Platform(900, 300), Platform(2000, 100)]

    def testCollision(self,Player):
        for p in self.container:
            result =p.test(Player)
            if result:
                Player.current_platform = result
                Player.y=result.y
                #Player.falling=False
                return True
        return False
    def draw(self,window):
        for p in self.container:
            p.hitbox = (p.x1 + 10, p.y, 237,22)
            pygame.draw.rect(window, (255,0,0), p.hitbox, 2)
            window.blit(p.image, (p.x1,p.y))

    '''if Player.x>p.x and Player.x<p.x+237:
                if Player.y==p.y and Player.y+Player.velocity>=p.y:
                    Player.y=p.y
            if result!=None:
                #Player.current_platform = result
                Player.y=result
                Player.falling = False'''
import pygame

poop_bullet = pygame.image.load("assets/poop_bullet.png")

#initialising variables for bullets
class Projectile(object):
    def __init__(self,x,y,hw,color,facing):
        self.x = x
        self.y = y
        self.hw = 14.5
        self.color = color
        self.facing = facing
        self.vel = 18 * facing

#for blit of bullets
    def draw(self,window):
        #pygame.draw.circle(window, self.color, (self.x,self.y), self.radius)
        window.blit(poop_bullet, (self.x, self.y))
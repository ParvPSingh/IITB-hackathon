import pygame

walkRight = [pygame.image.load('rer1.png'), pygame.image.load('rer2.png'), pygame.image.load('rer3.png'), pygame.image.load('rer4.png'), pygame.image.load('rer stand.png')]
walkLeft = [pygame.image.load('rel1.png'), pygame.image.load('rel2.png'), pygame.image.load('rel3.png'), pygame.image.load('rel4.png'), pygame.image.load('rel stand.png')]


class Enemy():
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.walkCount = 0
        self.vel = 3
        self.hitbox = (self.x + 17, self.y + 2, 70, 110)
        self.health = 10
        self.visible = True

    def draw(self,window):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 12:
                self.walkCount = 0

            if self.vel > 0:
                window.blit(walkRight[self.walkCount //3], (self.x, self.y))
                self.walkCount += 1
            else:
                window.blit(walkLeft[self.walkCount //3], (self.x, self.y))
                self.walkCount += 1

            pygame.draw.rect(window, (255,0,0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
            pygame.draw.rect(window, (0,128,0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 - self.health)), 10))
            self.hitbox = (self.x + 17, self.y + 2, 70, 110)
            pygame.draw.rect(window, (255,0,0), self.hitbox,2)

    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0

    def hit(self):
        if self.health > 0:
            self.health -= 1
        else:
            self.visible = False
        print('hit')

        


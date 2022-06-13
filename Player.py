import pygame

walkRight = [pygame.image.load('ar_01.png'), pygame.image.load('ar_02.png'), pygame.image.load('ar_03.png'), pygame.image.load('ar_04.png'), pygame.image.load('ar_05.png'), pygame.image.load('ar_06.png'), pygame.image.load('ar_07.png'), pygame.image.load('ar_08.png'), pygame.image.load('ar_09.png'), pygame.image.load('ar_10.png'), pygame.image.load('ar_11.png'), pygame.image.load('ar_12.png'), pygame.image.load('ar_13.png'), pygame.image.load('ar_16.png')]
walkLeft = [pygame.image.load('al_01.png'), pygame.image.load('al_02.png'), pygame.image.load('al_03.png'), pygame.image.load('al_04.png'), pygame.image.load('al_05.png'), pygame.image.load('al_06.png'), pygame.image.load('al_07.png'), pygame.image.load('al_08.png'), pygame.image.load('al_09.png'), pygame.image.load('al_10.png'), pygame.image.load('al_11.png'), pygame.image.load('al_12.png'), pygame.image.load('al_13.png'), pygame.image.load('al_16.png')]

#initialising all variables
class Player():
    def __init__(self,x,y,rec_width,rec_height) -> None:
        self.x=x-rec_width
        self.y=y-30
        self.rec_width=rec_width
        self.rec_height=rec_height
        self.velocity=8
        self.square_side=rec_width
        self.square_posX=rec_width
        self.left=False
        self.right=False
        self.isShoot=False
        self.walkCount=0
        self.isJump=False
        self.jumpCount=10
        self.standing=True
        self.falling=True
        self.current_platform=None
        self.hitbox=(self.square_posX,self.y,self.rec_width, self.rec_height)
        
    #drawing player
    def draw(self,window):
        if self.walkCount+1>=27:
            self.walkCount=0

        if self.standing==False:
            if self.right:
                window.blit(walkRight[self.walkCount//3],(self.square_posX, self.y))
                self.walkCount+=1
            elif self.left:
                window.blit(walkLeft[self.walkCount//3],(self.square_posX, self.y))
                self.walkCount+=1
        else:
            if self.right:
                window.blit(walkRight[13],(self.square_posX, self.y))
            else:
                window.blit(walkLeft[13],(self.square_posX, self.y))
        
        self.hitbox=(self.square_posX+20,self.y+20,self.rec_width-40, self.rec_height+10)
        #pygame.draw.rect(window, (255,0,0), self.hitbox, 2)
        pygame.display.flip()

    #hit function for astronaut
    def hit(self,window):
        self.isJump = False
        self.jumpCount = 10
        self.x = self.x-500
        self.y = 20
        self.walkCount = 0
        '''font1 = pygame.font.SysFont('comicsans', 100)
        text = font1.render('-5', 1, (200,0,0))
        window.blit(text, (250 - (text.get_width()/2),200))
        pygame.display.update()'''
        while self.y<450:
            self.y+=1
        i = 0
        while i < 150:
            pygame.time.delay(1)
            i += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = 11
                    pygame.quit()
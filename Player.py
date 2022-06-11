import pygame

walkRight = [pygame.image.load('ar_01.png'), pygame.image.load('ar_02.png'), pygame.image.load('ar_03.png'), pygame.image.load('ar_04.png'), pygame.image.load('ar_05.png'), pygame.image.load('ar_06.png'), pygame.image.load('ar_07.png'), pygame.image.load('ar_08.png'), pygame.image.load('ar_09.png'), pygame.image.load('ar_10.png'), pygame.image.load('ar_11.png'), pygame.image.load('ar_12.png'), pygame.image.load('ar_13.png'), pygame.image.load('ar_16.png')]
walkLeft = [pygame.image.load('al_13.png'), pygame.image.load('al_12.png'), pygame.image.load('al_11.png'), pygame.image.load('al_10.png'), pygame.image.load('al_09.png'), pygame.image.load('al_08.png'), pygame.image.load('al_07.png'), pygame.image.load('al_06.png'), pygame.image.load('al_05.png'), pygame.image.load('al_04.png'), pygame.image.load('al_03.png'), pygame.image.load('al_02.png'), pygame.image.load('al_01.png'), pygame.image.load('al_16.png')]
shootRight = [pygame.image.load('r15.png'), pygame.image.load('r16.png'), pygame.image.load('r17.png'), pygame.image.load('r18.png'), pygame.image.load('r19.png'), pygame.image.load('r20.png'), pygame.image.load('r21.png'), pygame.image.load('r22.png'), pygame.image.load('r23.png'), pygame.image.load('r24.png'), pygame.image.load('r25.png')]
shootLeft = [pygame.image.load('l15.png'), pygame.image.load('l16.png'), pygame.image.load('l17.png'), pygame.image.load('l18.png'), pygame.image.load('l19.png'), pygame.image.load('l20.png'), pygame.image.load('l21.png'), pygame.image.load('l22.png'), pygame.image.load('l23.png'), pygame.image.load('l24.png'), pygame.image.load('l25.png')]

class Player():
    def __init__(self,x,y,rec_width,rec_height) -> None:
        self.x=x-rec_width
        self.y=y-30
        self.rec_width=rec_width
        self.rec_height=rec_height
        self.velocity=7.5
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
        pygame.draw.rect(window, (255,0,0), self.hitbox, 2)
        pygame.display.flip()

    def hit(self,window):
        self.isJump = False
        self.jumpCount = 10
        self.x = 100
        self.y = 450
        self.walkCount = 0
        font1 = pygame.font.SysFont('comicsans', 100)
        text = font1.render('-5', 1, (255,0,0))
        window.blit(text, (250 - (text.get_width()/2),200))
        pygame.display.update()
        i = 0
        while i < 200:
            pygame.time.delay(10)
            i += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = 201
                    pygame.quit()
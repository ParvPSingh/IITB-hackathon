import pygame

walkRight = [pygame.image.load('r1.png'), pygame.image.load('r2.png'), pygame.image.load('r3.png'), pygame.image.load('r4.png'), pygame.image.load('r5.png'), pygame.image.load('r6.png'), pygame.image.load('r7.png'), pygame.image.load('r8.png'), pygame.image.load('r9.png'), pygame.image.load('r10.png'), pygame.image.load('r11.png'), pygame.image.load('r12.png'), pygame.image.load('r13.png'), pygame.image.load('r14.png')]
walkLeft = [pygame.image.load('l13.png'), pygame.image.load('l12.png'), pygame.image.load('l11.png'), pygame.image.load('l10.png'), pygame.image.load('l9.png'), pygame.image.load('l8.png'), pygame.image.load('l7.png'), pygame.image.load('l6.png'), pygame.image.load('l5.png'), pygame.image.load('l4.png'), pygame.image.load('l3.png'), pygame.image.load('l2.png'), pygame.image.load('l1.png'), pygame.image.load('l14.png')]
shootRight = [pygame.image.load('r15.png'), pygame.image.load('r16.png'), pygame.image.load('r17.png'), pygame.image.load('r18.png'), pygame.image.load('r19.png'), pygame.image.load('r20.png'), pygame.image.load('r21.png'), pygame.image.load('r22.png'), pygame.image.load('r23.png'), pygame.image.load('r24.png'), pygame.image.load('r25.png')]
shootLeft = [pygame.image.load('l15.png'), pygame.image.load('l16.png'), pygame.image.load('l17.png'), pygame.image.load('l18.png'), pygame.image.load('l19.png'), pygame.image.load('l20.png'), pygame.image.load('l21.png'), pygame.image.load('l22.png'), pygame.image.load('l23.png'), pygame.image.load('l24.png'), pygame.image.load('l25.png')]

class Player():
    def __init__(self,x,y,rec_width,rec_height) -> None:
        self.x=x
        self.y=y
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
        self.hitbox=(self.x+17,self.y+11,29,52)

    def draw(self,window):
        if self.walkCount+1>=27:
            self.walkCount=0

        if self.standing==False:
            if self.right:
                window.blit(walkRight[self.walkCount//3],(self.square_posX, self.y-self.square_side))
                self.walkCount+=1
            elif self.left:
                window.blit(walkLeft[self.walkCount//3],(self.square_posX, self.y-self.square_side))
                self.walkCount+=1
        else:
            if self.right:
                window.blit(walkRight[13],(self.square_posX, self.y-self.square_side))
            else:
                window.blit(walkLeft[13],(self.square_posX, self.y-self.square_side))
        #pygame.draw.rect(window, (255,0,0), (self.square_posX, self.y-self.square_side, self.rec_width, self.rec_height))
        pygame.display.flip()
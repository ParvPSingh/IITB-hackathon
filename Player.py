import pygame

class Player():
    def __init__(self,x,y,rec_width,rec_height) -> None:
        self.x=x
        self.y=y
        self.rec_width=rec_width
        self.rec_height=rec_height
        self.velocity=15
        self.left=False
        self.right=False
        self.walkCount=0
        self.isJump=False
        self.jumpCount=10
        self.standing=True
        self.hitbox=(self.x+17,self.y+11,29,52)

    def draw(self,window):
        if self.walkCount+1>=27:
            self.walkCount=0

        if self.standing==False:
            if self.right:
                #window.blit(walkRight[self.walkCount//3],(self.x,self.y))
                self.walkCount+=1
            elif self.left:
                #window.blit(walkLeft[self.walkCount//3],(self.x,self.y))
                self.walkCount+=1
        else:
            if self.right:
                pass
                #window.blit(walkRight[0],(self.x,self.y))
            else:
                pass
                #window.blit(walkLeft[0],(self.x,self.y))
        pygame.draw.rect(window, (255,0,0), (self.x, self.y, self.rec_width, self.rec_height))
        pygame.display.flip()
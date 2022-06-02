import pygame
from Player import Player
pygame.init()

screen_width=610
screen_height=347
window=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('SPACE PLUMBER')
bg = pygame.image.load(('space corridor.jpg'))
bgX = 0
bgX2 = bg.get_width()

clock=pygame.time.Clock()

def redraw_GameWindow():
    #window.blit(bg, (0,0))
    window.blit(bg, (bgX, 0))
    window.blit(bg, (bgX2, 0))
    man.draw(window)
    pygame.display.update()

man=Player(10,281,64,64)
run=True
while run:

    redraw_GameWindow()

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False

    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and man.x>man.velocity:
        man.x-=man.velocity
        bgX += 61
        bgX2 += 61
        if bgX < bg.get_width() * 1:
            bgX = bg.get_width()
    
        if bgX2 < bg.get_width() * 1:
            bgX2 = bg.get_width()

        man.left=True
        man.right=False
        man.standing=False
    elif keys[pygame.K_RIGHT] and man.x<screen_width -man.rec_width -man.velocity:
        man.x+=man.velocity
        bgX -= 61
        bgX2 -= 61
        if bgX < bg.get_width() * -1:
            bgX = bg.get_width()
    
        if bgX2 < bg.get_width() * -1:
            bgX2 = bg.get_width()

        man.right=True
        man.left=False
        man.standing=False
    else:
        man.standing=True
        man.walkCount=0
    
    if not(man.isJump):
        '''if keys[pygame.K_UP] and y>velocity:
            y-=velocity
        if keys[pygame.K_DOWN] and y<screen_height -rec_height -velocity:
            y+=velocity'''
        if keys[pygame.K_UP]:
            man.isJump=True
            man.left=False
            man.right=False
            man.walkCount=0

    else:
        if man.jumpCount>=-10:
            neg=1
            if man.jumpCount<0:
                neg=-1
            man.y-= (man.jumpCount**2)*0.5*neg
            man.jumpCount-=1
        else:
            man.isJump=False
            man.jumpCount=10

    clock.tick(27)

pygame.quit()
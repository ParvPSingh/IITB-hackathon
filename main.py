import pygame
from Player import Player
pygame.init()

screen_width=610
screen_height=347
window=pygame.display.set_mode((screen_width,screen_height))

pygame.display.set_caption('SPACE PLUMBER')

bg = pygame.image.load(('space corridor.jpg')).convert()
bgX = bg.get_width()
stage_width=bgX*3
stage_posX=0
start_scrolling_posX=screen_width/2

clock=pygame.time.Clock()

def redraw_GameWindow():
    relX=stage_posX%bgX
    window.blit(bg, (relX-bgX, 0))
    if relX<screen_width:
        window.blit(bg, (relX, 0))
    man.draw(window)
    #pygame.draw.rect(window, (255,0,0), (square_posX, man.y, man.rec_width, man.rec_height))
    #pygame.display.flip()
    pygame.display.update()

man=Player(30,281,30,30)
'''square_side=man.rec_width
square_posX=man.rec_width'''
#man.x=man.rec_width

run=True
while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False

    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        man.velocity=-7.5
        man.left=True
        man.right=False
        man.standing=False
    elif keys[pygame.K_RIGHT]:
        man.velocity=7.5
        man.right=True
        man.left=False
        man.standing=False
    else:
        man.velocity=0
        man.standing=True
        man.walkCount=0
    man.x+=man.velocity

    if man.x>stage_width-man.square_side:
        man.x=stage_width-man.square_side
    if man.x<0:
        man.x=0

    if man.x<start_scrolling_posX:
        man.square_posX=man.x
    elif man.x>stage_width-start_scrolling_posX:
        man.square_posX=man.x+screen_width-stage_width
    else:
        man.square_posX=start_scrolling_posX
        stage_posX+= (-man.velocity)

    
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

    redraw_GameWindow()

pygame.quit()
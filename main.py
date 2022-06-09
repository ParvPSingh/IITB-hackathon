from random import random
import pygame
from Platforms import *
from Platform import Platform
from Player import *
from Levels import Levels
pygame.init()

screen_width=1072
screen_height=603
window=pygame.display.set_mode((screen_width,screen_height))

pygame.display.set_caption('SPACE PLUMBER')

bgFirst = pygame.image.load(('level 1 background first image.png')).convert()
bg = pygame.image.load(('level 1 background.png')).convert()
bgX = bg.get_width()
stage_width= bgX*2
stage_posX=0
start_scrolling_posX=screen_width/2

#plat_list = Levels.platform(1)
platefarms = [Platform(200, 300), Platform(400, 400), Platform(700, 500), Platform(900, 300), Platform(2000, 100)]

clock=pygame.time.Clock()

def redraw_GameWindow():
    if man.x<screen_width+20:
        relX=stage_posX%bgX
        window.blit(bgFirst, (relX-bgX, 0))
        if relX<screen_width:
            window.blit(bgFirst, (relX, 0))
    else:
        relX=stage_posX%bgX
        window.blit(bg, (relX-bgX, 0))
        if relX<screen_width:
            window.blit(bg, (relX, 0))
    
    for plate in plates.container:
            plate.draw(window)

    man.draw(window)
    pygame.draw.rect(window, (255,0,0), (man.square_posX, man.y, man.rec_width, man.rec_height))
    pygame.display.flip()
    pygame.display.update()

man=Player(30,480,100,110)
'''plates=Platforms()
for i in range(0,50):
    plates.add(Platform(randint(0,stage_width),randint(60,300),237,22))
#plates.add(Platform(30,380,237,22))'''
plates=Platforms()

run=True
while run:
    clock.tick(27)

    #plat_list.draw(window)
    plates.testCollision(man)


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
    '''if man.current_platform:
        if not man.current_platform.test(man):
            #man.falling=True
            man.current_platform=None'''

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
        for plate in plates.container:
            plate.x+= (-man.velocity)

    
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
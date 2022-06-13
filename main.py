import pygame
import sys
from Button import Button
from Platforms import *
from Player import *
from Projectile import Projectile
from Enemy import *
pygame.init() #initialising pygame

screen_width=1072
screen_height=603
window=pygame.display.set_mode((screen_width,screen_height)) #setting up window

BG = pygame.image.load("assets/Background.png")

def get_font(size):
    return pygame.font.Font("assets/font.ttf", size) #font initialising

#main play function starts
def play():
    while True:

        #window.fill("black")

        #loading all the images and sounds
        bulletSound = pygame.mixer.Sound('poop gun.mp3')
        hitSound = pygame.mixer.Sound('robot hit.wav')
        robot_dieSound = pygame.mixer.Sound('power-down.mp3')

        music = pygame.mixer.music.load('GALACTIC_FILMSTRO.mp3')
        pygame.mixer.music.play(-1)

        dead_robot = pygame.image.load(('assets/der6.png')).convert()

        global score
        score = 0

        screen_width=1072
        screen_height=603
        window=pygame.display.set_mode((screen_width,screen_height))

        pygame.display.set_caption('SPACE PLUMBER')

        #setting up all the window variables
        bg = pygame.image.load(('level 1 background.png')).convert()
        bgX = bg.get_width()
        stage_width= bgX*8
        stage_posX=0
        start_scrolling_posX=screen_width/2

        clock=pygame.time.Clock()

        #main draw function for all classes
        def redraw_GameWindow():
            relX=stage_posX%bgX
            window.blit(bg, (relX-bgX, 0))
            if relX<screen_width:
                window.blit(bg, (relX, 0))

            for bullet in bullets:
                bullet.draw(window)
            text = font.render('Score: ' + str(score), 1, (0,0,0))
            window.blit(text, (350, 10))
            #plates.draw(window)
            man.draw(window)
            #robot.draw(window)
            for robo in robots:
                robo.draw(window)
            pygame.display.flip()
            pygame.display.update()

        #setting up instances of all classes
        man=Player(30,480,110,110)
        font = pygame.font.SysFont('comicsans', 30, True)
        #robot = Enemy(780, 480, 110, 110, 980)
        #plates=Platforms()
        shootLoop = 0
        bullets = []
        robots=[Enemy(300, 480, 110, 110, man.square_posX, man.square_posX+200), Enemy(6500, 480, 110, 110, man.square_posX, man.square_posX+500), Enemy(5500, 480, 110, 110, man.square_posX, man.square_posX+350), Enemy(5000, 480, 110, 110, man.square_posX, man.square_posX+400), Enemy(7500, 480, 110, 110, man.square_posX, man.square_posX+250), Enemy(6000, 480, 110, 110, man.square_posX, man.square_posX+300), Enemy(8000, 480, 110, 110, man.square_posX, man.square_posX+700), Enemy(5000, 480, 110, 110, man.square_posX, man.square_posX+600), Enemy(6000, 480, 110, 110, man.square_posX, man.square_posX+300), Enemy(6500, 480, 110, 110, man.square_posX, man.square_posX+500), Enemy(7000, 480, 110, 110, man.square_posX, man.square_posX+300), Enemy(1000, 480, 110, 110, man.square_posX, 550), Enemy(780, 480, 110, 110, man.square_posX, 1200), Enemy(2400, 480, 110, 110, man.square_posX, 980), Enemy(1880, 480, 110, 110, man.square_posX, 2180), Enemy(4500, 480, 110, 110, man.square_posX, 3480), Enemy(4500, 480, 110, 110, man.square_posX, 6800), Enemy(6900, 480, 110, 110, man.square_posX, 5800), Enemy(6300, 480, 110, 110, man.square_posX, 7600), Enemy(8000, 480, 110, 110, man.square_posX, 7500)]

        #main loop for game starts
        run=True
        while run:
            clock.tick(27)

            #plates.testCollision(man) was going to use this for the platforms

            #for quitting the game
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    run=False

            #to check if a robot touches the astronaut
            for robo in robots:
                if robo.visible == True:
                    if man.hitbox[1] < robo.hitbox[1] + robo.hitbox[3] and man.hitbox[1] + man.hitbox[3] > robo.hitbox[1]:
                        if man.hitbox[0] + man.hitbox[2] > robo.hitbox[0] and man.hitbox[0] < robo.hitbox[0] + robo.hitbox[2]:
                            man.hit(window)
                            #score -= 5
                else:
                    #initially plan was to blit a broken robot once it's popped from that position
                    derX=robo.x
                    derY=robo.y
                    window.blit(dead_robot, (derX, derY))
                    robots.pop(robots.index(robo))
                    
            #To set a limit of number of bullets to be appended at once
            if shootLoop > 0:
                shootLoop += 1
            if shootLoop > 3:
                shootLoop = 0
            
            #to check if a bullet hits a robot and to pop them from the list once their work is over
            for robo in robots:
                for bullet in bullets:
                    if bullet.y - bullet.hw < robo.hitbox[1] + robo.hitbox[3] and bullet.y + bullet.hw > robo.hitbox[1]:
                        if bullet.x + bullet.hw > robo.hitbox[0] and bullet.x - bullet.hw < robo.hitbox[0] + robo.hitbox[2]:
                            hitSound.play()
                            robo.hit()
                            score += 1
                            if len(bullets)!=0:
                                bullets.pop(bullets.index(bullet))
                            else:
                                pass
            
            for bullet in bullets:        
                if bullet.x < screen_width and bullet.x > 0:
                    bullet.x += bullet.vel
                else:
                    bullets.pop(bullets.index(bullet))

            #to do something once a key is pressed
            keys=pygame.key.get_pressed()

            if keys[pygame.K_SPACE] and shootLoop == 0:
                bulletSound.play()
                if man.left:
                    facing = -1
                else:
                    facing = 1
                    
                if len(bullets) < 10:
                    bullets.append(Projectile(round(man.square_posX + man.rec_width //2), round(man.y + man.rec_height//2), 17.5, (0,0,0), facing))

                shootLoop = 1

            if keys[pygame.K_LEFT]:
                if keys[pygame.K_UP]:
                    man.velocity=-15
                    man.left=True
                    man.right=False
                    man.standing=False
                else:
                    man.velocity=-8
                    man.left=True
                    man.right=False
                    man.standing=False
            elif keys[pygame.K_RIGHT]:
                if keys[pygame.K_UP]:
                    man.velocity=15
                    man.right=True
                    man.left=False
                    man.standing=False
                else:
                    man.velocity=8
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

            #to set the range for astronaut
            if man.x>stage_width-man.square_side:
                man.x=stage_width-man.square_side
                run=False
            if man.x<0:
                man.x=0

            #to set background scrolling and the player's position on one place
            if man.x<start_scrolling_posX:
                man.square_posX=man.x
            elif man.x>stage_width-start_scrolling_posX:
                man.square_posX=man.x+screen_width-stage_width
            else:
                man.square_posX=start_scrolling_posX
                stage_posX+= (-man.velocity)
                for robo in robots:
                    robo.x+= (-man.velocity)
                '''for plate in plates.container:
                    plate.x1+= (-man.velocity)'''

            #jump function
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
                    man.y-= (man.jumpCount**2)*0.8*neg
                    man.jumpCount-=1
                else:
                    man.isJump=False
                    man.falling=True
                    man.jumpCount=10

            redraw_GameWindow()
        end_screen() #gives the end screen
    

def end_screen():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        window.fill((255,255,255,0.2))

        OPTIONS_TEXT = get_font(55).render('THE END', True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        window.blit(OPTIONS_TEXT, OPTIONS_RECT)
        #window.blit(howtoplay,(20,20))

        OPTIONS_BACK = Button(image=None, pos=(1000, 580), 
                            text_input="BACK", font=get_font(25), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(window)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()
    
#gives options screen
def options():
    while True:
        howtoplay = pygame.image.load(('assets/How to play.png')).convert()
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        window.fill("white")

        window.blit(howtoplay,(20,20))

        OPTIONS_BACK = Button(image=None, pos=(1000, 580), 
                            text_input="BACK", font=get_font(25), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(window)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()

#gives menu screen
def main_menu():
    music = pygame.mixer.music.load('assets/main_menu_music.mp3')
    pygame.mixer.music.play(-1)
    while True:
        
        window.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(750, 300), 
                            text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(750, 425), 
                            text_input="HOW TO PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(750, 550), 
                            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        window.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(window)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()
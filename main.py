import pygame
import sys
from Button import Button
from Platforms import *
from Player import *
from Projectile import Projectile
from Enemy import Enemy
pygame.init()

screen_width=1072
screen_height=603
window=pygame.display.set_mode((screen_width,screen_height))

BG = pygame.image.load("assets/Background.png")

def get_font(size):
    return pygame.font.Font("assets/font.ttf", size)

def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        #window.fill("black")

        bulletSound = pygame.mixer.Sound('poop gun.mp3')
        hitSound = pygame.mixer.Sound('robot hit.wav')
        #robot_dieSound = pygame.mixer.Sound('power-down.mp3')

        music = pygame.mixer.music.load('GALACTIC_FILMSTRO.mp3')
        pygame.mixer.music.play(-1)

        score = 0

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

            for bullet in bullets:
                bullet.draw(window)
            text = font.render('Score: ' + str(score), 1, (0,0,0))
            window.blit(text, (350, 10))
            #plates.draw(window)
            man.draw(window)
            robot.draw(window)
            pygame.display.flip()
            pygame.display.update()

        man=Player(30,480,110,110)
        font = pygame.font.SysFont('comicsans', 30, True)
        robot = Enemy(780, 480, 110, 110, 980)
        #plates=Platforms()
        shootLoop = 0
        bullets = []

        run=True
        while run:
            clock.tick(27)

            #plates.testCollision(man)

            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    run=False

            if robot.visible == True:
                if man.hitbox[1] < robot.hitbox[1] + robot.hitbox[3] and man.hitbox[1] + man.hitbox[3] > robot.hitbox[1]:
                    if man.hitbox[0] + man.hitbox[2] > robot.hitbox[0] and man.hitbox[0] < robot.hitbox[0] + robot.hitbox[2]:
                        man.hit(window)
                        score -= 5

            if shootLoop > 0:
                shootLoop += 1
            if shootLoop > 3:
                shootLoop = 0
            
            for bullet in bullets:
                if bullet.y - bullet.radius < robot.hitbox[1] + robot.hitbox[3] and bullet.y + bullet.radius > robot.hitbox[1]:
                    if bullet.x + bullet.radius > robot.hitbox[0] and bullet.x - bullet.radius < robot.hitbox[0] + robot.hitbox[2]:
                        hitSound.play()
                        robot.hit()
                        score += 1
                        bullets.pop(bullets.index(bullet))
                        
                if bullet.x < screen_width and bullet.x > 0:
                    bullet.x += bullet.vel
                else:
                    bullets.pop(bullets.index(bullet))

            keys=pygame.key.get_pressed()

            if keys[pygame.K_SPACE] and shootLoop == 0:
                bulletSound.play()
                if man.left:
                    facing = -1
                else:
                    facing = 1
                    
                if len(bullets) < 5:
                    bullets.append(Projectile(round(man.x + man.rec_width //2), round(man.y + man.rec_height//2), 6, (0,0,0), facing))

                shootLoop = 1

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
                robot.x+= (-man.velocity)
                '''for plate in plates.container:
                    plate.x1+= (-man.velocity)'''

            
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
                    man.falling=True
                    man.jumpCount=10

            redraw_GameWindow()

        PLAY_BACK = Button(image=None, pos=(20, 20), 
                            text_input="BACK", font=get_font(25), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(window)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

        pygame.display.update()
        pygame.quit()
        sys.exit()
    
def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        window.fill("white")

        OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        window.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

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

def main_menu():
    music = pygame.mixer.music.load('assets/main_menu_music.mp3')
    pygame.mixer.music.play(-1)
    while True:
        
        window.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 250), 
                            text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 400), 
                            text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 550), 
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
import pygame
pygame.init()

window=pygame.display.set_mode((612,310))
pygame.display.set_caption('SPACE PLUMBER')
bg = pygame.image.load('space corridor.jpg')
window.blit(bg, (0,0))
pygame.display.update()

#boom chika

run=True
while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False

pygame.quit()


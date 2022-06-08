import pygame

platform_images = [pygame.image.load('platform tri edges.png'), pygame.image.load('platform rectangle.png')]

class Platforms():
    def __init__(self) -> None:
        self.container=list([])

    def add(self,p):
        self.container.append(p)

    def testCollision(self,Player):
        if not Player.falling:
            return False
        for p in self.container:
            result =p.test(Player)
            if result:
                Player.current_platform = result
                Player.y=result.y
                Player.falling = False
                return True
            return False

    def draw(self,window):
        display=pygame.display.get_surface()
        for p in self.container:
            window.blit(platform_images[0],(p.x1,p.y1))

    def do(self,Player,window):
        self.testCollision(Player)
        self.draw(window)
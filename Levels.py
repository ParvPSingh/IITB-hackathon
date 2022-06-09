import pygame
from Platform import *

class Levels():
    def platform( lvl ):
        plat_list = []
        if lvl == 1:
            plat = Platform(200, 300)
            plat_list.append(plat)
            plat = Platform(500, 340)
            plat_list.append(plat)
        if lvl == 2:
            print("Level " + str(lvl) )
        
        return plat_list
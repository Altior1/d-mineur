######## les imports #########
import pygame
from pygame.locals import *
import mines
import random

####### initialisation ######
pygame.init()

######" les constantes" ####
WIDHTSCREEN = 1200
HEIGHTSCREEN = 800

#### affichage écran ######



#### fonction d'initialisation du jeu #####
def madePlateau(tailleX, tailleY, n):
    listeMine = []
    for i in range(n):
        x=random.randint(0,HEIGHTSCREEN)
        y=random.randint(0,WIDHTSCREEN)
        mine = mines.Mines(x,y)
        listeMine.append(mine)
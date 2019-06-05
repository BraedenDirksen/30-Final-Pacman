'''
title: PyGame Template
author: micheal zhang
date: 2019-04-08
'''
import pygame, random
from myClass import *
pygame.init() # loads the pygame module comands in the program

# display variables
TITLE = "PacMan" # title that appears in the window title
FPS = 30
WIDTH = 928
HEIGHT = 1024
SCREENDIM = (WIDTH, HEIGHT)

# color variables
WHITE = (255,255,255)
BLACK = (0,0,0)
GREY = (50,50,50)

# Create the window
screen = pygame.display.set_mode(SCREENDIM)
# creates main surface where all other assets are placed on top
pygame.display.set_caption(TITLE) # updates window title to "TITLE"
screen.fill(BLACK) # fills the entire surface with "GREY"
clock = pygame.time.Clock() # starts a clock object to measure time


#--- code starts here ---#

ghosts = []
hitBoxes = []
pacman = player(50,50,"shtuff/pacman.png",WIDTH/2-25,HEIGHT/2+40)
background = mySprite("shtuff/maze.png")
#pacman = player(50,50,"C:/Users/socce/Documents/VS CODE/30-Final-Pacman/shtuff/pacman.png",WIDTH/2-25,HEIGHT/2+40)
#background = mySprite("C:/Users/socce/Documents/VS CODE/30-Final-Pacman/shtuff/maze.png")
for i in range(1):
    ghosts.append(ghost(50,50,WIDTH/2-25,HEIGHT/2-150))#,WIDTH/2-85+(60* i),HEIGHT/2-55))

hitBoxSize = 15
hitBoxlength = 50
for i in range(len(ghosts)):
        hitBoxes.append([box(hitBoxSize,hitBoxlength,0),box(hitBoxSize,hitBoxlength,1),box(hitBoxSize,hitBoxlength,2),box(hitBoxSize,hitBoxlength,3)])
    
running = True
while running:
    for event in pygame.event.get(): # returns all inputs amd triggers into an array
        if event.type == pygame.QUIT:
            running = False
    screen.fill(BLACK)
    pressedKeys = pygame.key.get_pressed()
    screen.blit(background.surface,background.getPos())

    pacman.playerDirections()
    pacman.mapCollision(background)
    pacman.playerMove(pressedKeys,player,background)
    screen.blit(pacman.surface,pacman.getPos())


    for i in range(len(ghosts)):
        ghosts[i].getOpenClose(hitBoxes[i],background)
        ghosts[i].choseDir()
        ghosts[i].checkSides(hitBoxes[i],background)
        ghosts[i].movement(hitBoxes[i],background)
        ghosts[i].directions()
        screen.blit(ghosts[i].surface,ghosts[i].getPos())
        for j in range(4):
            hitBoxes[i][j].follow(ghosts[i])
            screen.blit(hitBoxes[i][j].surface,hitBoxes[i][j].getPos())


    clock.tick(FPS) # pause the game until the FPS time is reached
    pygame.display.flip() # update the screen with changes
pygame.quit()
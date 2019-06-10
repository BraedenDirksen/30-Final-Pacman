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
pellets = [] #25 X 26 
pacman = player(50,50,"shtuff/pacman.png",WIDTH/2-25,HEIGHT/2+40)
background = mySprite("shtuff/maze.png")
#pacman = player(50,50,"C:/Users/socce/Documents/VS CODE/30-Final-Pacman/shtuff/pacman.png",WIDTH/2-25,HEIGHT/2+40)
#background = mySprite("C:/Users/socce/Documents/VS CODE/30-Final-Pacman/shtuff/maze.png")
for i in range(3):
    ghosts.append(ghost(50,50,WIDTH/2-25,HEIGHT/2-150))#,WIDTH/2-85+(60* i),HEIGHT/2-55))

hitBoxSize = 65
hitBoxlength = 50
for i in range(len(ghosts)):
        hitBoxes.append([box(hitBoxSize,hitBoxlength,0),box(hitBoxSize,hitBoxlength,1),box(hitBoxSize,hitBoxlength,2),box(hitBoxSize,hitBoxlength,3)])

for i in range(29):
    pellets.append([])
    for j in range(26):
        pellets[i].append(pellet(7.5,7.5,55+(32.5*j),55+(32.5*i)))

PelletsPosRemove = [(88, 91), (122, 91), (155, 91), (186, 91), (189, 120), (154, 123), (121, 127), (90, 157), (86, 123), (120, 154), (156, 157), (181, 155), (251, 155), (253, 121), (288, 88), (256, 89), (279, 121), (316, 88), (350, 94), (379, 90), (382, 126), (381, 150), (348, 152), (355, 117), (315, 127), (319, 151), (284, 157)]


running = True
while running:
    for k in range(len(PelletsPosRemove)):
        for i in range(len(pellets)):
            for j in range(len(pellets[i])):
                if getSpriteCollision(PelletsPosRemove[k],pellets[i][j].getPos()):
                    pellets[i].pop(j)
                    break
    for event in pygame.event.get(): # returns all inputs amd triggers into an array
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            for i in range(len(pellets)):
                for j in range(len(pellets[i])):
                    if getSpriteCollision(pellets[i][j].getPos(), pygame.mouse.get_pos()):
                        PelletsPosRemove.append(pygame.mouse.get_pos())
                        pellets[i].pop(j)
                        break

    screen.fill(BLACK)
    pressedKeys = pygame.key.get_pressed()
    screen.blit(background.surface,background.getPos())

    pacman.playerDirections()
    pacman.mapCollision(background)
    pacman.playerMove(pressedKeys,player,background)
    screen.blit(pacman.surface,pacman.getPos())

    for i in range(len(ghosts)):
        ghosts[i].movement(hitBoxes[i],background)
        ghosts[i].directions()
        for j in range(4):
            hitBoxes[i][j].follow(ghosts[i])
            hitBoxes[i][j].mapCollision(background)
            #screen.blit(hitBoxes[i][j].surface,hitBoxes[i][j].getPos())
        screen.blit(ghosts[i].surface,ghosts[i].getPos())
    
    for i in range(len(pellets)):
        for j in range(len(pellets[i])):
            screen.blit(pellets[i][j].surface,pellets[i][j].getPos())
            if pellets[i][j].getCollision(pacman) == True:
                pellets[i].pop(j)
                break

    clock.tick(FPS) # pause the game until the FPS time is reached
    pygame.display.flip() # update the screen with changes
print(PelletsPosRemove)
pygame.quit()
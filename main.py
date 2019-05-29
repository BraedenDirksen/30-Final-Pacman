'''
title: PyGame Template
author: micheal zhang
date: 2019-04-08
'''
import pygame
from myClass import *
pygame.init() # loads the pygame module comands in the program

# display variables
TITLE = "hello world" # title that appears in the window title
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


pacman = player(50,50,"shtuff/pacman.png",WIDTH/2-25,HEIGHT/2+40)
background = mySprite("shtuff/maze.png")
ghost = ghost(50,50,WIDTH/2-25,HEIGHT/2-25)
running = True
while running:
    for event in pygame.event.get(): # returns all inputs amd triggers into an array
        if event.type == pygame.QUIT:
            running = False
    screen.fill(BLACK)
    pressedKeys = pygame.key.get_pressed()
    screen.blit(background.surface,background.getPos())

    pacman.playerMove(pressedKeys,player,background)
    pacman.mapCollision(background)
    pacman.playerDirections()
    screen.blit(pacman.surface,pacman.getPos())

    screen.blit(ghost.surface,ghost.getPos)

    clock.tick(FPS) # pause the game until the FPS time is reached
    pygame.display.flip() # update the screen with changes
pygame.quit()
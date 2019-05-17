'''
title: PyGame Template
author: micheal zhang
date: 2019-04-08
'''
import pygame
pygame.init() # loads the pygame module comands in the program

# display variables
TITLE = "hello world" # title that appears in the window title
FPS = 30
WIDTH = 800
HEIGHT = 600
SCREENDIM = (WIDTH, HEIGHT)

# color variables
WHITE = (255,255,255)
BLACK = (0,0,0)
GREY = (50,50,50)

# Create the window
screen = pygame.display.set_mode(SCREENDIM)
# creates main surface where all other assets are placed on top
pygame.display.set_caption(TITLE) # updates window title to "TITLE"
screen.fill(GREY) # fills the entire surface with "GREY"
clock = pygame.time.Clock() # starts a clock object to measure time

#--- code starts here ---#
running = True
while running:
    for event in pygame.event.get(): # returns all inputs amd triggers into an array
        if event.type == pygame.QUIT:
            running = False

    clock.tick(FPS) # pause the game until the FPS time is reached
    pygame.display.flip() # update the screen with changes
pygame.quit()
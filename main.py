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
#pacman = player(50,50,"shtuff/pacman.png",WIDTH/2-25,HEIGHT/2+40)
#background = mySprite("shtuff/maze.png")
pacman = player(50,50,"C:/Users/socce/Documents/VS CODE/30-Final-Pacman/shtuff/pacman.png",WIDTH/2-25,HEIGHT/2+40)
background = mySprite("C:/Users/socce/Documents/VS CODE/30-Final-Pacman/shtuff/maze.png")
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
# this is all the pellets in those positions need to be removed
PelletsPosRemove = [(88, 91), (122, 91), (155, 91), (186, 91), (189, 120), (154, 123), (121, 127), (90, 157), (86, 123), (120, 154), (156, 157), (181, 155), (251, 155), (253, 121), (288, 88), (256, 89),
(279, 121), (316, 88), (350, 94), (379, 90), (382, 126), (381, 150), (348, 152), (355, 117), (315, 127), (319, 151), (284, 157), (289, 94), (322, 123), (347, 124), (349, 89), (384, 121), (253, 90), (125, 124), (479, 90), (480, 61), (446, 61), (448, 89), (448, 153), (448, 187), (447, 219), (415, 221), (382, 220), (352, 222), (350, 251), (380, 254), (416, 256), (448,
252), (477, 254), (515, 254), (541, 253), (541, 221), (481, 221), (512, 222), (479, 191), (479, 158), (481, 285), (446, 285), (448, 318), (481, 318), (482, 353), (450, 349), (445, 412), (409, 417), (385, 413), (349, 420), (353, 445), (350, 482), (348, 515), (349, 541), (382, 541), (414, 546), (449, 545), (478, 546), (513, 548), (541, 549), (577, 544), (575, 513), (578, 483), (578, 451), (577, 416), (547, 418), (515, 418), (482, 416), (479, 448), (450, 451), (416, 452), (382, 447), (382, 479), (417, 481), (414, 513), (383, 514), (450, 517), (450,
481), (477, 479), (483, 513), (512, 514), (513, 480), (513, 449), (543, 450), (546, 480), (546, 511), (577, 608), (546, 608), (515, 611), (479, 610), (448, 609), (415, 612), (386, 609), (353, 609), (350, 644), (385, 644), (418, 643), (448, 645), (478, 641), (512, 642), (544, 642), (577, 645), (635, 643), (674, 640), (672, 613), (645, 611), (642, 574), (637, 547), (641, 478), (644, 516), (642, 447), (644, 415), (673, 416), (676, 450), (676, 480), (676, 510), (674, 548), (676, 349), (676, 316), (673, 282), (673, 251), (642, 255), (643, 285), (642,
319), (644, 351), (611, 349), (609, 317), (577, 318), (544, 320), (546, 352), (576, 351), (577, 256), (576, 213), (547, 152), (546, 123), (545, 91), (579, 90), (614, 92), (640, 90), (641, 120), (608, 120), (576, 125), (579, 153), (615, 154), (645, 156), (676, 157), (675, 122), (671, 92), (742, 93), (774, 89), (806, 90), (835, 90), (833, 125), (805, 126), (737, 126), (775, 126), (742, 153), (770, 157), (804, 155), (839, 157), (839, 220), (805, 218), (770, 221), (743, 220), (676, 223), (640, 218), (739, 252), (772, 257), (804, 257), (839, 254), (841, 320), (838, 349), (873, 352), (870, 321), (776, 320), (740, 320), (740, 352), (772, 352), (766, 381), (737, 380), (744, 414), (738, 451), (770, 443), (776, 413), (798, 411), (836, 419), (837, 448), (806, 448), (383, 317), (379, 351), (351, 353), (318, 320), (350, 316), (313, 349), (287, 349), (284, 313), (285, 286), (287, 251), (282, 219), (254, 221), (254, 246), (253, 285), (255, 320), (252, 346), (188, 249), (155, 220), (185, 221), (121, 222), (92, 221), (94, 255), (123, 254), (152, 253), (156, 317), (188, 319), (153, 352), (154, 384), (156, 413), (148, 447), (120, 445), (120, 415), (191, 450), (189, 413), (187, 381), (186, 347), (94, 348), (88, 319), (53, 317), (59, 349), (285, 91), (318, 122), (609, 90), (610, 158), (740, 91), (739, 123), (773, 125), (808, 125), (739, 415), (776, 417), (740, 450), (739, 512), (641, 514), (578, 480), (576, 448), (545, 414), (510, 417), (449, 450), (416, 448), (444, 514), (480, 513), (350, 446), (344, 412), (283, 414), (249, 414), (256, 446), (281, 450), (278, 479), (187, 445), (90, 351), (479, 187), (479, 55), (415, 250), (838, 321), (869, 320), (865, 350), (773, 320), (775, 252), (803, 252), (737, 222), (672, 220), (580, 253), (773, 513), (810, 512), (514, 543), (349, 611), (385, 609), (413, 640), (547, 547), (279, 515), (254,
514), (255, 544), (252, 581), (255, 609), (282, 609), (286, 576), (252, 478), (284, 546), (190, 648), (158, 641), (157, 609), (183, 608), (188, 579), (151, 580), (160, 542), (124, 546), (92, 546), (93, 512), (124, 516), (150, 517), (188, 511), (192, 544), (90, 448), (87, 417), (52, 612), (79, 613), (82, 644), (60, 646), (93, 714), (93, 740), (123, 735), (124, 711),
(153, 709), (153, 740), (184, 741), (183, 710), (155, 773), (156, 802), (155, 832), (185, 832), (183, 805), (186, 773), (181, 898), (185, 934), (161, 934), (156, 907), (122, 901), (93, 900), (91, 934), (121, 932), (87, 841), (86, 809), (60, 805), (59, 832), (259, 705), (258, 642), (284, 642), (280, 709), (278, 734), (256, 742), (316, 706), (317, 736), (348, 738), (351, 711), (378, 705), (381, 740), (448, 711), (477, 709), (481, 744), (477, 779), (477, 807), (477, 841), (475, 868), (477, 894), (451, 901), (452, 867), (452, 837), (448, 801), (449,
770), (449, 741), (415, 824), (414, 812), (382, 805), (384, 838), (352, 807), (351, 837), (282, 807), (256, 804), (255, 833), (252, 868), (250, 904), (250, 935), (282, 927), (312, 933), (349, 934), (376, 935), (374, 906), (349, 907), (323, 909), (291, 905), (281, 870), (280, 839), (504, 805), (512, 832), (542, 835), (549, 809), (570, 806), (572, 838), (548, 908), (550, 930), (574, 932), (476, 930), (450, 932), (579, 902), (605, 905), (637, 910), (645, 868), (650, 843), (646, 809), (676, 812), (672, 840), (672, 901), (675, 874), (670, 932), (646,
937), (608, 934), (745, 901), (745, 930), (770, 936), (776, 900), (803, 907), (808, 933), (835, 933), (837, 907), (838, 838), (842, 807), (865, 808), (871, 843), (775, 835), (775, 804), (774, 771), (775, 746), (743, 745), (743, 775), (740, 810), (740, 834), (743, 711), (775, 709), (806, 712), (805, 734), (839, 741), (838, 706), (838, 640), (839, 611), (870, 642), (867, 614), (770, 641), (746, 640), (742, 606), (745, 578), (744, 549), (774, 549), (773, 568), (771, 614), (805, 540), (834, 541), (834, 513), (682, 578), (546, 708), (543, 742), (578,
734), (576, 707), (609, 710), (610, 733), (642, 732), (643, 712), (673, 705), (671, 733)]

for k in range(len(PelletsPosRemove)):
    for i in range(len(pellets)):
        for j in range(len(pellets[i])):
            try:
                if getSpriteCollision(PelletsPosRemove[k],pellets[i][j].getPos()):
                    pellets[i].pop(j)
            except IndexError:
                pass

score = 0
go = 0
running = True
while running:

    for event in pygame.event.get(): # returns all inputs amd triggers into an array
        if event.type == pygame.QUIT:
            running = False
    if go == 0:

        screen.fill(BLACK)
        pressedKeys = pygame.key.get_pressed()
        screen.blit(background.surface,background.getPos())

        pacman.playerDirections()
        pacman.mapCollision(background)
        pacman.playerMove(pressedKeys,player,background)
        screen.blit(pacman.surface,pacman.getPos())
        for i in range(len(ghosts)):
            if pacman.ghostCollision(ghosts[i]):
                go = 1
                win = False

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
                    score += 1
                    scorePrint = text(str(score))
                    break
        screen.blit(scorePrint.surface,(15,960))
        if score == 331:
            go = 1
            win = True

        clock.tick(FPS) # pause the game until the FPS time is reached
        pygame.display.flip() # update the screen with changes
    else:
        for event in pygame.event.get(): # returns all inputs amd triggers into an array
            if event.type == pygame.QUIT:
                running = False

        if win == False:
            screen.blit(text("YOU LOSE").surface,(WIDTH/2-125,HEIGHT/2-75))
        else:
            screen.blit(text("YOU WIN").surface,(WIDTH/2-115,HEIGHT/2-75))
        clock.tick(FPS) # pause the game until the FPS time is reached
        pygame.display.flip() # update the screen with changes

pygame.quit()
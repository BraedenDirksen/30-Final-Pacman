'''
title my sprite classes
author braeden dirksen
date created 2019-04-15
'''
import pygame
class myClass:
    import pygame
    def __init__(self,color = (0,0,0),x = 0,y = 0):
        self.surface = pygame.Surface((0,0),pygame.SRCALPHA)
        self.red = 0
        self.green = 0
        self.blue = 0
        self.color = color

class text(myClass):
    def __init__(self, content, font = 'Arial', fontSize = 24):
        myClass.__init__(self)
        self.fontFam = font
        self.fontSize = fontSize
        self.font = pygame.font.SysFont(self.fontFam,self.fontSize)
        self.content = content
        self.surface = self.font.render(self.content,1,self.color)

class mySprite(myClass):
    def __init__(self,fileName):
        myClass.__init__(self)
        self.surface = self.pygame.image.load(fileName).convert_alpha()
        self.surface = pygame.transform.scale(self.surface, (928,1024))
        self.mask = pygame.mask.from_surface(self.surface)
        self.x = 0
        self.y = 0
        self.pos = (self.x,self.y)
    def getPos(self):
        return self.pos

class player(myClass):
    def __init__(self,height,width,fileName,x=0,y=0,color = (0,0,0),dirx=1,diry=1):
        myClass.__init__(self,color)
        self.height = height 
        self.width = width 
        self.surface = self.pygame.image.load(fileName).convert_alpha()
        self.surface = pygame.transform.scale(self.surface, (self.width,self.height))
        self.mask = pygame.mask.from_surface(self.surface)
        self.spd = 5
        self.xDir = dirx
        self.yDir = diry
        self.spdX = self.spd
        self.spdY = self.spd
        self.x = x
        self.y = y 
        self.pos = (self.x,self.y)
        self.facing = "right"
        self.moving = "right"
    def getPos(self):
        return self.pos
    def getWidth(self):
        return self.width
    def getHeight(self):
        return self.height
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def playerMove(self,pressedKeys,sprite1,sprite2):
        if pressedKeys[pygame.K_a]:
            self.moving = "left"
            self.x -= self.spd
        elif pressedKeys[pygame.K_d]:
            self.moving = "right"
            self.x += self.spd
        elif pressedKeys[pygame.K_w]:
            self.moving = "up"
            self.y -= self.spd
        elif pressedKeys[pygame.K_s]:
            self.moving = "down"
            self.y += self.spd
            
        self.pos = (self.x,self.y)

    def mapCollision(self,sprite2):
        offset = int(sprite2.getPos()[0] - self.pos[0]),int(sprite2.getPos()[1] - self.pos[1])
        collisionPoint = self.mask.overlap(sprite2.mask,offset)
        if collisionPoint:
            if self.moving == "left":
                self.x += self.spd
            if self.moving == "right":
                self.x -= self.spd
            if self.moving == "up":
                self.y += self.spd
            if self.moving == "down":
                self.y -= self.spd


    def playerDirections(self):
        if self.facing == self.moving:
            pass
        elif self.facing == "right" and self.moving == "left":
            self.surface = pygame.transform.rotate(self.surface, 180)
        elif self.facing == "right" and self.moving == "up":
            self.surface = pygame.transform.rotate(self.surface, 90)
        elif self.facing == "right" and self.moving == "down":
            self.surface = pygame.transform.rotate(self.surface, 270)

        elif self.facing == "up" and self.moving == "down":
            self.surface = pygame.transform.rotate(self.surface, 180)
        elif self.facing == "up" and self.moving == "right":
            self.surface = pygame.transform.rotate(self.surface, 270)
        elif self.facing == "up" and self.moving == "left":
            self.surface = pygame.transform.rotate(self.surface, 90)

        elif self.facing == "left" and self.moving == "right":
            self.surface = pygame.transform.rotate(self.surface, 180)
        elif self.facing == "left" and self.moving == "up":
            self.surface = pygame.transform.rotate(self.surface, 270)
        elif self.facing == "left" and self.moving == "down":
            self.surface = pygame.transform.rotate(self.surface, 90)

        elif self.facing == "down" and self.moving == "up":
            self.surface = pygame.transform.rotate(self.surface, 180)
        elif self.facing == "down" and self.moving == "right":
            self.surface = pygame.transform.rotate(self.surface, 90)
        elif self.facing == "down" and self.moving == "left":
            self.surface = pygame.transform.rotate(self.surface, 270)
            
        self.facing = self.moving



class ghost(myClass):
    import random
    def __init__(self,height,width,x=0,y=0,color = (255,255,255),dirx=1,diry=1):
        myClass.__init__(self,color)
        self.height = height 
        self.width = width 
        self.dim = (self.width,self.height)
        self.surface = pygame.Surface(self.dim,pygame.SRCALPHA, 32)
        self.surface.fill(color)
        self.spd = 20
        self.facing = "right"
        self.moving = "right"
        self.x = x
        self.y = y 
        self.pos = (self.x,self.y)
    def getPos(self):
        return self.pos
    def getWidth(self):
        return self.width
    def getHeight(self):
        return self.height
    def getX(self):
        return self.x
    def getY(self):
        return self.y

    def move(self):
        dir = random.randrange(4)
        if dir == 0: #right
            self.x += self.spd
        elif dir == 1:# left
            self.x -= self.spd
        elif dir == 2: #down
            self.y += self.spd
        elif dir == 3: #up
            self.y -= self.spd
        

    def mapCollision(self,sprite2):
        offset = int(sprite2.getPos()[0] - self.pos[0]),int(sprite2.getPos()[1] - self.pos[1])
        collisionPoint = self.mask.overlap(sprite2.mask,offset)
        if collisionPoint:
            if self.moving == "left":
                self.x += self.spd
            if self.moving == "right":
                self.x -= self.spd
            if self.moving == "up":
                self.y += self.spd
            if self.moving == "down":
                self.y -= self.spd



















def getSpriteCollision(sprite1, sprite2):
    if sprite2.getX() <= sprite1.getX() + sprite1.getWidth() <= sprite2.getX() + sprite2.getWidth() + sprite1.getWidth() and sprite2.getY() <= sprite1.getY() + sprite1.getHeight() <= sprite2.getY() + sprite2.getHeight() + sprite1.getHeight():
        return True
    else:
        return False


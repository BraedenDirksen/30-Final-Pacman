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
        self.mask = pygame.mask.from_surface(self.surface)
        self.x = 0
        self.y = 0
        self.pos = (self.x,self.y)
    def getPos(self):
        return self.pos

class player(myClass):
    def __init__(self,height,width,x=0,y=0,color = (0,0,0),dirx=1,diry=1):
        myClass.__init__(self,color)
        self.height = height 
        self.width = width 
        self.dim = (self.width,self.height)
        self.surface = pygame.Surface(self.dim,pygame.SRCALPHA, 32)
        self.surface.fill(self.color)
        self.spd = 20
        self.xDir = dirx
        self.yDir = diry
        self.spdX = self.spd
        self.spdY = self.spd
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
    def playerMove(self,pressedKeys,WIDTH,):
        if pressedKeys[pygame.K_a]:
            self.x -= self.spd
        if pressedKeys[pygame.K_d]:
            self.x += self.spd
        if self.x <= 0:
            self.x += self.spd
        if self.x + self.width >= WIDTH:
            self.x -= self.spd
        self.pos = (self.x,self.y)

def ghost(myClass):
    def __init__(self,height,width,x=0,y=0,color = (0,0,0),dirx=1,diry=1):
        myClass.__init__(self,color)
        self.height = height 
        self.width = width 
        self.dim = (self.width,self.height)
        self.surface = pygame.Surface(self.dim,pygame.SRCALPHA, 32)
        self.surface.fill(self.color)
        self.spd = 20
        self.xDir = dirx
        self.yDir = diry
        self.spdX = self.spd
        self.spdY = self.spd
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
    def move(self,WIDTH,HEIGHT, spdX = 20, spdY = 20):
        pass

def getCollisionPoint(sprite1,sprite2):
    offset = (sprite2.getPos()[0] - sprite1.getPos()[0],sprite2.getPos()[1] - sprite1.getPos()[1]
    collisionPoint = sprite1.mask.overlap(sprite2.mask,offset)
    if collisionPoint:
        return True
    else:
        return False

def getSpriteCollision(sprite1, sprite2):
    if sprite2.getX() <= sprite1.getX() + sprite1.getWidth() <= sprite2.getX() + sprite2.getWidth() + sprite1.getWidth() and sprite2.getY() <= sprite1.getY() + sprite1.getHeight() <= sprite2.getY() + sprite2.getHeight() + sprite1.getHeight():
        return True
    else:
        return False


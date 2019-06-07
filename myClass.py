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
    def __init__(self,height,width,x=0,y=0,color = (255,255,255),dirx=1,diry=1):
        myClass.__init__(self,color)
        self.height = height 
        self.width = width 
        self.dim = (self.width,self.height)
        self.surface = pygame.Surface(self.dim,pygame.SRCALPHA, 32)
        self.surface.fill(color)
        self.mask = pygame.mask.from_surface(self.surface)
        self.spd = 3
        self.facing = 2
        self.moving = 2
        self.x = x
        self.y = y 
        self.pos = (self.x,self.y)
        self.dir = 0
        self.sides = 0

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

    def directions(self):

        if self.facing == self.moving:
            pass
        elif self.facing == 2 and self.moving == 3:
            self.surface = pygame.transform.rotate(self.surface, 180)
        elif self.facing == 2 and self.moving == 0:
            self.surface = pygame.transform.rotate(self.surface, 90)
        elif self.facing == 2 and self.moving == 1:
            self.surface = pygame.transform.rotate(self.surface, 270)

        elif self.facing == 0 and self.moving == 1:
            self.surface = pygame.transform.rotate(self.surface, 180)
        elif self.facing == 0 and self.moving == 2:
            self.surface = pygame.transform.rotate(self.surface, 270)
        elif self.facing == 0 and self.moving == 3:
            self.surface = pygame.transform.rotate(self.surface, 90)

        elif self.facing == 3 and self.moving == 2:
            self.surface = pygame.transform.rotate(self.surface, 180)
        elif self.facing == 3 and self.moving == 0:
            self.surface = pygame.transform.rotate(self.surface, 270)
        elif self.facing == 3 and self.moving == 1:
            self.surface = pygame.transform.rotate(self.surface, 90)

        elif self.facing == 1 and self.moving == 0:
            self.surface = pygame.transform.rotate(self.surface, 180)
        elif self.facing == 1 and self.moving == 2:
            self.surface = pygame.transform.rotate(self.surface, 90)
        elif self.facing == 1 and self.moving == 3:
            self.surface = pygame.transform.rotate(self.surface, 270)
            
        self.facing = self.moving

    def checkSides(self,hitBoxes,background,x = 1):
        if self.dir == 0:
            if hitBoxes[2].mapCollision(background) == False:
                self.open = [2]
                if x == 1:
                    self.open.append(0)
                self.choseDir()
                self.sides = 0
            elif hitBoxes[3].mapCollision(background) == False:
                self.open = [3]
                if x == 1:
                    self.open.append(0)
                self.choseDir()
                self.sides = 0
        elif self.dir == 1:
            if hitBoxes[2].mapCollision(background) == False:
                self.open = [2]
                if x == 1:
                    self.open.append(1)
                self.choseDir()
                self.sides = 0
            elif hitBoxes[3].mapCollision(background) == False:
                self.open = [3]
                if x == 1:
                    self.open.append(1)
                self.choseDir()
                self.sides = 0
        if self.dir == 2:
            if hitBoxes[0].mapCollision(background) == False:
                self.open = [0]
                if x == 1:
                    self.open.append(2)
                self.choseDir()
                self.sides = 0
            elif hitBoxes[1].mapCollision(background) == False:
                self.open = [1]
                if x == 1:
                    self.open.append(2)
                self.choseDir()
                self.sides = 0
        elif self.dir == 3:
            if hitBoxes[0].mapCollision(background) == False:
                self.open = [0]
                if x == 1:
                    self.open.append(3)
                self.choseDir()
                self.sides = 0
            elif hitBoxes[1].mapCollision(background) == False:
                self.open = [1]
                if x == 1:
                    self.open.append(3)
                self.choseDir()
                self.sides = 0
                
    def choseDir(self):
        import random
        self.dir = self.open[random.randrange(len(self.open))]


    def movement(self,hitBoxes,background):
        self.sides += 1
        if self.sides > 15:
            self.checkSides(hitBoxes,background)
        if self.dir == 0: # up
            if hitBoxes[0].mapCollision(background) == True:
                self.checkSides(hitBoxes,background,0)
            self.y -= self.spd
            self.moving = 0
        elif self.dir == 1: # down
            if hitBoxes[1].mapCollision(background) == True:
                self.checkSides(hitBoxes,background,0)
            self.y += self.spd
            self.moving = 1
        elif self.dir == 2: # right
            if hitBoxes[2].mapCollision(background) == True:
                self.checkSides(hitBoxes,background,0)
            self.x += self.spd
            self.moving = 2
        elif self.dir == 3: # left
            if hitBoxes[3].mapCollision(background) == True:
                self.checkSides(hitBoxes,background,0)
            self.x -= self.spd
            self.moving = 3
        self.pos = (self.x,self.y)
        
class box:
    def __init__(self,height,width,j,x=0,y=0,color = (255,0,0)):
        self.height = height 
        self.width = width 
        self.dim = (self.width,self.height)
        self.surface = pygame.Surface(self.dim,pygame.SRCALPHA, 32)
        self.surface.fill(color)
        self.positioning = j
        if self.positioning == 3 or self.positioning == 2:
            self.surface = pygame.transform.rotate(self.surface, 90)
        self.mask = pygame.mask.from_surface(self.surface)
        self.spd = 5
        self.x = x
        self.y = y
        self.pos = (self.x,self.y)
        self.dir = 0
    def getPos(self):
        return self.pos
    def follow(self,sprite):
        if self.positioning == 0: #above
            self.y = sprite.getY() - 15
            self.x = sprite.getX()
        elif self.positioning == 1: #below
            self.y = sprite.getY()
            self.x = sprite.getX()
        elif self.positioning == 2: #right
            self.x = sprite.getX()
            self.y = sprite.getY()
        elif self.positioning == 3: #left
            self.x = sprite.getX() - 15
            self.y = sprite.getY()

        self.pos = (self.x,self.y)

    def mapCollision(self,sprite2):
        offset = int(sprite2.getPos()[0] - self.pos[0]),int(sprite2.getPos()[1] - self.pos[1])
        collisionPoint = self.mask.overlap(sprite2.mask,offset)
        if collisionPoint:
            self.surface.fill((0,255,0))
            return True
        else:
            self.surface.fill((255,0,0))
            return False
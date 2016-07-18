import pygame
import config

import Colour
import Exceptions

from Directions import Direction


class Square(object):
    def __init__(self, x, y, size, colour):
        self.__x = x
        self.__y = y
        self.__size = size;    
        self.__colour = colour
            
    def getXPos(self):
        return self.__x

    def getYPos(self):
        return self.__y

    def setXPos(self, delta):
        self.__x += delta

    def setYPos(self, delta):
        self.__y += delta

    def getColour(self):
        return self.__colour

    def getSize(self):
        return self.__size

    def getBBox(self):
        return [self.getXPos(), self.getYPos(), self.getSize(), self.getSize()]

    def draw(self, surface):
        pygame.draw.rect(surface, self.getColour(), self.getBBox())

    def leftWallCollision(self, xCoord):
        if(self.getXPos() + xCoord < 0):
            return True
        else:
            return False

    def rightWallCollision(self, xCoord):
        if(self.getXPos() + xCoord + self.getSize() > config.width):
            return True
        else:
            return False

    def topWallCollision(self, yCoord):
        if(self.getYPos() + yCoord < 0):
            return True
        else:
            return False

    def bottomWallCollision(self, yCoord):
        if(self.getYPos() + yCoord + self.getSize() > config.height):
            return True
        else:
            return False        

    def move(self, direction):
        if direction == Direction.UP:
            if(not self.topWallCollision(-config.speedFactor*config.speed)):
                self.setYPos(-config.speedFactor*config.speed)
        
        elif direction == Direction.DOWN:
            if(not self.bottomWallCollision(config.speedFactor*config.speed)):
                self.setYPos(config.speedFactor*config.speed)
        
        elif direction == Direction.RIGHT:
            if(not self.rightWallCollision(config.speedFactor*config.speed)):
                self.setXPos(config.speedFactor*config.speed)
        
        elif direction == Direction.LEFT:
            if(not self.leftWallCollision(-config.speedFactor*config.speed)):
                self.setXPos(-config.speedFactor*config.speed)
        else:
            raise DirectionException("Must input valid direction, up, down, right, left")
        
    

                              

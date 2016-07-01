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

    def move(self, direction):
        if direction == Direction.UP:
            self.setYPos(-config.speed)
        elif direction == Direction.DOWN:
            self.setYPos(config.speed)
        elif direction == Direction.RIGHT:
            self.setXPos(config.speed)
        elif direction == Direction.LEFT:
            self.setXPos(-config.speed)
        else:
            raise DirectionException("Must input valid direction, up, down, right, left")
        
    

                              

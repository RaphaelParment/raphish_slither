import pygame
import Square
import Colour
import Exceptions
import config

from Directions import Direction


pygame.init()
gameDisplay = pygame.display.set_mode((config.width, config.height))
pygame.display.set_caption('Slither')

pygame.display.update()

gameExit = False

black = (0,0,0)
white = (255,255,255)

s = Square.Square(300, 400, 10, black)


d = Direction.LEFT;

while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
        
        

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                d = Direction.LEFT
            elif event.key == pygame.K_RIGHT:
                d = Direction.RIGHT
            elif event.key == pygame.K_UP:
                d = Direction.UP
            elif event.key == pygame.K_DOWN:
                d = Direction.DOWN
    gameDisplay.fill(white)
    s.move(d)           
    s.draw(gameDisplay)
    pygame.display.update()


pygame.quit()
quit()

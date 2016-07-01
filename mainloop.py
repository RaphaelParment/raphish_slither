import pygame
import Square
import Colour
import Exceptions

from Directions import Direction



pygame.init()
gameDisplay = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Slither')

pygame.display.update()

gameExit = False

black = (0,0,0)
white = (255,255,255)

s = Square.Square(300, 400, 10, black)



while not gameExit:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.KEYUP:
            if key == K_LEFT:
                gameDisplay.fill(white)
                s.draw(gameDisplay)
                s.move(Direction.LEFT)
        if event.type == pygame.KEYUP:
            if key == K_RIGHT:
                gameDisplay.fill(white)
                s.draw(gameDisplay)
                s.move(Direction.RIGHT)
    pygame.display.update()


pygame.quit()
quit()

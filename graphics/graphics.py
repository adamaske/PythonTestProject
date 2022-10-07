import sys
import pygame
import os
class Graphics():
    def __init__(self):
        #Set up window
        self.screen = pygame.display.set_mode((c.HEIGHT, c.WIDTH))
        self.screen.fill((255,255,255))

        #Load image into image
        self.image = pygame.image.load('Images/hammer.png')
    def ShowImage(self, path):
       print("Show Image!")
       self.image = pygame.image.load(os.path.join('Images', path))
    def UpdateGraphics(self):
        self.screen.blit(self.image, (0,0))
        pygame.display.update()
        


if __name__ == '__main__':
    #When run from this file
    import constants as c
    import helpers as h
    g = Graphics()
    g.ShowImage("", 50,50)
else:
    import graphics.constants as c
    import graphics.helpers as h


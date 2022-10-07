#Triggering the entire project
from sys import exit
#Do this by python run.py
#Imports c as an object
import constants as c
#Includes everything in helpers to this file
import helpers as h
#Graphics
from graphics.graphics import Graphics
#Pygame
import pygame
pygame.init()

def run():
    g = Graphics()
    i = 0
    g.ShowImage("hammer.png")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        g.UpdateGraphics()
        


    

#Convention for checking if this is the first file ran
if __name__ == '__main__':
    run()
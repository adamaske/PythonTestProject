#Triggering the entire project
#Do this by python run.py
#Imports c as an object
import constants as c
#Includes everything in helpers to this file
import helpers as h
#Graphics
from graphics.graphics import Graphics

def run():
    g = Graphics()
    g.ShowImage("/Images/hammer.png")

#Convention for checking if this is the first file ran
if __name__ == '__main__':
    run()
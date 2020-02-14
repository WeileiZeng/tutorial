# a moving face of smile
# the coods need be set according to the size of the window,otherwise the face
# would be funny
import time
import graphics
from graphics import *
def main():
    win=GraphWin('haha',300,300)
    win.setCoords(-10,-10,10,10)
    face=Circle(Point(0,0),6)
    eyes1=Oval(Point(-4,4),Point(-1.5,2))
    eyes2=Oval(Point(4,4),Point(1.5,2))
    eye1=Circle(Point(-2.8,2.85),0.8)
    eye2=Circle(Point(2.8,2.85),0.8)
    eye1.setFill('black')
    eye2.setFill('black')
    nose=Oval(Point(-1,1.5),Point(1,-2))
    nose.setFill('black')
    mouth=Circle(Point(0,-4),1.3)
    face.draw(win)
    eyes1.draw(win)
    eyes2.draw(win)
    eye1.draw(win)
    eye2.draw(win)
    nose.draw(win)
    mouth.draw(win)
    p=win.getMouse()
    for i in range(20):
        # close
        time.sleep(0.5)
        eyes1.undraw()
        eyes2.undraw()
        eye1.undraw()
        eye2.undraw()
        eyes1=Oval(Point(-4,3),Point(-1.5,2))  #
        eyes2=Oval(Point(4,3),Point(1.5,2))    #
        eye1=Circle(Point(-2.8,2.5),0.5)      #
        eye2=Circle(Point(2.8,2.5),0.5)       #
        eye1.setFill('black')
        eye2.setFill('black')
        eyes1.draw(win)
        eyes2.draw(win)
        eye1.draw(win)
        eye2.draw(win)
        # open
        time.sleep(0.5)
        eyes1.undraw()
        eyes2.undraw()
        eye1.undraw()
        eye2.undraw()
        eyes1=Oval(Point(-4,4),Point(-1.5,2))
        eyes2=Oval(Point(4,4),Point(1.5,2))
        eye1=Circle(Point(-2.8,2.85),0.8)
        eye2=Circle(Point(2.8,2.85),0.8)
        eye1.setFill('black')
        eye2.setFill('black')
        eyes1.draw(win)
        eyes2.draw(win)
        eye1.draw(win)
        eye2.draw(win)
    p=win.getMouse()
    win.close()
        

        
    
main()

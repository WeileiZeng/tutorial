# a moving face of smile
import graphics
from graphics import *
def main():
# draw the first smileface
    win=GraphWin('haha',300,300)
    win.setCoords(-10,-10,10,10)
    face=Circle(Point(0,0),6)
    eyes1=Oval(Point(-4,3),Point(-1.5,2))  #
    eyes2=Oval(Point(4,3),Point(1.5,2))    #
    eye1=Circle(Point(-2.8,2.5),0.5)      #
    eye2=Circle(Point(2.8,2.5),0.5)       #
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
    win.close()
# eyes shine
    
main()

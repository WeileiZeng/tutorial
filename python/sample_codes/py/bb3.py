"""this module is aimed to draw some points follow some rules that can gathering
them in a shape.then,make the all window a flash by controling the points"""


import py
import button
import time
import graphics
import math
from graphics import *
def main():
    win=GraphWin('flash',300,300)
    win.setCoords(-30.0,-30.0,30.0,30.0)
    tt=Text(Point(25,25),'haha')
    tt.draw(win)
    n=50
    points=[]
    for i in range(1050-n):#draw 1000 points
            x=20*(math.cos(i/10.0))*(i/1000.0)
            y=20*(math.sin(i/10.0))*(i/1000.0)
            p=Point(x,y)
            points.append(p)
            p.setFill('blue')
            p.draw(win)
            #time.sleep(0.001)
    for i in range(20):#flash 1
        continue
        for i in range(1000-n):
            p=points[i]
            p.undraw()
        time.sleep(0.2)
        for i in range(1000-n):
            p=points[i]
            p.draw(win)        
        n=n+50
    for i in range(1000):#flash 2
        p=points[i]
        p.setFill('red')
        time.sleep(0.02)
    pp=win.getMouse()
    win.close()
main()

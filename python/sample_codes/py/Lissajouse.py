"""this is a program to draw the Lissajous Figure.
main2 can draw a simple figure.
main can draw more figure and display them in a loop.
"""

import py
import button
import time
import graphics
import math
from graphics import *
def create_figure(win,vx,vy,phase_difference,color):
    #phase_difference is the part of phase x over y 
    #vx:vy=velosity_x:velocity_y
    lines=[]
    pi=math.pi
    rang=500.0
    x=20*(math.cos(phase_difference))
    y=20*(math.sin(0))
    p1=Point(x,y)    
    for i in range(1,rang+1):
            x=20*(math.cos(vx*i*2.0*pi/rang+phase_difference))
            y=20*(math.sin(vy*i*2.0*pi/rang))
            p2=Point(x,y)
            line=Line(p1,p2)
            lines.append(line)
            line.setFill(color)
            line.draw(win)
            p1=p2
            time.sleep(0.001)
    return lines
def undraw(points):
    for point  in points:
        point.undraw()
def create_win():
    win=GraphWin('Lissajouse Figure',400,400)
    win.setCoords(-40.0,-40.0,40.0,40.0)
    return win
def main2(xn,yn):
    win=create_win()
    create_figure(win,xn,yn,-math.pi/8.0,'blue')
    #win.getMouse()
    #win.close()

    
def main():#draw 10 figures
    pi=math.pi
    win=GraphWin('win',300,300)
    win.setCoords(-30.0,-30.0,30.0,30.0)
    face=Circle(Point(-4,0),2)
    face.setFill('red')
    face.setOutline('red')
    tt=Text(Point(25,25),'haha')
    tt.draw(win)
    n=4
    points1=[]
    rang=1000
    color=['blue','red']
    co=1
    coo=co%2
    for i in range(rang):
            x=20*(math.cos(i*2.0*pi/rang))
            y=20*(math.sin(n*i*2.0*pi/rang))
            p=Point(x,y)
            points1.append(p)
            p.setFill(color[coo])
            p.draw(win)
            time.sleep(0.001)
    points2=[]
    for i in range(10):
        for i in range(rang):
            p=points1[i]
            p.undraw()
            
            x=20*(math.cos(i*2.0*pi/rang))
            y=20*(math.sin(n*i*2.0*pi/rang))
            p=Point(x,y)
            points2.append(p)
            p.setFill(color[coo])
            p.draw(win)
            time.sleep(0.001)
        co=co+1
        coo=co%2
        points1=points2
        points2=[]
        n=n+1
        #time.sleep(1)
    for i in range(rang):
            p=points1[i]
            p.undraw()
        
        #time.sleep(0.3)
    pp=win.getMouse()
    win.close()


main2(13,19)



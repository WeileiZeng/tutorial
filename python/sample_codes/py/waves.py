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
def create_win():
    win=GraphWin('Lissajouse Figure',800,400)
    win.setCoords(-11.0,-20.5,71.0,20.5)
    l=Line(Point(-10,0),Point(70,0))
    l.draw(win)
    l.setArrow('last')
    l=Line(Point(0,-20),Point(0,20))
    l.draw(win)
    l.setArrow('last')
    Point(60,0).draw(win)
    Point(0,10).draw(win)
    Point(0,-10).draw(win)
    return win
def create_figure1(win,A,w,t,u,phase,color):#create_figure2 is faster than create_figure1
    #phase_difference is the part of phase x over y 
    #vx:vy=velosity_x:velocity_y
    points=[]
    pi=math.pi
    rang=100
    for i in range(rang):
        x=i*60.0/rang
        if t-x/u>0:
            y=A*math.cos(w*(t-x/u)+phase)
            p=Point(x,y)
            points.append(p)
            p.setFill(color)
            p.draw(win)
    print len(points)
    return points
def create_figure2(win,A,w,t,u,phase,color):
    #phase_difference is the part of phase x over y 
    #vx:vy=velosity_x:velocity_y
    lines=[]
    pi=math.pi
    rang=100
    point1=Point(0,A*math.cos(w*t+phase))
    for i in range(1,rang):
        x=i*60.0/rang
        if t-x/u>0:
            y=A*math.cos(w*(t-x/u)+phase)
            point2=Point(x,y)
            line=Line(point1,point2)
            lines.append(line)
            line.setFill(color)
            line.draw(win)
            point1=point2
    print len(lines)
    return lines
def create_figure3(win,A1,w1,t,u1,phase1,A2,w2,u2,phase2,color):
    #phase_difference is the part of phase x over y 
    #vx:vy=velosity_x:velocity_y
    lines=[]
    pi=math.pi
    rang=300
    point1=Point(0,A1*math.cos(w1*t+phase1)+A2*math.cos(w2*t+phase2))

    for i in range(1,rang):
        x=i*60.0/rang
        if t-x/u1>0 and t-x/u2>0 :
            y=A1*math.cos(w1*(t-x/u1)+phase1)+A2*math.cos(w2*(t-x/u2)+phase2)
            point2=Point(x,y)
            line=Line(point1,point2)
            lines.append(line)
            line.setFill(color)
            line.draw(win)
            point1=point2
    print len(lines)
    return lines
def undraw(objects):
    for picture  in objects:
        picture.undraw()

def main2():#just draw a wave
    win=create_win()
    A=5.0
    w=2.0#w=2*pi/T
    t=30.0
    u=3.0
    phase=0.0
    create_figure2(win,A,w,t,u,phase,'blue')
    win.getMouse()
    win.close()
def main3():#draw 2 wave seperately and then take the two together
    win=create_win()
    A1,A2=5.0,5.0
    w1,w2=3.0,6.0#w=2*pi/T
    u1,u2=10.0,10.0
    phase1,phase2=0.0,0.0
    t=6.0
    create_figure2(win,A1,w1,t,u1,phase1,'blue')
    create_figure2(win,A2,w2,t,u2,phase2,'yellow')
    create_figure3(win,A1,w1,t,u1,phase1,A2,w2,u2,phase2,'red')
    win.getMouse()
    win.close()
def main4():#the wave will move with the time
    win=create_win()
    A1,A2=5.0,5.0
    w1,w2=3.0,6.0#w=2*pi/T
    u1,u2=10.0,10.0
    phase1,phase2=0.0,0.0
    t=5
    rang=100
    for i in range(rang):
        t+=0.1
        wave1=create_figure2(win,A1,w1,t,u1,phase1,'blue')
        wave2=create_figure2(win,A2,w2,t,u2,phase2,'yellow')
        wave12=create_figure3(win,A1,w1,t,u1,phase1,A2,w2,u2,phase2,'red')
        time.sleep(0.1)
        undraw(wave1)
        undraw(wave2)
        undraw(wave12)
    win.getMouse()
    win.close()
main4()




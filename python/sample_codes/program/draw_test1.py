#draw the picture of (a*cos+b*sin,a*sin+b*cos)


import py
import time
from math import *
from graphics import *
def function1(a,b):#x,y=a*cos(sita)+b*sin(sita),a*sin(sita)+b*cos(sita)
    win=GraphWin('Curve Figure',400,400)
    win.setCoords(-5,-5,5,5)#set the center as origin
    n=100.0#accuracity
    for i in range(n):#draw the curve
        sita=2*pi*(i/n)-pi/4
        x,y=a*cos(sita)+b*sin(sita),a*sin(sita)+b*cos(sita)
        #function of the curve
        print x,y
        Point(x,y).draw(win)
        time.sleep(0.1)

from random import*
def ran():
    return randrange(1,5)
def ran2():
    return random()-0.5
def function2():# this program is gonna to solve a problem:
    # Suppose you are travel through crosses one by one. In each cross, there
    # are four derections you can go along, left, right, toward, backward. The
    # derection you choose is random. The question is what is the average distance
    # from you to the original place, after you have travel acroos 50 crosses.
    x,y=0,0
    for i in range(50):
        a=ran()
        if a==1:
            x-=1
        elif a==2:
            x+=1
        elif a==3:
            y-=1
        else:
            y+=1
    return x,y
def function3():
    x,y=0,0
    for i in range(30):
        sita=2*pi*random()
        x+=cos(sita)
        y+=sin(sita)
    return x,y
def draw():
    win=GraphWin('Curve Figure',600,600)
    win.setCoords(-15,-15,15,15)#set the center as origin
    c=Circle(Point(0,0),10)
    c.setOutline('red')
    c.draw(win)
    n=100000.0#accuracity
    for i in range(n):#draw the curve
        (x,y)=function3()
        #x+=ran2()
        #y+=ran2()
        Point(x,y).draw(win)
function1(1,2)
    
    

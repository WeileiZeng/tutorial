"""this program is a model of several particles' movement omly with the ifluence
of gravity. you can give the imformation of the number of the particles and
the mass,positon,velocity and color of each particle.then,you can see a simulative
result that how they would move.
you would give the infornation in this form:[mass,position,velocity,color]
like [10.0**6,[20.0,15.0],[450.0,0],'red'].
then put this as a elements into a big list.supposing the list is called a,
then do "main(a,timelenth,accuracy)",such as "main(a,5,0.1*4)"
so the program will calculate per 0.0001 secend of the particles'movement from
0 to 5th secends.
the program is not very accurate.
the difference between main and main2:
in main2,the locus the particles has gone on will be kept in the window,
but in main, not.

"""
import math
import time
import copy
import graphics
from graphics import *
class particle():
    def __init__(self,win,mass,position,velocity,color):
        self.mass=mass
        self.color=color
        self.win=win
        self.position_x=position[0]
        self.position_y=position[1]
        self.velocity_x=velocity[0]
        self.velocity_y=velocity[1]
        self.point=Circle(Point(self.position_x,self.position_y),0.1)
        self.point.setFill(color)
        self.point.setOutline(color)
        self.point.draw(win)
    def move(self,dx,dy):
        self.point=Circle(Point(self.position_x+dx,self.position_y+dy),0.1)
        self.point.setFill(self.color)
        self.point.setOutline(self.color)
        self.point.draw(self.win)
def main(variable,timelenth,accuracy):#timelenth is how long the time you want to calculate
    #accuracy is the time differnce between every two calculations 
    win=GraphWin('window',600,600)
    win.setCoords(-10.0,-10.0,50.0,50.0)
    Line(Point(0,-10),Point(0,50)).draw(win)
    Line(Point(-10,0),Point(50,0)).draw(win)
    g=0.00000000006754#wan you yin li chang liang
    dt=accuracy
    particles=[]
    n=len(variable)
    for pp in variable:
        mass=pp[0]
        position=pp[1]
        velocity=pp[2]
        color=pp[3]
        a=particle(win,mass,position,velocity,color)
        particles.append(a)
    for i in range(int(timelenth/accuracy)):
        print i
        for pp1 in particles:
            fx,fy=0,0
            for pp2 in particles:
             if pp2 != pp1:
                xx,yy=pp2.position_x-pp1.position_x,pp2.position_y-pp1.position_y
                rr=(xx)**2+(yy)**2
                f12=g*pp1.mass*pp2.mass/rr
                r=math.sqrt(rr)
                fx +=f12*(xx/r)
                fy +=f12*(yy/r)
            pp1.dvx,pp1.dvy=(fx/pp1.mass)*dt,(fy/pp1.mass)*dt
        for pp in particles:
            pp.point.move((pp.velocity_x+0.5*pp.dvx)*dt,(pp.velocity_y+0.5*pp.dvx)*dt)#different from main2
            pp.position_x +=pp.velocity_x*dt
            pp.position_y +=pp.velocity_y*dt
            pp.velocity_x +=pp.dvx
            pp.velocity_y +=pp.dvy
def main2(variable,timelenth,accuracy):#timelenth is how long the time you want to calculate
    #accuracy is the time differnce between every two calculations 
    win=GraphWin('wimdow',600,600)
    win.setCoords(-10.0,-10.0,50.0,50.0)
    Line(Point(0,-10),Point(0,50)).draw(win)
    Line(Point(-10,0),Point(50,0)).draw(win)
    g=0.00000000006754#wan you yin li chang liang
    dt=accuracy
    particles=[]
    n=len(variable)
    for pp in variable:
        mass=pp[0]
        position=pp[1]
        velocity=pp[2]
        color=pp[3]
        a=particle(win,mass,position,velocity,color)
        particles.append(a)
    for i in range(int(timelenth/accuracy)):
        for pp1 in particles:
            fx,fy=0,0
            for pp2 in particles:
             if pp2 != pp1:
                xx,yy=pp2.position_x-pp1.position_x,pp2.position_y-pp1.position_y
                rr=(xx)**2+(yy)**2
                f12=g*pp1.mass*pp2.mass/rr
                r=math.sqrt(rr)
                fx +=f12*(xx/r)
                fy +=f12*(yy/r)
            pp1.dvx,pp1.dvy=(fx/pp1.mass)*dt,(fy/pp1.mass)*dt
        for pp in particles:
            pp.move((pp.velocity_x+0.5*pp.dvx)*dt,(pp.velocity_y+0.5*pp.dvx)*dt)
            pp.position_x +=pp.velocity_x*dt
            pp.position_y +=pp.velocity_y*dt
            pp.velocity_x +=pp.dvx
            pp.velocity_y +=pp.dvy
    
b=[[1000000000000000.0,[2.0,3.0],[100,0]],
   [1000000000000000.0,[10.0,3.0],[20,0]],
   [500000000000000.0,[7.0,40.0],[0,-10.0]],
   [1000000000000000.0,[30.0,20.0],[0,10.0]]]
a=[[1.5e16,[20.0,20.0],[0,0],'black'],
   [10.0**6,[20.0,15.0],[345.0,0],'red'],
   [10.0**6,[25.0,18.0],[30.0,280],'green'],
   [10.0**6,[20.0,10.0],[225.0,-20],'yellow']]
main2(a,10,1.5e-3)
            
            
            
            
    
    
        
    
    
    
    
    

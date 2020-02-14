#
import py
import graphics
import button
from button import *
from graphics import *
def main():
    win=GraphWin('hanluota',400,400)
    win.setCoords(-10.0,0.0,10.0,20.0)
    rr=Rectangle(Point(-6,6),Point(6,7))
    rr.draw(win)
    rr=Rectangle(Point(-4.25,7),Point(-3.75,15))
    rr.draw(win)
    rr=Rectangle(Point(-0.25,7),Point(0.25,15))
    rr.draw(win)
    rr=Rectangle(Point(3.75,7),Point(4.25,15))
    rr.draw(win)
    b1=button(win,Point(-4,8),4.0,1.0,'')
    b2=button(win,Point(-4,10),3.0,1.0,'')
    b3=button(win,Point(-4,12),2.0,1.0,'')
    q=0
    height=[6,0,0]
    positionx=[-4,-4,-4]
    position=[0,0,0]
    while q==0:
        pp=win.getMouse()
        if b1.judge():
            bi.active()
            pp=getMouse()
            x=pp.getX()
            y=pp.getY()
            if x>-6 and x<6 and y>6 and y<15:
                if x>2.0:
                    dx=4.0-positionx[0]
                    dy=height[2]-height[position[0]]+2.0
                    b1.move(dx,dy)
                    height[position[0]]
                    position1[0]=4
                    position2[0]=2
                elif x<-2.0:
                    dx=-4.0-positionx[0]
                    dy=height[2]-height[position[0]]+2.0
                    b1.move(dx,dy)                    
    



    bb=button(win,Point(-5,2),2,2,'start')
    print bb.x
    pp=win.getMouse()
    win.close()
main()
    

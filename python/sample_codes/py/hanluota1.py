#hanluota1.py
import py
import copy
import time
import graphics
import button
from copy import *
from button import *
from graphics import *
def hanluota(n):
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
    q=0
    p0={'x':-4.0,'y':n}
    p1={'x':0.0,'y':0.0}
    p2={'x':4.0,'y':0.0}
    bb=[]
    bbb=[]
    
    move(n,p0,p1,p2,q,win,bb,bbb)
    pp=win.getMouse()
    win.close()
def move(n,p0,p1,p2,q,win,bb,bbb):
    
    if q==0:
        q=1
        bb=[]
        bbb=[]
        color=['yellow','red','blue','gray','green']
        for i in range(n):
            
            b1=button(win,Point(-4,7.5+i/1.0),4.0-i*0.4,1.0,'')
            b1.setFill(color[i%5])
            bb.append(b1)
        bbb.append(bb)
        time.sleep(0.1)

    if n==1:
        b1=bb[0]
        dx=p1['x']-p0['x']
        dy=p1['y']-p0['y']+1.0
        p0['y']=p0['y']-1
        p1['y']=p1['y']+1
        b1.move(dx,dy)
    elif n==2:
        b1=bb[1]
        b2=bb[0]
        dx=p2['x']-p0['x']
        dy=p2['y']-p0['y']+1.0
        p2['y']=p2['y']+1.0
        p0['y']=p0['y']-1.0
        b1.move(dx,dy)
        time.sleep(0.1)
        dx=p1['x']-p0['x']
        dy=p1['y']-p0['y']+1.0
        p1['y']=p1['y']+1.0
        p0['y']=p0['y']-1.0
        b2.move(dx,dy)
        time.sleep(0.1)
        dx=p1['x']-p2['x']
        dy=p1['y']-p2['y']+1.0
        p1['y']=p1['y']+1.0
        p2['y']=p2['y']-1.0
        b1.move(dx,dy)
    else:
        length=len(bbb)
        cc=bbb[length-1]
        bb=[]
        for i in cc:
            bb.append(i)
        b1=bb[0]
        del bb[0]
        bbb.append(bb)
        pp=p1
        p1=p2
        p2=pp
        print n-1,p0,p1,p2,q,len(bb),len(bbb)#
        move(n-1,p0,p1,p2,q,win,bb,bbb)
        #del bbb[]
        time.sleep(0.1)
        length =len(bbb)
        b1=bbb[length-2][0]
        dx=p2['x']-p0['x']
        dy=p2['y']-p0['y']+1.0
        p0['y']=p0['y']-1.0
        p2['y']=p2['y']+1.0
        b1.move(dx,dy)
        time.sleep(0.1)
        pp=p0
        p0=p1
        p1=p2
        p2=pp
        print n-1,p0,p1,p2,q,len(bb),len(bbb)#
        move(n-1,p0,p1,p2,q,win,bb,bbb)
        time.sleep(0.1)
        length=len(bbb)
        del bbb[length-1]

hanluota(10)

    

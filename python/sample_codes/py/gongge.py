#bad work
import time
import py
import button
import graphics
from graphics import *
from button import *




def main(row,col,n,derection):
    ddx=0
    ddy=0
    dx=1*derection
    dy=1*derection
    if row==1:
        dy=-1
        ddy=1
    elif row==n:
        dy=1
        ddy=-1
    if col==1:
        dx=-1
        ddx=1
    elif col==n:
        dx=1
        ddx=-1
    print dx,dy,derection
    bb=[]
    for i in range(n+1):
        cc=[]
        for i in range(n+1):
            cc.append(0)
        bb.append(cc)
    for i in range(n*n):
        bb[row][col]=i+1
        row=row+dy
        col=col+dx
        #print 'row,col= ',row,col
        if row==n+1:
            row=1
        if row==0:
            row=n
        if col==n+1:
            col=1
        if col==0:
            col=n
        if bb[row][col]>0:
            row=row-dy
            col=col-dx
            #print 'row,col1= ',row,col
            if row==n+1:
                row=1
            if row==0:
                row=n
            if col==n+1:
                col=1
            if col==0:
                col=n
            row=row+ddy
            col=col+ddx
            

            if row==n+1:
                row=1
            if row==0:
                row=n+1
            if col==n+1:
                col=1
            if col==0:
                col=n
            #print 'row,col2= ',row,col
    for i in range(n+1):
            print bb[i]
    del bb[0]
    for i in range(n):
        del bb[i][0]
    return bb
    #print '------------------------------'
def main1():
    win=GraphWin('gongge',400,320)
    win.setCoords(0,0,10,8)
    gongge=[]
    for i in range(5):
        bb=[]
        for j in range(5):
            bb1=button(win,Point(1.0+j,2.0+i),1.0,1.0,'')
            bb.append(bb1)
        gongge.append(bb)
    setfirst=button(win,Point(8,7),2.0,1.0,'set')
    answer1=button(win,Point(8,5.5),2.0,1.0,'answer1')
    answer2=button(win,Point(8,4),2.0,1.0,'answer2')
    #reset=button(win,Point(8,2.5),2.0,1.0,'reset')
    qquit=button(win,Point(8,1),2.0,1.0,'exit')
    rowen=Entry(Point(1.6,1),2)
    rowen.draw(win)
    colen=Entry(Point(3,1),2)
    colen.draw(win)
    Text(Point(0.7,1),'row:').draw(win)
    Text(Point(2.3,1),'col:').draw(win)
    Text(Point(3.8,1),'size:').draw(win)
    sizeen=Entry(Point(4.5,1),2)
    sizeen.draw(win)
    answer=0
    derection=1
    pp=win.getMouse()
    while not qquit.judge(pp):
        if answer1.judge(pp):
            drection=1
            answer=1
        if answer2.judge(pp):
            drection=-1*derection
            answer=1
        if setfirst.judge(pp) or answer ==1 :
            q=1
            while q==1:
                try:
                    row=rowen.getText()
                    row=eval(row)
                    col=colen.getText()
                    col=eval(col)
                    size=sizeen.getText()
                    size=eval(size)
                    print row,col,derection,size
                    arrow=main(row,col,size,derection)
                    
                    print arrow
                    q=0
                except:
                    time.sleep(0.5)
                    
            for i in range(size):
                for j in range(size):
                    tt=arrow[i][j]
                    bb1=gongge[i][j]
                    bb1.setText(tt)
                    #time.sleep(0.1)
            answer=0

        pp=win.getMouse()
    win.close()
main1()    
#main(1,2,3)
#main(1,6,11)

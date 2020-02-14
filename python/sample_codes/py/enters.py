import button
import time
import graphics
import random
from graphics import *
from button import *
def main():
    win=GraphWin('enters',250,300)
    win.setCoords(0,0,10,12.0)
    num=range(0,10)
    nu=[]
    for i in range(10):
        a=random.randint(0,9-i)
        nu.append(num[a])
        del num[a]
    a=2.0
    b=5.0
    c=8.0
    d=4.0
    e=6.0
    f=8.0
    h=10.0
    pp=[Point(a,d),Point(a,e),Point(a,f),Point(a,h),
        Point(b,e),Point(b,f),Point(b,h),
        Point(c,e),Point(c,f),Point(c,h),
        Point(b,d),Point(c,d)]
    bb=[]
    for i in range(10):
        b=button(win,pp[i],1.8,1.8,nu[i])
        bb.append(b)
    c=button(win,pp[10],1.8,1.8,'C')
    enter=button(win,pp[11],1.8,1.8,'En')
    eexit=button(win,Point(2,2.0),2.0,1.0,'Exit')
    reset=button(win,Point(5.0,2.0),2.0,1.0,'reset')
    ll=Line(Point(7.0,1.6),Point(9.0,1.6))
    ll.draw(win)
    tt=Text(Point(8.0,2.0),'')
    tt.draw(win)
    ttt=0
    pp=win.getMouse()
    while not eexit.judge(pp):
        if c.judge(pp):
            aa=tt.getText()
            aa=aa[0:len(aa)-1]
            tt.setText(aa)
            ttt=ttt/10
            
        if reset.judge(pp):
            num=range(0,10)
            nu=[]
            for i in range(10):
                a=random.randint(0,9-i)
                nu.append(num[a])
                bb[i].setText(num[a])
                del num[a]
        if enter.judge(pp):
            tt.setText('')
            print ttt
            ttt=0
        for i in range(10):
            b=bb[i]
            if b.judge(pp):
                aa=tt.getText()
                aa=aa+'#'
                tt.setText(aa)
                ttt=ttt*10+b.getText()
                break
        pp=win.getMouse()
    win.close()
main()
            
            
            
    
    
    
    
        
        
    

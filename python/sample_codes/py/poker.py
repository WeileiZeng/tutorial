# poke
import button
import time
import graphics
import math
import random
from graphics import *

def randoms(n):
    rand=[]
    num=range(52)
    for i in range(n):
        a=random.randint(0,51-i)
        b=num[a]
        rand.append(b)
        del num[a]
    return rand


def main():
    win=GraphWin('win',600,600)
    win.setCoords(-30.0,-30.0,30.0,30.0)
    images=['1.gif','2.gif','3.gif','4.gif','5.gif','6.gif','7.gif','8.gif',
            '9.gif','10.gif','11.gif','12.gif','13.gif','14.gif','15.gif','16.gif',
            '17.gif','18.gif','19.gif','20.gif','21.gif','22.gif','23.gif','24.gif',
            '25.gif','26.gif','27.gif','28.gif','29.gif','30.gif','31.gif','32.gif',
            '33.gif','34.gif','35.gif','36.gif','37.gif','38.gif','39.gif','40.gif',
            '41.gif','42.gif','43.gif','44.gif','45.gif','46.gif','47.gif','48.gif',
            '49.gif','50.gif','51.gif','52.gif']
            
    rand=randoms(13)
    linedown=[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
    #represent their condition(1or-1:up or down)
    widedown=[]
    n=13
    for i in range(n):
        widedown.append(-29.1+3*i)#their width
    widedown.append(-29.1+46.2)
    listdown=[]#pokers
    listup=[]
    un='false'
    # draw some button
    x=5
    y=3
    start=button.button(win,Point(-25,-28),x,y,'start')
    play=button.button(win,Point(-15,-28),x,y,'play')
    deal=button.button(win,Point(-10,-28),x,y,'deal')
    undo=button.button(win,Point(-20,-28),x,y,'undo')
    quit1=button.button(win,Point(-0,-28),x,y,'quit')
    pp=win.getMouse()
    while start.judge(pp)=='false':
        pp=win.getMouse()
    for i in range(13):
            a01=Image(Point(-24+i*3,-10),images[rand[i]])
            listdown.append(a01)
            a01.draw(win)
            list2=listdown
    uu=0
    ww=0
    qq=1
    

    while qq==1:
        pp=win.getMouse()
        x=pp.getX()
        y=pp.getY()
        
        if x>widedown[0]and x<widedown[n] and y>-17.7 and y<-2.4 and ww==0:#chose a poker per time
            for i in range(n):
                if x>widedown[n-1-i]:
                    poke=n-1-i
                    break
                
            a01=listdown[poke]
            a01.move(0,(-2)*linedown[poke])
            linedown[poke]=(-1)*linedown[poke]
        if deal.judge(pp)=='ture':
            for i in range(13):
                a01=listdown[i]
                a01.undraw()
            rand=randoms(13)
            linedown=[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
            uu=0
            ww=0
            listdown=[]
            for i in range(13):
                a01=Image(Point(-24+i*3,-10),images[rand[i]])
                listdown.append(a01)
                a01.draw(win)
        if play.judge(pp)=='ture':
            for i in range(13):
                a01=listdown[i]
                a01.undraw()
                up=0
                down=0
            listdown=[]
            listdown1=[]
            for i in range(13):
                if linedown[i]==1:
                    a01=Image(Point(-24+up,10),images[rand[i]])
                    up=up+3
                    listdown.append(a01)
                    a01.draw(win)

                if linedown[i]==-1:
                    a01=Image(Point(-24+down,-10),images[rand[i]])
                    down=down+3
                    listdown.append(a01)
                    a01.draw(win)
                    uu=uu+3
            """widedown=[]            
            for i in range(n):
                widedown.append(-30+3*i)#their width
            widedown.append(-30+3*(n+2))                    
                    # a01.move(-25-uu-a01.getX(aa),15-a01.getY(aa))"""
                    
            un=undo.active()
            ww=1
        if undo.judge(pp)=='ture' and un=='ture':
            for i in range(13):
                a01=listdown[i]
                a01.undraw()
            listdown=[]
            linedown=[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
            for i in range(13):
                a01=Image(Point(-24+i*3,-10),images[rand[i]])
                listdown.append(a01)
                a01.draw(win)
            un=undo.unactive()
            ww=0
        if quit1.judge(pp)=='ture':
            win.close()
            qq=0           
main()

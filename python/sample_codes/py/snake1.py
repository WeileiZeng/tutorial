import py
import random
import button
import time
import graphics
from graphics import *
def main():
    win=GraphWin('snake',420,500)
    win.setCoords(0.0,-4.0,21.0,21.0)
    window=Rectangle(Point(0.4,0.4),Point(20.6,20.6))
    window.draw(win)
    up=button.button(win,Point(10,-0.8),2,2,'/\\')
    down=button.button(win,Point(10,-2.9),2,2,'\/')
    left=button.button(win,Point(7.5,-2.9),2,2,'<==')
    right=button.button(win,Point(12.5,-2.9),2,2,'==>')
    start=button.button(win,Point(15.3,-2.9),2.3,1.5,'start')
    pause=button.button(win,Point(17.8,-2.9),2.2,1.5,'pause')
    qquit=button.button(win,Point(20,-2.9),1.8,1.5,'quit')
    soon=button.button(win,Point(1.8,-1),1.8,1.5,'soon')
    slow=button.button(win,Point(4,-1),1.8,1.5,'slow')
    speed=Text(Point(1.7,-3),'speed:')
    speed.draw(win)
    s0=button.button(win,Point(3.7,-3),0.3,1.0,'')
    s1=button.button(win,Point(4,-3),0.3,1.0,'')
    s2=button.button(win,Point(4.3,-3),0.3,1.0,'')
    s3=button.button(win,Point(4.6,-3),0.3,1.0,'')
    s4=button.button(win,Point(4.9,-3),0.3,1.0,'')
    s5=button.button(win,Point(5.2,-3),0.3,1.0,'')
    s6=button.button(win,Point(5.5,-3),0.3,1.0,'')
    s7=button.button(win,Point(5.8,-3),0.3,1.0,'')
    s8=button.button(win,Point(6.1,-3),0.3,1.0,'')
    s0.active()
    sp=0
    speed=[s0,s1,s2,s3,s4,s5,s6,s7,s8]
    sc=0
    score=Text(Point(15.3,-1),'score:')
    score.draw(win)
    score=Text(Point(17.3,-1),sc)
    score.draw(win)
    pp=win.getMouse()  
    q=1
    x=0
    y=0
    eg=0
    eggx=0
    eggy=0
    snake=[]
    direction='right'
    egg=Point(100,100)
    egg.draw(win)
    while q==1:
        if start.judge(pp):
            sn=button.button(win,Point(1,10),0.9,0.9,'')
            sn.active()
            snake.append(sn)
            sn=button.button(win,Point(2,10),0.9,0.9,'')
            sn.active()
            snake.append(sn)
            start.setText('restart')
            q=0
        if qquit.judge(pp):
            q=0
        ppp=win.checkMouse()
        if type(pp)==type(ppp):
            pp=ppp        
        time.sleep(1)
    snakexy=[[1,10],[2,10]]
    pp=Point(12.5,-2.9)
    q=1
    n=1.0
    while q==1:
        #the following is to procider the eggs to make the snake longer
        while eg==0:
            eggx=random.randint(1,20)
            eggy=random.randint(1,20)
            if [eggx,eggy] in snakexy:
                eg=0
            else:
                eg=1
        egg.undraw()
        egg=Circle(Point(eggx,eggy),0.5)
        egg.setFill('yellow')
        egg.setOutline('yellow')
        egg.draw(win)
        #the following is to judge  
        if start.judge(pp):
            for i in range(len(snake)):
                sn=snake[i]
                sn.close()
            snake=[]
            snakexy=[[1,10],[2,10]]
            sn=button.button(win,Point(1,10),0.9,0.9,'')
            sn.active()
            snake.append(sn)
            sn=button.button(win,Point(2,10),0.9,0.9,'')
            sn.active()
            snake.append(sn)
            time.sleep(1.0)
            pp=Point(0,0)
            direction='right'
        if up.judge(pp) and direction !='down':
            direction='up'
        if down.judge(pp) and direction !='up':
            direction='down'
        if left.judge(pp) and direction !='right':
            direction='left'
        if right.judge(pp) and direction !='left':
            direction='right'
        ll=len(snake)
        if direction=='up':
            x=snakexy[ll-1][0]
            y=snakexy[ll-1][1]+1               
        if direction=='down':
            x=snakexy[ll-1][0]
            y=snakexy[ll-1][1]-1
        if direction=='left':
            x=snakexy[ll-1][0]-1
            y=snakexy[ll-1][1]
        if direction=='right':
            x=snakexy[ll-1][0]+1
            y=snakexy[ll-1][1]
        if soon.judge(pp) and n>0.3:
            n=n-0.1
            sp=sp+1
            spp=speed[sp]
            spp.active()
            pp=Point(0,0)
        if slow.judge(pp) and n<1.0:
            n=n+0.1
            sp=sp-1
            spp=speed[sp+1]
            spp.unactive()
            pp=Point(0,0)
        if qquit.judge(pp):
            q=0
            continue
        if pause.judge(pp):
                time.sleep(1.0)
                ppp=win.checkMouse()
                if type(pp)==type(ppp):
                    pp=ppp
                continue
            
        if ([x,y] in snakexy) or x<1 or x>20 or y<1 or y>20 :
            print 'x,y=',x,y#
            print 'snakexy=',snakexy #
            for i in range(4):
                ra=i%3
                pain=Circle(Point(snakexy[ll-1][0],snakexy[ll-1][1]),(ra+1)/5.0)
                pain.draw(win)
                pain.setFill('red')
                pain.setOutline('red')
                time.sleep(0.2)
                pain.undraw()
            pp=Point(15.3,-2.9)
            time.sleep(n)
        else:
            sn=button.button(win,Point(x,y),0.9,0.9,'')
            sn.active()
            snake.append(sn)
            if [x,y]==[eggx,eggy]:
                eg=0
                sc=sc+sp+1
                score.setText(sc)
            else:
                sn=snake[0]
                sn.close()
                del snake[0]
            #recieve new order
            time.sleep(n)
            ppp=win.checkMouse()
            if type(pp)==type(ppp):
                pp=ppp
        snakexy.append([x,y])
        if [x,y] != [eggx,eggy]:
            del snakexy[0]        
    win.close()
main()

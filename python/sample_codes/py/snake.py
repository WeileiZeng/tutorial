import py
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
    s1=button.button(win,Point(4,-3),0.5,1.0,'')
    s2=button.button(win,Point(4.5,-3),0.5,1.0,'')
    s3=button.button(win,Point(5,-3),0.5,1.0,'')
    s4=button.button(win,Point(5.5,-3),0.5,1.0,'')
    s0=button.button(win,Point(3.5,-3),0.5,1.0,'')
    score=Text(Point(15.3,-1),'score:')
    score.draw(win)
    score=Text(Point(17.3,-1),0000)
    score.draw(win)
    pp=win.getMouse()
    q=1
    x=0
    y=0
    snake=[]
    direction='right'
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
        if up.judge(pp) and direction !='down':
            direction='up'
        if down.judge(pp) and direction !='up':
            direction='down'
        if left.judge(pp) and direction !='right':
            direction='left'
        if right.judge(pp) and direction !='left':
            direction='right'
        if direction=='up':
            speed.setText('up')#
            ll=len(snake)
            dx=snakexy[ll-1][0]-snakexy[0][0]
            dy=snakexy[ll-1][1]-snakexy[0][1]
            dy=dy+1
            sn=snake[0]
            sn.move(dx,dy)
            sn.active()
            snake.append(sn)
            del snake[0]
            x=snakexy[ll-1][0]
            y=snakexy[ll-1][1]+1
        if direction=='down':
            speed.setText('down')#
            ll=len(snake)
            dx=snakexy[ll-1][0]-snakexy[0][0]
            dy=snakexy[ll-1][1]-snakexy[0][1]
            dy=dy-1
            sn=snake[0]
            sn.move(dx,dy)
            sn.active()
            snake.append(sn)
            del snake[0]
            x=snakexy[ll-1][0]
            y=snakexy[ll-1][1]-1
        if direction=='left':
            speed.setText('left')#
            ll=len(snake)
            dx=snakexy[ll-1][0]-snakexy[0][0]
            dy=snakexy[ll-1][1]-snakexy[0][1]
            dx=dx-1
            sn=snake[0]
            sn.move(dx,dy)
            sn.active()
            snake.append(sn)
            del snake[0]
            x=snakexy[ll-1][0]-1
            y=snakexy[ll-1][1]            
        if direction=='right':
            speed.setText('right')#
            ll=len(snake)
            dx=snakexy[ll-1][0]-snakexy[0][0]
            dy=snakexy[ll-1][1]-snakexy[0][1]
            
            dx=dx+1
            
            sn=snake[0]
            sn.move(dx,dy)
            sn.active()
            snake.append(sn)
            del snake[0]
            x=snakexy[ll-1][0]+1
            y=snakexy[ll-1][1]            

        if soon.judge(pp):
            pass
        if slow.judge(pp):
            pass

            
        time.sleep(n)   
        ppp=win.checkMouse()
        if type(pp)==type(ppp):
            pp=ppp
        if qquit.judge(pp):
            q=0                    
        if [x,y] in snakexy:
            print 'x,y=',x,y#
            print 'snakexy=',snakexy #
            for i in range(2):
                ra=i%3
                pain=Circle(Point(x,y),(ra+1)/5.0)
                pain.draw(win)
                pain.setFill('red')
                pain.setOutline('red')
                time.sleep(0.2)
                pain.undraw()
            pp=Point(15.3,-2.9)
        """if direction=='up':

            
            snakexy.append([x,y])
            del snakexy[0]
                       
        if direction=='down':

            snakexy.append([x,y])
            del snakexy[0]
                        
        if direction=='left':

            snakexy.append([x,y])
            del snakexy[0]
                        
        if direction=='right':"""
        snakexy.append([x,y])
        del snakexy[0]

    win.close()
main()

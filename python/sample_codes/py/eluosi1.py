import py
import random
import button
import copy
import time
import graphics
import eluosi
from graphics import *
class square():
    def __init__(self,win,center,size,color):
        self.x=center.getX()
        self.y=center.getY()
        self.square=Rectangle(Point(self.x-size/2.0,self.y-size/2.0),
                              Point(self.x+size/2.0,self.y+size/2.0))
class Squares():
    def __init__(self,win,x,y,shapenumber):
        self.shapenumber=shapenumber
        self.y=y
        self.x=x
        self.win=win
        self.shape=0
        self.ss=0
        self.position=0
        self.position_number=0
        self.color=['red','blue','yellow','green','orange','purple','gray']
        shapes=[        #shapes contains all position of the seven series of four squares,it makes move easier
            [[[-1,1],[0,1],[-1,0],[0,0]]],#0zhengfangxing
            [[[0,2],[0,1],[0,0],[0,-1]],[[-2,0],[-1,0],[0,0],[1,0]]],#1changtiao
            [[[-1,1],[0,1],[0,0],[1,0]],[[1,1],[1,0],[0,0],[0,-1]]],#2youtixing
            [[[-1,0],[0,0],[0,1],[1,1]],[[0,1],[0,0],[1,0],[1,-1]]],#3zuotixing
            [[[-1,0],[0,1],[0,0],[1,0]],[[0,1],[0,0],[1,0],[0,-1]],
            [[-1,0],[0,-1],[0,0],[1,0]],[[0,1],[0,0],[-1,0],[0,-1]]],#4shangxing
            [[[-1,0],[0,0],[1,0],[1,1]],[[0,1],[0,0],[ 0,-1],[1,-1]],
            [[-1,-1],[-1,0],[0,0],[1,0]],[[-1,1],[0,1],[0,0],[0,-1]]],#5zheng7
            [[[-1,1],[-1,0],[0,0],[1,0]],[[0,1],[1,1],[0,0],[0,-1]],
            [[-1,0],[0,0],[1,0],[1,-1]],[[-1,-1],[0,-1],[0,0],[0,1]]]]#6fan7   
        shape1=shapes[shapenumber]#choose the shape of the 4 squares
        self.shape=shape1
        self.ss=[]
        ran=random.randint(0,len(shape1)-1)#decide the first derection of the squares in certain shapes
        self.position_number=ran
        shape2=shape1[ran]#'shape2' contains the positions of the 4 squares
        self.position=shape2
        Squares.draw(self)
    def draw(self):
        for i in range(4):
            a=self.position[i][0]+self.x-0.47
            b=self.position[i][1]+self.y-0.47
            c=self.position[i][0]+self.x+0.47
            d=self.position[i][1]+self.y+0.47
            #print a,b,c,d
            rect=Rectangle(Point(a,b),Point(c,d))
            rect.draw(self.win)
            rect.setFill(self.color[self.shapenumber])
            rect.setOutline(self.color[self.shapenumber])
            self.ss.append(rect)
    def spin(self,spin_derection):
        Squares.undraw(self)
        self.ss=[]
        self.position_number=(self.position_number+spin_derection)%(len(self.shape))
        shape2=self.shape[self.position_number]#'shape2' contains the positions of the 4 squares
        self.position=shape2
        Squares.draw(self)
    def move(self,dx,dy):
        for i in range(4):
            self.ss[i].move(dx,dy)
        self.x=self.x+dx
        self.y=self.y+dy
        x=self.x
        y=self.y
    def undraw(self):
        for i in range(4):
            self.ss[i].undraw()
    
                            
                         

                         
def main():
    win=GraphWin('welcome!',430,700)
    win.setCoords(0.0,-3.0,14.0,21.0)
    window=Rectangle(Point(0.5,0.5),Point(10.5,20.5))
    window.draw(win)
    up=button.button(win,Point(5,-0.5),1.5,1.5,'/\\')
    down=button.button(win,Point(5,-2.2),1.5,1.5,'\/')
    left=button.button(win,Point(3.3,-2.2),1.5,1.5,'<==')
    right=button.button(win,Point(6.7,-2.2),1.5,1.5,'==>')#
    start=button.button(win,Point(12.3,1.6),1.8,1.0,'start')
    pause=button.button(win,Point(12.3,0.3),1.8,1.0,'pause')
    stop=button.button(win,Point(12.3,-1.0),1.8,1.0,'stop')
    eexit=button.button(win,Point(12.3,-2.3),1.8,1.0,'exit')
    introduction=button.button(win,Point(9.7,-2.3),2.8,1.0,'introduction')#
    soon=button.button(win,Point(12.3,13.6),1.8,1.0,'soon')
    slow=button.button(win,Point(12.3,12.3),1.8,1.0,'slow')#
    mode1=button.button(win,Point(12.3,11.0),1.8,1.0,'mode1')
    mode2=button.button(win,Point(12.3,9.7),1.8,1.0,'mode2')#
    right1=button.button(win,Point(12.3,8.4),1.8,1.0,'right')
    left1=button.button(win,Point(12.3,7.1),1.8,1.0,'left')#
    Image(Point(12.3,20),'20111202.gif').draw(win)
    Text(Point(11.4,19),'next:').draw(win)
    Text(Point(11.5,15),'level:').draw(win)
    level=1
    level1=Text(Point(13.0,15),level)
    level1.draw(win)
    sp=0
    sc=0
    Text(Point(11.5,5.6),'score:').draw(win)
    score=Text(Point(12.5,5.6),sc)
    score.draw(win) 
    q=1
    window1={}
    window2=[[1,1,1,1,1,1,1,1,1,1,1,1,],
    [2,0,0,0,0,0,0,0,0,0,0,2],
    [2,0,0,0,0,0,0,0,0,0,0,2],
    [2,0,0,0,0,0,0,0,0,0,0,2],
    [2,0,0,0,0,0,0,0,0,0,0,2],
    [2,0,0,0,0,0,0,0,0,0,0,2],
    [2,0,0,0,0,0,0,0,0,0,0,2],
    [2,0,0,0,0,0,0,0,0,0,0,2],
    [2,0,0,0,0,0,0,0,0,0,0,2],
    [2,0,0,0,0,0,0,0,0,0,0,2],
    [2,0,0,0,0,0,0,0,0,0,0,2],
    [2,0,0,0,0,0,0,0,0,0,0,2],
    [2,0,0,0,0,0,0,0,0,0,0,2],
    [2,0,0,0,0,0,0,0,0,0,0,2],
    [2,0,0,0,0,0,0,0,0,0,0,2],
    [2,0,0,0,0,0,0,0,0,0,0,2],
    [2,0,0,0,0,0,0,0,0,0,0,2],
    [2,0,0,0,0,0,0,0,0,0,0,2],
    [2,0,0,0,0,0,0,0,0,0,0,2],
    [2,0,0,0,0,0,0,0,0,0,0,2],
    [2,0,0,0,0,0,0,0,0,0,0,2],
    [3,3,3,3,3,3,3,3,3,3,3,3],
    [3,3,3,3,3,3,3,3,3,3,3,3],
    [3,3,3,3,3,3,3,3,3,3,3,3]]
    window=copy.deepcopy(window2)
    shapenumber=random.randint(0,6)
    ss2=eluosi.Squares(win,12.5,17,shapenumber)
    start_number=1
    spin_derection=1
    while q==1:
        pp=win.getMouse()
        if start.judge(pp):#under this condition,the game will start until user lose the game or the order of stop is got
         qq1=1#line146
         qq2=1#line153
         while qq1==1:
          if stop.judge(pp):
                        qq1=0
                        for rect in range(len(window1)):
                            rect.undraw()
                        window1={}        
                        window=copy.deepcopy(window2)
                        break
          if pause.judge(pp):
              pp=Point(0,0)
              qq2=-qq2#a varible to decide if to move
              time.sleep(1.0)
              ppp=win.checkMouse()
              if type(ppp)==type(pp):
                  pp=ppp
          if qq1==1 and qq2==1:#move as usual
            qq3=1#line170,
            if start_number==1:#creat a new Squares
                start_number=0
                ss2.move(-6.5,4.0)
                ss1=ss2#ss1 refer to the squares moving now
                shapenumber=random.randint(0,6)
                ss2=eluosi.Squares(win,12.5,17,shapenumber)#ss2 refer to the squares waiting to move, which are drawn in the rihgt side of the window
            if up.judge(pp):#spin
                ran=(ss1.position_number+spin_derection)%(len(ss1.shape))
                position=ss1.shape[ran]
                spin=1#a controlling key
                for i in range(4):#check if it can spin
                    a=window[int(position[i][1]+ss1.y)][int(position[i][0]+ss1.x)]
                    if a==2 or a==1:
                        spin=spin+1
                if spin==1:
                    ss1.spin(spin_derection)
                    qq3=0
            dx=0
            dy=-1
            if left.judge(pp):
                dx=-1
                dy=0
            elif right.judge(pp):
                dx=1
                dy=0
            for i in range(4):#check whether the squares can be moved as the user want.if not,change the derection to down
                b=int(ss1.x+dx+ss1.position[i][0])
                a=int(ss1.y+dy+ss1.position[i][1])
                a=window[a][b]
                if a==2 or a==1:
                    dx=0
                    dy=-1 
            if down.judge(pp):
                dy=-1
            move=1
            for i in range(4):#this is a judgement related to the judgement above
                b=int(ss1.x+dx+ss1.position[i][0])
                a=int(ss1.y+dy+ss1.position[i][1])
                a=window[a][b]
                if a==2:
                    dx=0
                    dy=-1 
                elif a==1:
                    move=0
                    start_number=1
            if start_number==1:#when the squares arrive the bottom, judge whether there is any row to be full and if the aquares has been over the window
                for i in range(4):
                    b=int(ss1.x+ss1.position[i][0])
                    a=int(ss1.y+ss1.position[i][1])
                    window[a][b]=1
                    window1[(a,b)]=ss1.ss[i]
                b=0
                for i in range(20):
                    a=0
                    for j in range(10):
                        if window[i+1-b][j+1]==0:
                            break
                        else:
                            a=a+1
                    if a==10:
                        for k in range(10):
                            window[i+1-b][k+1]=0
                            window1[(i+1-b,k+1)].undraw()
                            del window1[(i+1-b,k+1)]
                        for ii in range(i-b+2,21):
                            for jj in range(10):
                                if window[ii][jj+1]==1:
                                    window[ii][jj+1]=0
                                    window[ii-1][jj+1]=1
                                    window1[(ii,jj+1)].move(0,-1.0)
                                    window1[(ii-1,jj+1)]=window1[(ii,jj+1)]
                                    del window1[(ii,jj+1)]
                                #for  i in range(11):
                                    #print window[11-i][1:10]
                                #print '----------------------------------------------'
                        b=b+1
                aa=0
                for i in range(10):#check if the squares has arrived the top of the window
                    if window[21][i+1]==1:
                        aa=1
                if aa==1:
                        c=Image(Point(5,10),'101gameover.gif')
                        c.draw(win)
                        time.sleep(3)
                        c.undraw()
                        for rect in range(len(window1)):
                            rect.undraw()
                        window1={}
                            
                                
                        window=copy.deepcopy(window2)
                        break
            if move==1 and qq3==1:
                ss1.move(dx,dy)
            time.sleep(0.5-level*0.05)
            
            pp=Point(0,0)
            ppp=win.checkMouse()
            if type(ppp)==type(pp):
                pp=ppp
        if soon.judge(pp):
            level=level+1
            level1.setText(level)
        if slow.judge(pp) and level>1:
            level=level-1
            level1.setText(level)
        if right.judge(pp):
            spin_derection=1
        if left.judge(pp):
            spin_derection=-1
        if mode1.judge(pp):
            mode=1
        if mode2.judge(pp):
            mode=2
        if eexit.judge(pp):
            win.close()
            q=0
        
   
main()

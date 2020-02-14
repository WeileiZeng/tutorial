import random
#import py
import button
import copy
import time
import graphics#this program is based on graphics
import eluosi
from graphics import *
class Squares():#Squares is a set of four squares
    def __init__(self,win,x,y,shapenumber):
        self.shapenumber=shapenumber
        self.y=y
        self.x=x#(x,y) is the position of the squares whose number is [0,0] in the four 
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
            [[[-1,0],[0,1],[0,0],[1,0]],[[0,1],[0,0],[-1,0],[0,-1]],
             [[-1,0],[0,-1],[0,0],[1,0]],[[0,1],[0,0],[1,0],[0,-1]]],#4shangxing
            [[[-1,0],[0,0],[1,0],[1,1]],[[0,1],[0,0],[ 0,-1],[1,-1]],
             [[-1,-1],[-1,0],[0,0],[1,0]],[[-1,1],[0,1],[0,0],[0,-1]]],#5zheng7
            [[[-1,1],[-1,0],[0,0],[1,0]],[[0,1],[1,1],[0,0],[0,-1]],
             [[-1,0],[0,0],[1,0],[1,-1]],[[-1,-1],[0,-1],[0,0],[0,1]]]]#6fan7   
        shape1=shapes[shapenumber]#choose the shape of the 4 squares
        self.shape=shape1#a list containing serevel lists in it
        self.ss=[]#contain the four squares,so you can control them seprately as objects in graphics
        ran=random.randint(0,len(shape1)-1)#decide the first derection of the squares in certain shapes
        self.position_number=ran#ran is related to spinning
        shape2=shape1[ran]#'shape2' contains the positions of the 4 squares
        self.position=shape2#position of the four squares 
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
    b="        INTRODUCTION\n    The button 'soon' and 'slow' can\nbe pressed any time to change the \nspeed,the higher the speed is, the \nfaster your scores increase.     \n    the mode1 is common mode,mode2 is\ndifficulter,in which there will be an  \nextral row in the bottom of the window\n    the buttons \'right\'and \'left\' can     \nchange the derection when the squares\n', 'spin.                    \n    if you want to exit before game is\nover,press \'stop\' first!       \n"
    txt=Text(Point(5,10),b)
    txt_close=button.button(win,Point(9,6),1.5,0.8,'close')#to end introduction
    txt_close.close()
    up=button.button(win,Point(5,-0.5),1.5,1.5,'/\\')
    down=button.button(win,Point(5,-2.2),1.5,1.5,'\/')
    left=button.button(win,Point(3.3,-2.2),1.5,1.5,'<==')
    right=button.button(win,Point(6.7,-2.2),1.5,1.5,'==>')#moving derection
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
    left1=button.button(win,Point(12.3,7.1),1.8,1.0,'left')#to change the drection of spinning,different to button 'right' and 'left'
    Image(Point(12.3,20),'20111202.gif').draw(win)#the image 'eluosifangkuai'
    Text(Point(11.4,19),'next:').draw(win)
    Text(Point(11.5,15),'level:').draw(win)
    level=1
    level1=Text(Point(13.0,15),level)
    level1.draw(win)
    sp=0
    scores=0
    Text(Point(11.5,5.6),'score:').draw(win)
    score=Text(Point(12.5,5.6),scores)
    score.draw(win)
    color=['red','blue','yellow','green','orange','purple','gray']
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
    [3,3,3,3,3,3,3,3,3,3,3,3]]#the top of the list represents the bottom of the window
    window=copy.deepcopy(window2)
    shapenumber=random.randint(0,6)
    next_squares=eluosi.Squares(win,12.5,17,shapenumber)
    spin_derection=1#reperesent right
    for bb in [start,eexit,introduction,soon,slow,mode1,mode2,right1,left1]:
        bb.active()
    mode=1
    mode1_light=Circle(Point(11.0,11.0),0.3)
    mode1_light.setFill('green')
    mode1_light.setOutline('green')
    mode1_light.draw(win)
    mode2_light=Circle(Point(11.0,9.7),0.3)
    mode2_light.setFill('green')
    mode2_light.setOutline('green')
    right_light=Circle(Point(11.0,8.4),0.3)
    right_light.setFill('green')
    right_light.setOutline('green')
    right_light.draw(win)
    left_light=Circle(Point(11.0,7.1),0.3)
    left_light.setFill('green')
    left_light.setOutline('green')
    q=1
    while q==1:
        pp=win.getMouse()
        if introduction.judge(pp):
            txt.draw(win)
            txt_close.draw()
            for bb in [soon,slow,mode1,mode2,right1,left1,start,introduction,eexit]:
                bb.unactive()
            txt_close.active()
            while not txt_close.judge(pp):
                pp=win.getMouse()
            txt.undraw()
            txt_close.close()
            for bb in [soon,slow,mode1,mode2,right1,left1,start,introduction,eexit]:
                bb.active()
            
        if soon.judge(pp) and level<13:
            level=level+1
            level1.setText(level)
        elif slow.judge(pp) and level>1:
            level=level-1
            level1.setText(level)
        elif right1.judge(pp) and spin_derection==-1:
            spin_derection=1
            right_light.draw(win)
            left_light.undraw()
        elif left1.judge(pp) and spin_derection==1:
            spin_derection=-1
            left_light.draw(win)
            right_light.undraw()
        elif mode1.judge(pp) and mode==2:
            mode=1
            mode2_light.undraw()
            mode1_light.draw(win)
        elif mode2.judge(pp) and mode==1:
            mode=2
            mode1_light.undraw()
            mode2_light.draw(win)
        elif eexit.judge(pp):
            win.close()
            q=0
        elif start.judge(pp):#under this condition,the game will start until user lose the game or the order of stop is got
         stop_number=1#a controling number of stop
         pause_number=1#a controling number of pausing
         start_number=1
         down_number=0
         mode_number=0
         mode_number2=1
         for bb in [up,down,right,left,pause,stop]:
             bb.active()
         eexit.unactive()
         introduction.unactive()
         while stop_number==1:
          if pause_number==-1:#if it's pausing now,wait to get a new order
              pp=win.getMouse()
          if stop.judge(pp):
                        eexit.active()
                        introduction.active()
                        stop_number=0#an controling number of stop
                        scores=0#scores
                        for rect in window1.values():
                            rect.undraw()
                        current_squares.undraw()
                        window1={}        
                        window=copy.deepcopy(window2)
                        break
          if pause.judge(pp):
              pause_number=-pause_number#a varible to decide if to move
          if soon.judge(pp) and level<13:
            level=level+1
            level1.setText(level)
          if slow.judge(pp) and level>1:
            level=level-1
            level1.setText(level)
          if right.judge(pp):
            spin_derection=1
          if left.judge(pp):
            spin_derection=-1
          if stop_number==1 and pause_number==1:#move as usual
            qq3=1#line170,
            if start_number==1:#creat a new Squares
                start_number=0
                next_squares.move(-6.5,4.0)
                current_squares=next_squares#current_squares refer to the squares moving now
                shapenumber=random.randint(0,6)
                next_squares=eluosi.Squares(win,12.5,17,shapenumber)#next_squares refer to the squares waiting to move, which are drawn in the rihgt side of the window
            if up.judge(pp):#spin
                ran=(current_squares.position_number+spin_derection)%(len(current_squares.shape))
                position=current_squares.shape[ran]
                spin_number=1#a controlling key
                for i in range(4):#check if it can spin
                    a=window[int(position[i][1]+current_squares.y)][int(position[i][0]+current_squares.x)]
                    if a==2 or a==1:
                        spin_number=spin_number+1
                if spin_number==1:
                    current_squares.spin(spin_derection)
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
                b=int(current_squares.x+dx+current_squares.position[i][0])
                a=int(current_squares.y+dy+current_squares.position[i][1])
                a=window[a][b]
                if a==2 or a==1:
                    dx=0
                    dy=-1
            move=1
            for i in range(4):#this is a judgement related to the judgement above
                b=int(current_squares.x+dx+current_squares.position[i][0])
                a=int(current_squares.y+dy+current_squares.position[i][1])
                a=window[a][b]
                if a==2:
                    dx=0
                    dy=-1 
                elif a==1:
                    move=0
                    start_number=1
            if start_number==1:#when the squares arrive the bottom,judge whether
#there is any row to be full and if the aquares has been over the window
                for i in range(4):#change the number in new positions in window from 0 to 1
                    b=int(current_squares.x+current_squares.position[i][0])
                    a=int(current_squares.y+current_squares.position[i][1])
                    window[a][b]=1
                    window1[(a,b)]=current_squares.ss[i]
                b=0#record the number of full row
                down_number=0
                for i in range(20):
                    a=0
                    for j in range(10):#calculate the number of squares in row i
                        if window[i+1-b][j+1]==0:
                            break
                        else:
                            a=a+1
                    if a==10:#meabs this row is full 
                        scores=scores+level*(b+1)
                        score.setText(scores)
                        for k in range(10):#remove the squares in row i
                            window[i+1-b][k+1]=0
                            window1[(i+1-b,k+1)].undraw()
                            del window1[(i+1-b,k+1)]
                        for ii in range(i-b+2,21):#move down the squares over row i 
                            for jj in range(10):
                                if window[ii][jj+1]==1:
                                    window[ii][jj+1]=0
                                    window[ii-1][jj+1]=1
                                    window1[(ii,jj+1)].move(0,-1.0)
                                    window1[(ii-1,jj+1)]=window1[(ii,jj+1)]#correct the reference from window1 to the squares in the window 
                                    del window1[(ii,jj+1)]
                        b=b+1
                if mode==2 and int(mode_number/100)==mode_number2:
                #in mode2,after the given time, it will product an extra row with serveral squares in it
                    mode_number2 +=1
                    for i in range(19):#move up the current squares to empty the first row.
                        row =19-i
                        for j in range(10):
                            col=j+1
                            if window[row][col]==1:
                                window[row+1][col]=1
                                window[row][col]=0
                                window1[(row,col)].move(0,1.0)
                                window1[(row+1,col)]=window1[(row,col)]
                                del window1[(row,col)]
                    for i in range(10):#product the new row
                        a=random.randint(1,3)
                        if a in [2,3]:
                            window[1][i+1]=1
                            sq=Rectangle(Point(i+1-0.5,1-0.5),Point(i+1+0.5,1+0.5))
                            color_number=random.randint(0,6)
                            sq.setFill(color[color_number])
                            sq.setOutline(color[color_number])
                            sq.draw(win)
                            window1[(1,i+1)]=sq               
                aa=0
                for i in range(10):#check if the squares has arrived the top of the window
                    if window[21][i+1]==1:
                        aa=1
                if aa==1:
                        
                        c=Image(Point(6,10),'101gameover.gif')
                        c.draw(win)
                        time.sleep(3)
                        c.undraw()
                        current_squares.undraw()
                        for rect in window1.values():
                            rect.undraw()
                        window1={}
                        scores=0
                        window=copy.deepcopy(window2)
                        break
            if move==1 and qq3==1:
                current_squares.move(dx,dy)
            if down.judge(pp):
                down_number=1#a passcard to move the squares down
            if down_number==0:
                time.sleep(2.0/(1+level))
                mode_number +=1
            pp=Point(0,0)#escape point pp to be judged again
            ppp=win.checkMouse()
            if type(ppp)==type(pp):
                pp=ppp
   
main()

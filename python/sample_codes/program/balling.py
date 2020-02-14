# -*- coding: cp936 -*-
#this programme is aimed to make the programmers ideal game concept come true,and
#this game is called angry ball which is like the game called "angry bird"which has been
#popular for a so long time,and i just use the idea shown in the game "angry bird"
#and anyway you are supposed to release a little ball which has the uncertain initial
#velosity and the angle of the initial velosity,then just click the screen to make the
#initial velosity and the angle of the initial velosity,after that the ball will go
#in his own way which is ruled by the physics laws ,and you can modify the state of
#the ball when it is flying ,finally the little ball will hit the object ,if it is
#fulfill the requirement ,you will get some points as the award.




from graphics import*
from threading import*
from string import*
import string
import threading
import graphics
import time
import math
lock = threading.Lock()

class initialstate:
      def __init__(self,x,y,v0):
          self.x=x
          self.y=y
          self.v0=v0
      def cos(self):
          return float(self.x-50)/self.v0
      def sin(self):
          return float(self.y-50)/self.v0


class split:
      def __init__(self,vx,vy,theta):
          self.v=(vx**2+vy**2)**0.5
          self.theta=math.atan(vy/vx)+theta*math.pi/180

      def vx(self):
          return float((self.v)*math.cos(self.theta))
      def vy(self):
          return float((self.v)*math.sin(self.theta))
     




win=graphics.GraphWin("Angry Ball",1000,500)
win.setCoords(0,0,1000,500) 
win.setBackground("white")
p1=Point(50,50)
c1=Circle(p1,5)
c1.setFill("blue")
p1=Point(50,50)
c2=Circle(p1,20)
p1=Point(50,50)
c3=Circle(p1,30)
p1=Point(50,50)
c4=Circle(p1,40)
c2.draw(win)
c1.draw(win)
c3.draw(win)
c4.draw(win)
pp=Point(700,250)
cc=Circle(pp,100)
cc.setFill("yellow")
pp1=Point(700,360)
cc1=Circle(pp1,10)
pp2=Point(700,140)
cc2=Circle(pp2,10)
pp3=Point(590,250)
cc3=Circle(pp3,10)
pp4=Point(810,250)
cc4=Circle(pp4,10)
cc1.setFill("red")
cc2.setFill("red")
cc3.setFill("red")
cc4.setFill("red")
cc1.draw(win)
cc2.draw(win)
cc3.draw(win)
cc4.draw(win)
cc.draw(win)
x1=50
y1=50
x2=0
x3=0
y2=0
y3=0
vx=0
vy=0
score=0

def release11():
    global x1,y1,vx,vy
    p2=win.getMouse()
    r=((p2.getX()-50)**2+(p2.getY()-50)**2)**0.5
    if r>=5 and r<=40:
       v=3*r
       a=initialstate(p2.getX(),p2.getY(),r)
       vx=v*(a.cos())
       vy=v*(a.sin())
    dt=0.1
    try:
          p1=Point(x1,y1)
          c1=Circle(p1,5)
          c1.setFill("blue")
          p1.setFill("yellow")
          c1.draw(win)
          p1.draw(win)
    except:
            pass
    for i in range(1,300000,1): 
        time.sleep(0.01)
        if x1>400:
           vx=vx
           vy=vy+9.8*dt
           dx1=vx*dt
           dy1=vy*dt
           x1=x1+vx*dt
           y1=y1+vy*dt
           p1=Point(x1,y1)
           p1.setFill("yellow")
           try:
                 c1.move(dx1,dy1)
                 p1.draw(win)
           except:
                 pass
        if x1<=400:
           vx=vx
           vy=vy-9.8*dt
           dx1=vx*dt
           dy1=vy*dt
           x1=x1+vx*dt
           y1=y1+vy*dt
           p1=Point(x1,y1)
           p1.setFill("yellow")
           try:
                 c1.move(dx1,dy1)
                 p1.draw(win)
           except:
                 pass
        if x1>1000:
           break
    print "11" 

def circle11():#target made up of recycling balls
    global x1,y1
    dtt=0.01
    for i in range(1,300000,1):
        #lock.acquire()
        dxx4=-110*math.sin(0.01*i)*dtt
        dyy4=110*math.cos(0.01*i)*dtt
        dxx1=-110*math.sin(0.01*i+math.pi/2)*dtt
        dyy1=110*math.cos(0.01*i+math.pi/2)*dtt
        dxx3=-110*math.sin(0.01*i+math.pi)*dtt
        dyy3=110*math.cos(0.01*i+math.pi)*dtt
        dxx2=-110*math.sin(0.01*i+3*math.pi/2)*dtt
        dyy2=110*math.cos(0.01*i+3*math.pi/2)*dtt
        try:
              cc2.move(dxx2,dyy2)
              cc4.move(dxx4,dyy4)
              cc1.move(dxx1,dyy1)
              cc3.move(dxx3,dyy3)
              pp1.move(dxx1,dyy1)
              pp2.move(dxx2,dyy2)
              pp3.move(dxx3,dyy3)
              pp4.move(dxx4,dyy4)
              time.sleep(0.01)
        except:
              pass
        #lock.release()
        if x1>1000:
           break
    print "12"

def score11():
    global x1,y1
    global score
    k1=0
    k2=0
    k3=0
    k4=0
    for i in range(1,30000,1): 
        lock.acquire()
        xx1=pp1.getX()
        yy1=pp1.getY()
        xx2=pp2.getX()
        yy2=pp2.getY()
        xx3=pp3.getX()
        yy3=pp3.getY()
        xx4=pp4.getX()
        yy4=pp4.getY()
        r1=((x1-xx1)**2+(y1-yy1)**2)**0.5
        r2=((x1-xx2)**2+(y1-yy2)**2)**0.5
        r3=((x1-xx3)**2+(y1-yy3)**2)**0.5
        r4=((x1-xx4)**2+(y1-yy4)**2)**0.5
        if 0<=r1<=15:
           cc1.undraw()
           if k1==0:
              score=score+500
              k1+=1
        if 0<=r2<=15:
           cc2.undraw()
           if k2==0:
              score=score+500
              k2+=1           
        if 0<=r3<=15:
           cc3.undraw()
           if k3==0:
              score=score+500
              k3+=1
        if 0<=r4<=15:
           cc4.undraw()
           if k4==0:
              score=score+500
              k4+=1
        lock.release()         
        if x1>1000:
           break 
    #lock.acquire()
    try:
          score1=str(score)
          text1=Text(Point(100,400),"your final score is"+"     "+score1)
          text1.draw(win)
    except:
          pass
    #lock.release()
    print "13"
def series1():
      t1=threading.Thread(target=release11,args=())
      t2=threading.Thread(target=circle11,args=())
      t3=threading.Thread(target=score11,args=())
      threads=[t1,t2,t3]
      for i in range(0,3,1):
        threads[i].start()
      for i in range(0,3,1):
        threads[i].join()          

      time.sleep(2)
      win.close()
win.close()
#series1()

         
#time.sleep(2)

#the second part of the first game 第一局中的第二次发射：  
# -*- coding: cp936 -*-
class initialstate:
      def __init__(self,x,y,v0):
          self.x=x
          self.y=y
          self.v0=v0
      def cos(self):
          return float(self.x-50)/self.v0
      def sin(self):
          return float(self.y-50)/self.v0


win=graphics.GraphWin("Angry Ball",1000,500)
win.setCoords(0,0,1000,500) 
win.setBackground("white")
p1=Point(50,50)
c1=Circle(p1,5)
c1.setFill("blue")
p1=Point(50,50)
c2=Circle(p1,20)
p1=Point(50,50)
c3=Circle(p1,30)
p1=Point(50,50)
c4=Circle(p1,40)
c2.draw(win)
c1.draw(win)
c3.draw(win)
c4.draw(win)
pp=Point(700,250)
cc=Circle(pp,100)
cc.setFill("yellow")
pp1=Point(700,360)
cc1=Circle(pp1,10)
pp2=Point(700,140)
cc2=Circle(pp2,10)
pp3=Point(590,250)
cc3=Circle(pp3,10)
pp4=Point(810,250)
cc4=Circle(pp4,10)
cc1.setFill("red")
cc2.setFill("red")
cc3.setFill("red")
cc4.setFill("red")
cc1.draw(win)
cc2.draw(win)
cc3.draw(win)
cc4.draw(win)
cc.draw(win)
x1=50
y1=50
x2=0
x3=0
y2=0
y3=0
      
def release22():
    global x1,y1,x2,y2,x3,y3
    print "click the circle"
    p2=win.getMouse()
    print "mouse have been got"
    r=((p2.getX()-50)**2+(p2.getY()-50)**2)**0.5
    if r>=5 and r<=40:
       v=3*r
       a=initialstate(p2.getX(),p2.getY(),r)
       vx=v*(a.cos())
       vy=v*(a.sin())
    dt=0.1
    p1=Point(x1,y1)
    c1=Circle(p1,5)
    c1.setFill("blue")
    p1.setFill("yellow")
    try:
          c1.draw(win)
          p1.draw(win)
    except:
            pass
    for i in range(1,300000,1):        
        if x1>500 :
           c1.undraw()
           vx2=vx
           vy2=vy
           vx3=vx
           vy3=vy
           v=(vx**2+vy**2)**0.5
           theta1=math.atan(vy/vx)+10*math.pi/180
           theta2=math.atan(vy/vx)-10*math.pi/180
           vx2=float((v)*math.cos(theta1))
           vx3=float((v)*math.cos(theta2))
           vy2=float((v)*math.sin(theta1))
           vy3=float((v)*math.sin(theta2))
           x2=x1
           y2=y1
           x2=x1
           y2=y1
           x3=x1
           y3=y1
           try:
                 p1=Point(x1,y1)
                 p2=Point(x2,y2)
                 p3=Point(x3,y3)
                 c1=Circle(p1,5)
                 c1.setFill("blue")
                 c2=Circle(p2,5)
                 c2.setFill("blue")
                 c3=Circle(p3,5)
                 c3.setFill("blue")
                 
                 c1.draw(win)
                 c2.draw(win)
                 c3.draw(win)    
                 p1.setFill("yellow")
                 p2.setFill("yellow")
                 p3.setFill("yellow")
           except:
            pass
           for i in range(1,300000,1):
               if x1<=1000 or x2<=1000 or x3<=1000:
                        dt=0.1
                        vx=vx
                        vy=vy-9.8*dt
                        vx2=vx2
                        vy2=vy2-9.8*dt
                        vx3=vx3
                        vy3=vy3-9.8*dt
                        dx1=vx*dt
                        dy1=vy*dt
                        dx2=vx2*dt
                        dy2=vy2*dt
                        dx3=vx3*dt
                        dy3=vy3*dt
                        x1=x1+dx1
                        y1=y1+dy1
                        x2=x2+dx2
                        y2=y2+dy2
                        x3=x3+dx3
                        y3=y3+dy3
                        p1=Point(x1,y1)
                        p2=Point(x2,y2)
                        p3=Point(x3,y3)
                        p1.setFill("yellow")
                        p2.setFill("yellow")
                        p3.setFill("yellow")
                        #lock.acquire()
                        try:
                              p1.draw(win)
                              p2.draw(win)
                              p3.draw(win)
                              c1.move(dx1,dy1)
                              c2.move(dx2,dy2)
                              dxx4=-110*math.sin(0.01*i)*dtt
                              dyy4=110*math.cos(0.01*i)*dtt
                              dxx1=-110*math.sin(0.01*i+math.pi/2)*dtt
                              dyy1=110*math.cos(0.01*i+math.pi/2)*dtt
                              dxx3=-110*math.sin(0.01*i+math.pi)*dtt
                              dyy3=110*math.cos(0.01*i+math.pi)*dtt
                              dxx2=-110*math.sin(0.01*i+3*math.pi/2)*dtt
                              dyy2=110*math.cos(0.01*i+3*math.pi/2)*dtt
                              c3.move(dx3,dy3)
                              time.sleep(0.02)
                        except:
                              pass
                        #lock.release()
               if  x1>1000 and x2>1000 and x3>1000:
                         break
        if x1<=500:
           vx=vx
           vy=vy-9.8*dt
           dx1=vx*dt
           dy1=vy*dt
           x1=x1+vx*dt
           y1=y1+vy*dt
           p1=Point(x1,y1)
           p1.setFill("yellow")
           #lock.acquire()
           try:
                 
                 c1.move(dx1,dy1)
                 p1.draw(win)
           except:
                              pass
           #lock.release()
        if x1>1000:
           break
    print  "21"
          

def circle12():#target made up of recycling balls
    print x1
    global x1
    print x1
    dtt=0.01
    for i in range(1,300000,1):
        #lock.acquire()
        
        dxx4=-110*math.sin(0.01*i)*dtt
        dyy4=110*math.cos(0.01*i)*dtt
        dxx1=-110*math.sin(0.01*i+math.pi/2)*dtt
        dyy1=110*math.cos(0.01*i+math.pi/2)*dtt
        dxx3=-110*math.sin(0.01*i+math.pi)*dtt
        dyy3=110*math.cos(0.01*i+math.pi)*dtt
        dxx2=-110*math.sin(0.01*i+3*math.pi/2)*dtt
        dyy2=110*math.cos(0.01*i+3*math.pi/2)*dtt
        try:
              cc2.move(dxx2,dyy2)
              cc4.move(dxx4,dyy4)
              cc1.move(dxx1,dyy1)
              cc3.move(dxx3,dyy3)
              pp1.move(dxx1,dyy1)
              pp2.move(dxx2,dyy2)
              pp3.move(dxx3,dyy3)
              pp4.move(dxx4,dyy4)
              time.sleep(0.01)
        except:
                              pass
        #lock.release()
        if x1>1000:
           print "x1=",x1
           break
    print  "22"

def score2():
    print "score2 starts"
    global score
    k11=0
    k12=0
    k13=0
    k14=0
    k21=0
    k22=0
    k23=0
    k24=0
    k31=0
    k32=0
    k33=0
    k34=0
    print "range(30000) starts"
    for i in range(1,30000):
        time.sleep(0.001)
        #lock.acquire()
        xx1=pp1.getX()
        yy1=pp1.getY()
        xx2=pp2.getX()
        yy2=pp2.getY()
        xx3=pp3.getX()
        yy3=pp3.getY()
        xx4=pp4.getX()
        yy4=pp4.getY()
        r11=((x1-xx1)**2+(y1-yy1)**2)**0.5
        r12=((x1-xx2)**2+(y1-yy2)**2)**0.5
        r13=((x1-xx3)**2+(y1-yy3)**2)**0.5
        r14=((x1-xx4)**2+(y1-yy4)**2)**0.5
        r21=((x2-xx1)**2+(y2-yy1)**2)**0.5
        r22=((x2-xx2)**2+(y2-yy2)**2)**0.5
        r23=((x2-xx3)**2+(y2-yy3)**2)**0.5
        r24=((x2-xx4)**2+(y2-yy4)**2)**0.5
        r31=((x3-xx1)**2+(y3-yy1)**2)**0.5
        r32=((x3-xx2)**2+(y3-yy2)**2)**0.5
        r33=((x3-xx3)**2+(y3-yy3)**2)**0.5
        r34=((x3-xx4)**2+(y3-yy4)**2)**0.5
        try:
              if 0<=r11<=15:
                 cc1.undraw()
                 if k11==0:
                    score=score+500
                    k11+=1
              if 0<=r12<=15:
                 cc2.undraw()
                 if k12==0:
                    score=score+500
                    k12+=1
              if 0<=r13<=15:
                 cc3.undraw()
                 if k13==0:
                    score=score+500
                    k13+=1
              if 0<=r14<=15:
                 cc4.undraw()
                 if k14==0:
                    score=score+500
                    k14+=1
              if 0<=r21<=15:
                 cc1.undraw()
                 if k21==0:
                    score=score+500
                    k21+=1
              if 0<=r22<=15:
                 cc2.undraw()
                 if k22==0:
                    score=score+500
                    k22+=1
              if 0<=r23<=15:
                 cc3.undraw()
                 if k23==0:
                    score=score+500
                    k23+=1
              if 0<=r24<=15:
                 cc4.undraw()
                 if k24==0:
                    score=score+500
                    k24+=1
              if 0<=r31<=15:
                 cc1.undraw()
                 if k31==0:
                    score=score+500
                    k31+=1
              if 0<=r32<=15:
                 cc2.undraw()
                 if k32==0:
                    score=score+500
                    k32+=1
              if 0<=r33<=15:
                 cc3.undraw()
                 if k33==0:
                    score=score+500
                    k33+=1
              if 0<=r34<=15:
                 cc4.undraw()
                 if k34==0:
                    score=score+500
                    k34+=1
        except:
                  pass
        #lock.release()
        if  x1>1000 and x2>1000 and x3>1000:
            print "score2 breaks"
            break 
    #lock.acquire()
    print "range(30000) stops"
    score1=str(score)
    try:
          text1=Text(Point(100,400),"your final score is"+"     "+score1)
          text1.draw(win)
    except:
            pass
    #lock.release()
    print  "23"


def series2():
    t1=threading.Thread(target=release22,args=())
    t2=threading.Thread(target=circle12,args=())
    t3=threading.Thread(target=score2,args=())
    threads=[t1,t2,t3]
    for i in range(0,3,1):
        threads[i].start()
    for i in range(0,3,1):
        threads[i].join()
    
    time.sleep(2)  
    win.close() 

series2()



time.sleep(2)

#the first release of the second game:第二局中第一次发射


win=graphics.GraphWin("Angry Ball",1000,500)
win.setCoords(0,0,1000,500)
win.setBackground("white")
p1=Point(50,50)
c1=Circle(p1,5)
c1.setFill("blue")
p1=Point(50,50)
c2=Circle(p1,20)
p1=Point(50,50)
c3=Circle(p1,30)
p1=Point(50,50)
c4=Circle(p1,40)
c2.draw(win)
c1.draw(win)
c3.draw(win)
c4.draw(win)
lp1=Point(745,320)
lp2=Point(755,320)
lp3=Point(755,300)
lp4=Point(745,300)
l1=Line(lp1,lp2)
l2=Line(lp2,lp3)
l3=Line(lp3,lp4)
l4=Line(lp4,lp1)
lpp1=Point(795,365)
lpp2=Point(805,365)
lpp3=Point(805,345)
lpp4=Point(795,345)
ll1=Line(lpp1,lpp2)
ll2=Line(lpp2,lpp3)
ll3=Line(lpp3,lpp4)
ll4=Line(lpp4,lpp1)
j1=Rectangle(Point(695,0),Point(705,245))
j2=Rectangle(Point(650,245),Point(705,255))
j3=Rectangle(Point(745,0),Point(755,290))
j4=Rectangle(Point(700,290),Point(755,300))
j5=Rectangle(Point(795,0),Point(805,335))
j6=Rectangle(Point(750,335),Point(805,345))
j1.setFill("brown")
j2.setFill("green")
j3.setFill("brown")
j4.setFill("green")
j5.setFill("brown")
j6.setFill("green")
j1.draw(win)
j2.draw(win)
j3.draw(win)
j4.draw(win)
j5.draw(win)
j6.draw(win)
l1.draw(win)
l2.draw(win)
l3.draw(win)
l4.draw(win)
ll1.draw(win)
ll2.draw(win)
ll3.draw(win)
ll4.draw(win)
ppp=Point(700,265)
ccc=Circle(ppp,10)
ccc.setFill("blue")
ccc.draw(win)
x1=50
y1=50
vx=0
vy=0
s1=0
s2=0
s3=0




class initialstate:
      def __init__(self,x,y,v0):
          self.x=x
          self.y=y
          self.v0=v0
      def cos(self):
          return float(self.x-50)/self.v0
      def sin(self):
          return float(self.y-50)/self.v0

def release14():
    global x1,y1,vx,vy
    p2=win.getMouse()
    r=((p2.getX()-50)**2+(p2.getY()-50)**2)**0.5
    if r>=5 and r<=40:
       v=3*r
       a=initialstate(p2.getX(),p2.getY(),r)
       vx=v*(a.cos())
       vy=v*(a.sin())
    dt=0.1
    p1=Point(x1,y1)
    c1=Circle(p1,5)
    c1.setFill("blue")
    p1.setFill("yellow")
    c1.draw(win)
    p1.draw(win)
    for i in range(1,300000,1): 
        time.sleep(0.01)
        if x1<=2000:
           vx=vx
           vy=vy-9.8*dt
           dx1=vx*dt
           dy1=vy*dt
           x1=x1+vx*dt
           y1=y1+vy*dt
           p1=Point(x1,y1)
           p1.setFill("yellow")
           lock.acquire()
           c1.move(dx1,dy1)
           p1.draw(win)
           lock.release()
        if x1>2000:
           break
    print  "41"      

def collision14():  #targets of a big ball which can move when collided
    global s1,x1,y1,vx
    dt=0.01
    for i in range(1,30000,1):
        time.sleep(0.01)
        distance=((x1-700)**2+(y1-265)**2)**0.5
##        print distance
        if distance<=20:
                   for i in range(1,30000,1):                      
                       ayy=-9.8
                       vyy=ayy*i*0.1
                       dyy=vyy*dt
                       vxx=vx/2
                       dxx=vxx*dt
                       lock.acquire()
                       s1+=1
                       ppp.move(dxx,dyy)
                       ccc.move(dxx,dyy)
                       time.sleep(0.005)
                       lock.release()
                       if x1>1500:
                          break
        if x1>1500:
           break
    print  "42"

def collision24():
    global s2,x1,y1,vx
    for i in range(1,30000,1):
        distance2=((x1-750)**2+(y1-310)**2)**0.5
##        print distance2
        if distance2<=10:
              for i in range(1,30000,1):
                  lock.acquire()
                  s2+=1
                  ldx1=(vx+(5*5**0.5)*math.sin((math.pi-math.atan(2))-50*i))*0.01
                  ldy1=(-9.8*i-(5*5**0.5)*math.cos((math.pi-math.atan(2))-50*i))*0.01      
                  ldx2=(vx+(5*5**0.5)*math.sin(math.atan(2)-50*i))*0.01
                  ldy2=(-9.8*i-(5*5**0.5)*math.cos(math.atan(2)-50*i))*0.01
                  ldx3=(vx+(5*5**0.5)*math.sin(-math.atan(2)-50*i))*0.01
                  ldy3=(-9.8*i-(5*5**0.5)*math.cos(-math.atan(2)-50*i))*0.01
                  ldx4=(vx+(5*5**0.5)*math.sin(-(math.pi-math.atan(2))-50*i))*0.01
                  ldy4=(-9.8*i-(5*5**0.5)*math.cos(-(math.pi-math.atan(2))-50*i))*0.01
                  lp1.move(ldx1,ldy1)
                  lp2.move(ldx2,ldy2)
                  lp3.move(ldx3,ldy3)
                  lp4.move(ldx4,ldy4)
                  l1=Line(lp1,lp2)
                  l2=Line(lp2,lp3)
                  l3=Line(lp3,lp4)
                  l4=Line(lp4,lp1)
                  l1.draw(win)
                  l2.draw(win)
                  l3.draw(win)
                  l4.draw(win)
                  time.sleep(0.06)
                  l1.undraw()
                  l2.undraw()
                  l3.undraw()
                  l4.undraw()
                  lock.release()
                  if x1>1500:
                          break
        if x1>1500:
            break
    print  "43"              

def collision34():
    global s3,x1,y1,vx
    for i in range(1,30000,1):
        time.sleep(0.01)
        distance3=((x1-800)**2+(y1-330)**2)**0.5
##        print distance3
        if distance3<=10:
              for i in range(1,30000,1):                  
                  lock.acquire()
                  s3+=1
                  lldx1=(vx+(5*5**0.5)*math.sin((math.pi-math.atan(2))-50*i))*0.01
                  lldy1=(-9.8*i-(5*5**0.5)*math.cos((math.pi-math.atan(2))-50*i))*0.01      
                  lldx2=(vx+(5*5**0.5)*math.sin(math.atan(2)-50*i))*0.01
                  lldy2=(-9.8*i-(5*5**0.5)*math.cos(math.atan(2)-50*i))*0.01
                  lldx3=(vx+(5*5**0.5)*math.sin(-math.atan(2)-50*i))*0.01
                  lldy3=(-9.8*i-(5*5**0.5)*math.cos(-math.atan(2)-50*i))*0.01
                  lldx4=(vx+(5*5**0.5)*math.sin(-(math.pi-math.atan(2))-50*i))*0.01
                  lldy4=(-9.8*i-(5*5**0.5)*math.cos(-(math.pi-math.atan(2))-50*i))*0.01
                  lpp1.move(lldx1,lldy1)
                  lpp2.move(lldx2,lldy2)
                  lpp3.move(lldx3,lldy3)
                  lpp4.move(lldx4,lldy4)
                  ll1=Line(lpp1,lpp2)
                  ll2=Line(lpp2,lpp3)
                  ll3=Line(lpp3,lpp4)
                  ll4=Line(lpp4,lpp1)
                  ll1.draw(win)
                  ll2.draw(win)
                  ll3.draw(win)
                  ll4.draw(win)
                  time.sleep(0.06)
                  ll1.undraw()
                  ll2.undraw()
                  ll3.undraw()
                  ll4.undraw()
                  lock.release()
                  if x1>1500:
                          break
        if x1>1500:
            break
    print  "44"                  

def score4():
    global score,s1,s2,s3
    if s1!=0:
          score=score+500
    if s2!=0:
          score=score+500
    if s3!=0:
          score=score+500
    lock.acquire()
    score1=str(score)
    text1=Text(Point(100,400),"your final score is"+"     "+score1)
    text1.draw(win)
    lock.release()
    
def series4():
    t1=threading.Thread(target=release14,args=())
    t2=threading.Thread(target=collision14,args=())
    t3=threading.Thread(target=collision24,args=())
    t4=threading.Thread(target=collision34,args=())
    threads=[t1,t2,t3,t4]
    for i in range(0,4,1):
        threads[i].start()
    for i in range(0,4,1):
        threads[i].join()          


    score4()
    print "5"
    time.sleep(2)
    win.close()
   
series4()

time.sleep(5)

#the second release of the second game:第二局中第二次发射


# -*- coding: cp936 -*-
from graphics import*
from threading import*
from string import*
import string
import threading
import graphics
import time
import math
lock = threading.Lock()
win=graphics.GraphWin("Angry Ball",1000,500)
win.setCoords(0,0,1000,500)
win.setBackground("white")
p1=Point(50,50)
c1=Circle(p1,5)
c1.setFill("blue")
p1=Point(50,50)
c2=Circle(p1,20)
p1=Point(50,50)
c3=Circle(p1,30)
p1=Point(50,50)
c4=Circle(p1,40)
c2.draw(win)
c1.draw(win)
c3.draw(win)
c4.draw(win)
lp1=Point(745,320)
lp2=Point(755,320)
lp3=Point(755,300)
lp4=Point(745,300)
l1=Line(lp1,lp2)
l2=Line(lp2,lp3)
l3=Line(lp3,lp4)
l4=Line(lp4,lp1)
lpp1=Point(795,365)
lpp2=Point(805,365)
lpp3=Point(805,345)
lpp4=Point(795,345)
ll1=Line(lpp1,lpp2)
ll2=Line(lpp2,lpp3)
ll3=Line(lpp3,lpp4)
ll4=Line(lpp4,lpp1)
j1=Rectangle(Point(695,0),Point(705,245))
j2=Rectangle(Point(650,245),Point(705,255))
j3=Rectangle(Point(745,0),Point(755,290))
j4=Rectangle(Point(700,290),Point(755,300))
j5=Rectangle(Point(795,0),Point(805,335))
j6=Rectangle(Point(750,335),Point(805,345))
j1.setFill("brown")
j2.setFill("green")
j3.setFill("brown")
j4.setFill("green")
j5.setFill("brown")
j6.setFill("green")
j1.draw(win)
j2.draw(win)
j3.draw(win)
j4.draw(win)
j5.draw(win)
j6.draw(win)
l1.draw(win)
l2.draw(win)
l3.draw(win)
l4.draw(win)
ll1.draw(win)
ll2.draw(win)
ll3.draw(win)
ll4.draw(win)
ppp=Point(700,265)
ccc=Circle(ppp,10)
ccc.setFill("blue")
ccc.draw(win)
x1=50
y1=50
x2=0
x3=0
y2=0
y3=0
vx=0
vy=0
s1=0
s2=0
s3=0

class initialstate:
      def __init__(self,x,y,v0):
          self.x=x
          self.y=y
          self.v0=v0
      def cos(self):
          return float(self.x-50)/self.v0
      def sin(self):
          return float(self.y-50)/self.v0

class split:
      def __init__(self,vx,vy,theta):
          self.v=(vx**2+vy**2)**0.5
          self.theta=math.atan(vy/vx)+theta*math.pi/180

      def vx(self):
          return float((self.v)*math.cos(self.theta))
      def vy(self):
          return float((self.v)*math.sin(self.theta))

def release25():
    global x1,y1,x2,y2,x3,y3,vx,vy
    p2=win.getMouse()
    r=((p2.getX()-50)**2+(p2.getY()-50)**2)**0.5
    if r>=5 and r<=40:
       v=3*r
       a=initialstate(p2.getX(),p2.getY(),r)
       vx=v*(a.cos())
       vy=v*(a.sin())
    dt=0.1
    p1=Point(x1,y1)
    c1=Circle(p1,5)
    c1.setFill("blue")
    p1.setFill("yellow")
    c1.draw(win)
    p1.draw(win)
    for i in range(1,300000,1):        
        if x1>500 :
           c1.undraw()
           vx2=vx
           vy2=vy
           vx3=vx
           vy3=vy
           v=(vx**2+vy**2)**0.5
           theta1=math.atan(vy/vx)+10*math.pi/180
           theta2=math.atan(vy/vx)-10*math.pi/180
           vx2=float((v)*math.cos(theta1))
           vx3=float((v)*math.cos(theta2))
           vy2=float((v)*math.sin(theta1))
           vy3=float((v)*math.sin(theta2))
           x2=x1
           y2=y1
           x2=x1
           y2=y1
           x3=x1
           y3=y1
           p1=Point(x1,y1)
           p2=Point(x2,y2)
           p3=Point(x3,y3)
           c1=Circle(p1,5)
           c1.setFill("blue")
           c2=Circle(p2,5)
           c2.setFill("blue")
           c3=Circle(p3,5)
           c3.setFill("blue")
           c1.draw(win)
           c2.draw(win)
           c3.draw(win)    
           p1.setFill("yellow")
           p2.setFill("yellow")
           p3.setFill("yellow")   
           for i in range(1,300000,1):
               if x1<=2000 or x2<=2000 or x3<=2000:
                        dt=0.1
                        vx=vx
                        vy=vy-9.8*dt
                        vx2=vx2
                        vy2=vy2-9.8*dt
                        vx3=vx3
                        vy3=vy3-9.8*dt
                        dx1=vx*dt
                        dy1=vy*dt
                        dx2=vx2*dt
                        dy2=vy2*dt
                        dx3=vx3*dt
                        dy3=vy3*dt
                        x1=x1+dx1
                        y1=y1+dy1
                        x2=x2+dx2
                        y2=y2+dy2
                        x3=x3+dx3
                        y3=y3+dy3
                        p1=Point(x1,y1)
                        p2=Point(x2,y2)
                        p3=Point(x3,y3)
                        p1.setFill("yellow")
                        p2.setFill("yellow")
                        p3.setFill("yellow")
                        lock.acquire()
                        p1.draw(win)
                        p2.draw(win)
                        p3.draw(win)
                        c1.move(dx1,dy1)
                        c2.move(dx2,dy2)
                        c3.move(dx3,dy3)
                        time.sleep(0.001)
                        lock.release()
               if  x1>2000 and x2>2000 and x3>2000:
                         break
                         c1.undraw()
                         c2.undraw()
                         c3.undraw()
        if x1<=500:
           vx=vx
           vy=vy-9.8*dt
           dx1=vx*dt
           dy1=vy*dt
           x1=x1+vx*dt
           y1=y1+vy*dt
           p1=Point(x1,y1)
           p1.setFill("yellow")
           lock.acquire()
           c1.move(dx1,dy1)
           p1.draw(win)
           time.sleep(0.01)
           lock.release()
        if x1>=2000 or x1<=0 or y1>=500 or y1<=0:
           break
           c1.undraw()
          
def collision15():  #targets of a big ball which can move when collided
    global s1,x1,y1,x2,y2,x3,y3,vx
    dt=0.01
    for i in range(1,30000,1):
        d11=((x1-700)**2+(y1-265)**2)**0.5
        d12=((x2-700)**2+(y2-265)**2)**0.5
        d13=((x3-700)**2+(y3-265)**2)**0.5
        if (d11<=20)or(d12<=20)or(d13<=20):
                   for i in range(1,30000,1):                      
                       ayy=-9.8
                       vyy=ayy*i*0.1
                       dyy=vyy*dt
                       vxx=vx/2
                       dxx=vxx*dt
                       lock.acquire()
                       s1+=1
                       ppp.move(dxx,dyy)
                       ccc.move(dxx,dyy)
                       time.sleep(0.001)
                       lock.release()
                       if x1>2000:
                          break
        if x1>2000:
           break

def collision25():
    global s2,x1,y1,x2,y2,x3,y3,vx
    for i in range(1,30000,1):
        d21=((x1-750)**2+(y1-310)**2)**0.5
        d22=((x2-750)**2+(y2-310)**2)**0.5
        d23=((x3-750)**2+(y3-310)**2)**0.5
        if (d21<=20)or(d22<=20)or(d23<=20):
              for i in range(1,30000,1):
                  lock.acquire()
                  s2+=1
                  ldx1=(vx+(5*5**0.5)*math.sin((math.pi-math.atan(2))-0.01*i))*0.01
                  ldy1=(-9.8*i-(5*5**0.5)*math.cos((math.pi-math.atan(2))-0.01*i))*0.01      
                  ldx2=(vx+(5*5**0.5)*math.sin(math.atan(2)-0.01*i))*0.01
                  ldy2=(-9.8*i-(5*5**0.5)*math.cos(math.atan(2)-0.01*i))*0.01
                  ldx3=(vx+(5*5**0.5)*math.sin(-math.atan(2)-0.01*i))*0.01
                  ldy3=(-9.8*i-(5*5**0.5)*math.cos(-math.atan(2)-0.01*i))*0.01
                  ldx4=(vx+(5*5**0.5)*math.sin(-(math.pi-math.atan(2))-0.01*i))*0.01
                  ldy4=(-9.8*i-(5*5**0.5)*math.cos(-(math.pi-math.atan(2))-0.01*i))*0.01
                  lp1.move(ldx1,ldy1)
                  lp2.move(ldx2,ldy2)
                  lp3.move(ldx3,ldy3)
                  lp4.move(ldx4,ldy4)
                  l1=Line(lp1,lp2)
                  l2=Line(lp2,lp3)
                  l3=Line(lp3,lp4)
                  l4=Line(lp4,lp1)
                  l1.draw(win)
                  l2.draw(win)
                  l3.draw(win)
                  l4.draw(win)
                  time.sleep(0.001)
                  l1.undraw()
                  l2.undraw()
                  l3.undraw()
                  l4.undraw()
                  lock.release()
                  if x1>2000:
                          break
        if x1>2000:
            break
                  
def collision35():
    global x1,y1,x2,y2,x3,y3,vx
    for i in range(1,30000,1):
        d31=((x1-800)**2+(y1-330)**2)**0.5
        d32=((x2-800)**2+(y2-330)**2)**0.5
        d33=((x3-800)**2+(y3-330)**2)**0.5
        if (d31<=20)or(d32<=20)or(d33<=20):
              for i in range(1,30000,1):                  
                  lock.acquire()
                  s3+=1
                  lldx1=(vx+(5*5**0.5)*math.sin((math.pi-math.atan(2))-50*i))*0.01
                  lldy1=(-9.8*i-(5*5**0.5)*math.cos((math.pi-math.atan(2))-50*i))*0.01      
                  lldx2=(vx+(5*5**0.5)*math.sin(math.atan(2)-50*i))*0.01
                  lldy2=(-9.8*i-(5*5**0.5)*math.cos(math.atan(2)-50*i))*0.01
                  lldx3=(vx+(5*5**0.5)*math.sin(-math.atan(2)-50*i))*0.01
                  lldy3=(-9.8*i-(5*5**0.5)*math.cos(-math.atan(2)-50*i))*0.01
                  lldx4=(vx+(5*5**0.5)*math.sin(-(math.pi-math.atan(2))-50*i))*0.01
                  lldy4=(-9.8*i-(5*5**0.5)*math.cos(-(math.pi-math.atan(2))-50*i))*0.01
                  lpp1.move(lldx1,lldy1)
                  lpp2.move(lldx2,lldy2)
                  lpp3.move(lldx3,lldy3)
                  lpp4.move(lldx4,lldy4)
                  ll1=Line(lpp1,lpp2)
                  ll2=Line(lpp2,lpp3)
                  ll3=Line(lpp3,lpp4)
                  ll4=Line(lpp4,lpp1)
                  ll1.draw(win)
                  ll2.draw(win)
                  ll3.draw(win)
                  ll4.draw(win)
                  time.sleep(0.001)
                  ll1.undraw()
                  ll2.undraw()
                  ll3.undraw()
                  ll4.undraw()
                  lock.release()
                  if x1>2000:
                          break
        if x1>2000:
            break
                  

def score5():
    global score,s1,s2,s3
    if s1!=0:
          score=score+500
    if s2!=0:
          score=score+500
    if s3!=0:
          score=score+500
    lock.acquire()
    score1=str(score)
    text1=Text(Point(100,400),"your final score is"+"     "+score1)
    text1.draw(win)
    lock.release()
    
def series5():
    t1=threading.Thread(target=release25,args=())
    t2=threading.Thread(target=collision15,args=())
    t3=threading.Thread(target=collision25,args=())
    t4=threading.Thread(target=collision35,args=())
    threads=[t1,t2,t3,t4]
    for i in range(0,4,1):
        threads[i].start()
    for i in range(0,4,1):
        threads[i].join()          


    score5()
    time.sleep(2)
    win.close()
   
series5()


time.sleep(8)

# -*- coding: cp936 -*-
     

from graphics import*
from threading import*
from string import*
import string
import threading
import graphics
import time
import math
lock = threading.Lock()
win=graphics.GraphWin("Angry Ball",1000,500)
win.setCoords(0,0,1000,500)
win.setBackground("white")
p1=Point(50,50)
c1=Circle(p1,10)
c1.setFill("blue")
p1=Point(50,50)
c2=Circle(p1,10)
p1=Point(50,50)
c3=Circle(p1,30)
p1=Point(50,50)
c4=Circle(p1,40)
c2.draw(win)
c1.draw(win)
c3.draw(win)
c4.draw(win)
point1=Point(700,250)
ball1=Circle(point1,20)
point2=Point(740,300)
ball2=Circle(point2,5)
point3=Point(760,320)
ball3=Circle(point3,5)
ball1.setFill("yellow")
ball2.setFill("blue")
ball3.setFill("red")
ball1.draw(win)
ball2.draw(win)
ball3.draw(win)
point1.draw(win)
point2.draw(win)
point3.draw(win)
x1=50
y1=50
x2=0
y2=0
x3=0
y3=0
vx=0
vy=0
k11=0
k12=0
k13=0
k21=0
k22=0
k23=0
k31=0
k32=0
k33=0
x1d=0
y1d=0
x2d=0
y2d=0
x3d=0
y3d=0

class initialstate:
      def __init__(self,x,y,v0):
          self.x=x
          self.y=y
          self.v0=v0
      def cos(self):
          return float(self.x-50)/self.v0
      def sin(self):
          return float(self.y-50)/self.v0



class split:
      def __init__(self,vx,vy,theta):
          self.v=(vx**2+vy**2)**0.5
          self.theta=math.atan(vy/vx)+theta*math.pi/180

      def vx(self):
          return float((self.v)*math.cos(self.theta))
      def vy(self):
          return float((self.v)*math.sin(self.theta))
     
      
def release28():
    global x1,y1,x2,y2,x3,y3,vx,vy
    p2=win.getMouse()
    r=((p2.getX()-50)**2+(p2.getY()-50)**2)**0.5
    if r>=5 and r<=40:
       v=3*r
       a=initialstate(p2.getX(),p2.getY(),r)
       vx=v*(a.cos())
       vy=v*(a.sin())
    dt=0.1
    p1=Point(x1,y1)
    c1=Circle(p1,5)
    c1.setFill("blue")
    p1.setFill("yellow")
    c1.draw(win)
    p1.draw(win)       
    for i in range(1,300000,1):        
        if x1>500 :
           c1.undraw()
           vx2=vx
           vy2=vy
           vx3=vx
           vy3=vy
           v=(vx**2+vy**2)**0.5
           theta1=math.atan(vy/vx)+10*math.pi/180
           theta2=math.atan(vy/vx)-10*math.pi/180
           vx2=float((v)*math.cos(theta1))
           vx3=float((v)*math.cos(theta2))
           vy2=float((v)*math.sin(theta1))
           vy3=float((v)*math.sin(theta2))
           x2=x1
           y2=y1
           x2=x1
           y2=y1
           x3=x1
           y3=y1
           p1=Point(x1,y1)
           p2=Point(x2,y2)
           p3=Point(x3,y3)
           c1=Circle(p1,5)
           c1.setFill("blue")
           c2=Circle(p2,5)
           c2.setFill("blue")
           c3=Circle(p3,5)
           c3.setFill("blue")
           c1.draw(win)
           c2.draw(win)
           c3.draw(win)    
           p1.setFill("yellow")
           p2.setFill("yellow")
           p3.setFill("yellow")   
           for i in range(1,300000,1):
               if x1<=2000 or x2<=2000 or x3<=2000:
                        dt=0.1
                        vx=vx
                        vy=vy-9.8*dt
                        vx2=vx2
                        vy2=vy2-9.8*dt
                        vx3=vx3
                        vy3=vy3-9.8*dt
                        dx1=vx*dt
                        dy1=vy*dt
                        dx2=vx2*dt
                        dy2=vy2*dt
                        dx3=vx3*dt
                        dy3=vy3*dt
                        x1=x1+dx1
                        y1=y1+dy1
                        x2=x2+dx2
                        y2=y2+dy2
                        x3=x3+dx3
                        y3=y3+dy3
                        p1=Point(x1,y1)
                        p2=Point(x2,y2)
                        p3=Point(x3,y3)
                        p1.setFill("yellow")
                        p2.setFill("yellow")
                        p3.setFill("yellow")
                        lock.acquire()
                        p1.draw(win)
                        p2.draw(win)
                        p3.draw(win)
                        c1.move(dx1,dy1)
                        c2.move(dx2,dy2)
                        c3.move(dx3,dy3)
                        time.sleep(0.02)
                        lock.release()
               if  x1>2000 and x2>2000 and x3>2000:
                         break
                         c1.undraw()
                         c2.undraw()
                         c3.undraw()
        if x1<=500:
           vx=vx
           vy=vy-9.8*dt
           dx1=vx*dt
           dy1=vy*dt
           x1=x1+vx*dt
           y1=y1+vy*dt
           p1=Point(x1,y1)
           p1.setFill("yellow")
           lock.acquire()
           c1.move(dx1,dy1)
           p1.draw(win)
           lock.release()
        if x1>=2000 or x1<=0 or y1>=500 or y1<=0:
           break
           c1.undraw()
          


def polybody8():
    global k11,k12,k13,k21,k22,k23,k31,k32,k33,x1d,y1d,x2d,y2d,x3d,y3d
    ve1x,ve1y,ve2x,ve2y,ve3x,ve3y,x1d,y1d,x2d,y2d,x3d,y3d,m1,m2,m3,dt=20,20,200,-200,-200,200,700,250,740,300,760,320,2000000000000000,20,30,0.001
    G=6.67*((10)**(-11))
    for i in range(1,300000,1):
         if k11==0 and k21==0 and k31==0: 
              a1x=((G*m2)/(((x1d-x2d)**2+(y1d-y2d)**2)**(3/2)))*(x2d-x1d)+((G*m3)/(((x1d-x3d)**2+(y1d-y3d)**2)**(3/2)))*(x3d-x1d)
              a1y=((G*m2)/(((x1d-x2d)**2+(y1d-y2d)**2)**(3/2)))*(y2d-y1d)+((G*m3)/(((x1d-x3d)**2+(y1d-y3d)**2)**(3/2)))*(y3d-y1d)
              a2x=((G*m1)/(((x1d-x2d)**2+(y1d-y2d)**2)**(3/2)))*(x1d-x2d)+((G*m3)/(((x2d-x3d)**2+(y2d-y3d)**2)**(3/2)))*(x3d-x2d)
              a2y=((G*m1)/(((x1d-x2d)**2+(y1d-y2d)**2)**(3/2)))*(y1d-y2d)+((G*m3)/(((x2d-x3d)**2+(y2d-y3d)**2)**(3/2)))*(y3d-y2d)
              a3x=((G*m1)/(((x1d-x3d)**2+(y1d-y3d)**2)**(3/2)))*(x1d-x3d)+((G*m2)/(((x2d-x3d)**2+(y2d-y3d)**2)**(3/2)))*(x2d-x3d)
              a3y=((G*m1)/(((x1d-x3d)**2+(y1d-y3d)**2)**(3/2)))*(y1d-y3d)+((G*m2)/(((x2d-x3d)**2+(y2d-y3d)**2)**(3/2)))*(y2d-y3d)
              ve1x=ve1x+a1x*dt
              ve1y=ve1y+a1y*dt
              ve2x=ve2x+a2x*dt
              ve2y=ve2y+a2y*dt
              ve3x=ve3x+a3x*dt
              ve3y=ve3y+a3y*dt
              x1d=x1d+ve1x*dt
              y1d=y1d+ve1y*dt
              x2d=x2d+ve2x*dt
              y2d=y2d+ve2y*dt
              x3d=x3d+ve3x*dt
              y3d=y3d+ve3y*dt   
              point1=Point(x1d,y1d)
              point2=Point(x2d,y2d)
              point3=Point(x3d,y3d)
              point1.setFill("yellow")
              point2.setFill("blue")
              point3.setFill("red")
              lock.acquire()
              point1.draw(win)
              point2.draw(win)
              point3.draw(win)
              ball1.move(ve1x*dt,ve1y*dt)
              ball2.move(ve2x*dt,ve2y*dt)
              ball3.move(ve3x*dt,ve3y*dt)
              time.sleep(0.01)
              lock.release()
              if x1>=2000:
                 break

         if k11!=0 or k21!=0 or k31!=0:
              ve2x=ve2x
              ve2y=ve2y
              ve3x=ve3x
              ve3y=ve3y
              x1d=x1d+ve1x*dt
              y1d=y1d+ve1y*dt
              x2d=x2d+ve2x*dt
              y2d=y2d+ve2y*dt
              x3d=x3d+ve3x*dt
              y3d=y3d+ve3y*dt   
              point1=Point(x1d,y1d)
              point2=Point(x2d,y2d)
              point3=Point(x3d,y3d)
              point1.setFill("yellow")
              point2.setFill("blue")
              point3.setFill("red")
              lock.acquire()
              point1.draw(win)
              point2.draw(win)
              point3.draw(win)
              ball1.move(ve1x*dt,ve1y*dt)
              ball2.move(ve2x*dt,ve2y*dt)
              ball3.move(ve3x*dt,ve3y*dt)
              time.sleep(0.01)
              lock.release()
              if x1>=2000:
                 break


def score8():   
    global x1,y1,x2,y2,x3,y3,k11,k12,k13,k21,k22,k23,k31,k32,k33,x1d,y1d,x2d,y2d,x3d,y3d
    global score
    for i in range(1,30000,1):
        lock.acquire()
        r11=((x1-x1d)**2+(y1-y1d)**2)**0.5
        r12=((x1-x2d)**2+(y1-y2d)**2)**0.5
        r13=((x1-x3d)**2+(y1-y3d)**2)**0.5
        r21=((x2-x1d)**2+(y2-y1d)**2)**0.5
        r22=((x2-x2d)**2+(y2-y2d)**2)**0.5
        r23=((x2-x3d)**2+(y2-y3d)**2)**0.5
        r31=((x3-x1d)**2+(y3-y1d)**2)**0.5
        r32=((x3-x2d)**2+(y3-y2d)**2)**0.5
        r33=((x3-x3d)**2+(y3-y3d)**2)**0.5
        if 0<=r11<=30:
           ball1.undraw()
           if k11==0:
              score=score+500
              k11+=1
        if 0<=r12<=15:
           ball2.undraw()
           if k12==0:
              score=score+500
              k12+=1
        if 0<=r13<=15:
           ball3.undraw()
           if k13==0:
              score=score+500
              k13+=1
        if 0<=r21<=30:
           ball1.undraw()
           if k21==0:
              score=score+500
              k21+=1
        if 0<=r22<=15:
           ball2.undraw()
           if k22==0:
              score=score+500
              k22+=1
        if 0<=r23<=15:
           ball3.undraw()
           if k23==0:
              score=score+500
              k23+=1
        if 0<=r31<=30:
           ball1.undraw()
           if k31==0:
              score=score+500
              k31+=1
        if 0<=r32<=15:
           ball2.undraw()
           if k32==0:
              score=score+500
              k32+=1
        if 0<=r33<=15:
           ball3.undraw()
           if k33==0:
              score=score+500
              k33+=1
        lock.release()
        if  x1>2000 and x2>2000 and x3>2000:
            break 
    lock.acquire()
    score1=str(score)
    text1=Text(Point(100,400),"your final score is"+"     "+score1)
    text1.draw(win)
    lock.release()
    
def series8():
    t1=threading.Thread(target=release28,args=())
    t2=threading.Thread(target=polybody8,args=())
    t3=threading.Thread(target=score8,args=())
    threads=[t1,t2,t3]
    for i in range(0,3,1):
        threads[i].start()
    for i in range(0,3,1):
        threads[i].join()

    time.sleep(2)
    win.close()


series8()

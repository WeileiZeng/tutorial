# button.py
import time
import graphics
from graphics import *
class button():
    def __init__(self,window,center,wide,high,text):
        self.center=center
        self.wide=wide
        self.high=high
        self.text=text
        self.win=window
        self.x=self.center.getX()
        self.y=self.center.getY()
        self.xyxy=[]
        self.rect=None
        self.tt=None
        button.draw(self)
        
    def setCenter(self,point):
        
        xx=point.getX()
        yy=point.getY()
        dx=xx-self.x
        dy=yy-self.y
        button.move(self,dx,dy)
        self.center=point
        self.x=xx
        self.y=yy

    def draw(self):
        
        p1=Point(self.x-self.wide/2.0,self.y+self.high/2.0)
        p2=Point(self.x+self.wide/2.0,self.y+self.high/2.0)
        p3=Point(self.x+self.wide/2.0,self.y-self.high/2.0)
        p4=Point(self.x-self.wide/2.0,self.y-self.high/2.0)
        x4=p4.getX()    
        y4=p4.getY()
        x2=p2.getX()
        y2=p2.getY()    #x2>x4,y2>y4  made this for judgement
        
        self.rect=Rectangle(p1,p3)
        self.rect.draw(self.win)
        self.tt=Text(self.center,self.text)
        self.tt.draw(self.win)
        self.xyxy=[x4,y4,x2,y2]

    def setFill(self,color):
        self.rect.setFill(color)
    def getText(self):
        return self.tt.getText()
    def setText(self,ttt):
        self.tt.setText(ttt)
    def click(self):
        x4,y4,x2,y2=self.xyxy[0],self.xyxy[1],self.xyxy[2],self.xyxy[3]
        pp=self.win.getMouse()
        xx=pp.getX()
        yy=pp.getY()
        while xx<x4 or xx>x2 or yy<y4 or yy>y2:
            pp=self.win.getMouse()
            xx=pp.getX()
            yy=pp.getY()
        return True
    def judge(self,point):
        xx=point.getX()
        yy=point.getY()
        x4,y4,x2,y2=self.xyxy[0],self.xyxy[1],self.xyxy[2],self.xyxy[3]
        if xx<x4 or xx>x2 or yy<y4 or yy>y2:
            return False
        else:
            """self.rect.setFill('red')
            time.sleep(0.1)
            self.rect.setFill('yellow')"""
            return True
    def active(self):#to show that the button can be press
        self.rect.setFill('gray')
        return True
    def unactive(self):#to show that the button cannot be press
        self.rect.setFill('white')
        return False

    def move(self,dx,dy):
        self.rect.undraw()
        self.tt.undraw()
        self.x=self.x+dx
        self.y=self.y+dy
        self.center=Point(self.x,self.y)
        button.draw(self)
    def close(self):
        self.rect.undraw()
        self.tt.undraw()

            
        
        

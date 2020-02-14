#a moudle of impact
import math
import graphics
import random
from random import *
from math import *
from graphics import *
class particular():
    def __init__(self,x,y,vx,vy,m,r,win):
        self.x=x
        self.y=y
        self.vx=vx
        self.vy=vy
        self.m=m
        self.r=r
        self.point=Point(x,y)
        self.point.draw(win)
        #if x>0:
            #self.point.setFill('red')#to observe the mix of two group of gas
    def move(self,dx,dy):
        self.point.move(dx,dy)
        self.x+=dx
        self.y+=dy
        
def create_window():
    win=GraphWin('impact',400,400)
    win.setCoords(-100.0,-100.0,100.0,100.0)
    return win
    
def length(a,b):
    return sqrt((a.x-b.x)**2+(a.y-b.y)**2)
def impact(a,b):#check if "a" impact "b" and change their velocity if so
    if length(a,b)<a.r+b.r :
        
        x,y=-a.x+b.x,-a.y+b.y
        #print x,y
        try:
            x,y=x/sqrt(x**2+y**2),y/sqrt(x**2+y**2)
        except:
            print b.x,a.x
        aa,bb=a.vx*x+a.vy*y,b.vx*x+b.vy*y
        a.vx+=2.0*(aa)*x
        a.vy+=2.0*(aa)*y
        b.vx-=2.0*(bb)*x
        b.vy-=2.0*(bb)*y
def wall(a):#check if "a" impact the wall and change its velosity if so
    l=100.0
    if l-abs(a.x)<a.r and a.x*a.vx>0:
        a.vx=-a.vx
    if l-abs(a.y)<a.r and a.y*a.vy>0:
        a.vy=-a.vy
def create_particular(win):

    l=100.0
    x,y=2.0*l*random()-l,l*random()*2.0-l#from -100.0 to 100.0
    u,sigma=0,100
    vx=gauss(u,sigma)
    vy=gauss(u,sigma)
    m=1e-10
    r=0.01
##r is very strange,when it is small,the particulars run following a staight line;
##while when it becomes large, the situation goes out of control.
    a=particular(x,y,vx,vy,m,r,win)
    return a
def sort(nums,flag,begin,end):
    #flag=range(len(nums))#flag is used to remenber the positon of objects in nums
    empty=begin
    a=nums[begin]
    b=flag[begin]
    i=begin+1
    j=end
    for k in range(end-begin):
        if i>empty:
            if nums[i]<=a:
                nums[empty]=nums[i]
                flag[empty]=flag[i]
                empty=i
                i=i+1
            elif nums[j]>a:
                j=j-1
            else:
                nums[empty]=nums[j]
                flag[empty]=flag[j]
                empty=j
                j=j-1
        elif j<empty:
            if nums[j]>a:
                nums[empty]=nums[j]
                flag[empty]=flag[j]
                empty=j
                j=j-1
            elif nums[i]>a:
                nums[empty]=nums[i]
                flag[empty]=flag[i]
                empty=i
                i=i+1
            else:
                i=i+1
    nums[empty]=a
    flag[empty]=b
    if begin<empty-1:
        sort(nums,flag,begin,empty-1)
    if end>empty+1:
        sort(nums,flag,empty+1,end)
    return flag
    

def main():
    win=create_window()
    pp=[]#particulars
    xx,yy=[],[]#the x and y of the particulars
    n=500                 #the number of particulars
    for i in range(n):
        p=create_particular(win)
        pp.append(p)
        xx.append(pp[i].x)
        yy.append(pp[i].y)
    #print xx
    track=p   ##to record the track of one particulars
    track_point1=p.point #record the point to draw line of the track
    flag1=range(n)
    sort(xx,flag1,0,len(xx)-1)
    flag2=range(n)
    sort(yy,flag2,0,len(yy)-1)
    for i in range(n):#judge the situation of the particulars(impact the wall or others?)
        a=pp[flag1[i]]
        wall(a)
        b=a#bug
        for j in range(n):      
            if b.x-a.x>a.r+b.r or i+1+j>n-1:
                break
            b=pp[flag1[i+1+j]]
            impact(a,b)
    for i in range(n):#judge the situation of the particulars(impact the wall or others?)
        a=pp[flag2[i]]
        wall(a)
        b=a
        for j in range(n):
            if b.y-a.y>a.r+b.r or i+1+j>n-1:
                break
            b=pp[flag2[i+1+j]]
            impact(a,b)
    dt=0.001
    q=1
    print 'start'
    while True:
        #print q
        q+=1
        xx=[]
        yy=[]
        for p in pp:#move the particulars according to their velocity
            p.move(p.vx*dt,p.vy*dt)
            g=500.0
            p.vy-=g*dt#Boltzmann-distributon
            xx.append(p.x)
            yy.append(p.y)
        flag1,flag2=range(n),range(n)
        sort(xx,flag1,0,n-1)
        sort(yy,flag2,0,n-1)
        for i in range(n):#judge the situation of the particulars(impact the wall or others?)
            a=pp[flag1[i]]
            wall(a)
            b=a
            for j in range(n):#judge if the particular in the right sight of a impacted a
                if b.x-a.x>a.r+b.r or i+1+j>n-1:
                    break
                b=pp[flag1[i+1+j]]
                impact(a,b)
            b=a
            for j in range(n):#judge if the particular in the right sight of a impacted a
                if a.x-b.x>a.r+b.r or i-1-j<0:
                    break
                b=pp[flag1[i-1-j]]
                impact(a,b)
        for i in range(n):#judge the situation of the particulars(impact the wall or others?)
            a=pp[flag2[i]]
            wall(a)
            b=a
            for j in range(n):
                if b.y-a.y>a.r+b.r or i+1+j>n-1:
                    break
                b=pp[flag2[i+1+j]]
                impact(a,b)
            b=a
            for j in range(n):
                if a.y-b.y>a.r+b.r or i-1-j<0:
                    break
                b=pp[flag2[i-1-j]]
                impact(a,b)
        track_point2=track.point
        #ll=Line(track_point1,track_point2)
        #ll.draw(win)
        #ll=Circle(track_point1,1)
        #ll.draw(win)#draw the track
        track_point1=track_point2
main()
    
                 
        
    
    
    
        
        
    
    

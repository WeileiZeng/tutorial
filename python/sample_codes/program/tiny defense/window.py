import py
import button
import time
from graphics import *
from math import*
class bug():
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.v=0.05
        #self.body=Circle(Point(x,y),0.5)
        #self.body.setFill('green')#color_rgb(60,70,80))
        self.body=Image(Point(x,y),'image/bug8.gif')
        #self.body.setPixel(20,20,'blue')
        self.body.draw(win)
        self.life=True
        life_power_full=100
        life_power=100
        self.life_bar=life_bar(x,y,life_power_full)
    def move(self):
        d=((15-self.x)**2+(10-self.y)**2)**0.5
        if (d>0.1):
            dx=(15-self.x)/d*self.v
            dy=(10-self.y)/d*self.v
            self.body.move(dx,dy)
            self.x+=dx
            self.y+=dy
            self.life_bar.move(dx,dy)
            self.life_bar.x+=dx
            self.life_bar.y+=dy
    def undraw(self):
        try:
            self.body.undraw()
        except:
            pass
        self.life_bar.undraw()
                         
    def action(self):
        if (not self.life):
            self.undraw()
        if (self.life_bar.life_power<1):
            self.life=False
            #print 'the bug died'
        else:
            self.move()
        

class life_bar():
    def __init__(self,x,y,life_power_full):
        self.size=0.6
        self.x=x
        self.y=y
        self.life_power=life_power_full
        self.life_power_full=life_power_full
        self.ratio=1.0
        self.bar_left=Rectangle(Point(x-self.size,y+self.size),Point(x+self.size*(2*self.ratio-1.0),y+self.size*1.2))
        self.bar_left.setFill('red')
        self.bar_left.draw(win)
        self.bar_right=Rectangle( Point(x+self.size*(-1.0+2*self.ratio),y+self.size),Point(x+self.size,y+self.size*1.2) )
        self.bar_right.draw(win)
    def minus(self,attack):
        self.life_power-=attack
        #print 'cerrent life_power = ',self.life_power
        self.ratio=1.0*self.life_power/self.life_power_full
        if (self.ratio<0):
            self.ratio=0
        self.bar_left.undraw()
        self.bar_right.undraw()
        self.bar_left=Rectangle(Point(self.x-self.size,self.y+self.size),Point(self.x+self.size*(2*self.ratio-1.0),self.y+self.size*1.2))
        self.bar_left.setFill('red')
        self.bar_left.draw(win)
        self.bar_right=Rectangle( Point(self.x+self.size*(-1.0+2*self.ratio),self.y+self.size),Point(self.x+self.size,self.y+self.size*1.2) )
        self.bar_right.draw(win)
    def move(self,dx,dy):
        self.bar_left.move(dx,dy)
        self.bar_right.move(dx,dy)
    def undraw(self):
        self.bar_left.undraw()
        self.bar_right.undraw()
class spark():
    def __init__(self,x,y,angle,v,frames):
        self.body=Circle(Point(x,y),0.1)
        self.body.setFill('red')
        self.body.draw(win)
        self.life=True
        self.lifetime=frames
    def action(self):
        if (lifetime>0):
            self.body.move(self.v*cos(self.angle),self.v*sin(self.angle))
            self.lifetime-=1
        else:
            self.life=False
class bullet():
    def __init__(self,x,y,v,target):#target is a bug
        self.x=x
        self.y=y
        self.v=v
        self.directionx=(target.x-x)/(((target.y-y)**2+(target.x-x)**2)**0.5)
        self.directiony=(target.y-y)/(((target.y-y)**2+(target.x-x)**2)**0.5)
        self.body=Circle(Point(x,y),0.1)
        self.body.setFill('red')
        self.body.draw(win)
        self.life=True
        self.lifetime=100
        #self.target=target
    def action(self):
        if (self.life):
            if (self.lifetime<1):
                self.life=False
            self.lifetime-=1
            self.move()
            for sb in bugs:
                if (impact(self,sb)):
                    sb.life_bar.minus(30)
                    self.life=False
                    self.body.undraw()
                
        
    def move(self):
        self.body.move(self.v*self.directionx,self.v*self.directiony)
        self.x+=self.v*self.directionx
        self.y+=self.v*self.directiony
    def bomb(self):
        pass
    def undraw(self):
        self.body.undraw()
class bar():
    def __init__(self,center,target):#target is the target point
        x=target.x-center.x
        y=target.y-center.y
        size=0.1
        d=(x**2+y**2)**0.5/size
        d2=d*0.1
        self.body=Polygon(Point(center.x-y/d,center.y+x/d),Point(center.x+y/d,center.y-x/d),Point(center.x+x/d2+y/d,center.y+y/d2-x/d),Point(center.x+x/d2-y/d,center.y+y/d2+x/d))
        self.body.setFill('blue')
        self.body.draw(win)
    def undraw(self):
        self.body.undraw()
class gun():
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.center=Point(x,y)
        self.body=bar(self.center,Point(x-1,y))
    def fire(self,target):
        self.body.undraw()
        self.body=bar(self.center,Point(target.x,target.y))
        v=1.0
        objects.append(bullet(self.x,self.y,v,target))
                            
class tank():
    def __init__(self,x,y):
        self.positon=[]
        self.x=x
        self.y=y
        self.size=0.4
        self.body=Rectangle(Point(x-self.size,y-self.size),Point(x+self.size,y+self.size))
        self.body.setFill('green')
        self.body.draw(win)
        self.gun=gun(x,y)
        life_power=100
        self.life_bar=life_bar(x,y,life_power)
        self.life=True

        self.recovery_time=0#equal 10 when full
        self.fire_range=8.0
    def fire(self,target):
        self.recovery_time=10
        return self.gun.fire(target)
    def action(self):
        if (self.recovery_time>0):
            self.recovery_time-=1
        self.search()
    def search(self):
        for sb in bugs:
            if (self.recovery_time==0 and sb.life and distance(self,sb)<self.fire_range):
                self.recovery_time=10
                self.gun.fire(sb)
                
                
    
        
                            
class tower():
    def __init__(self,x,y):
        self.position=[x,y]
        self.x=x
        self.y=y
        self.body=Circle(Point(x,y),1)
        self.body.setFill('red')
        self.body.draw(win)
def window():
    global win
    win=GraphWin('tiny defense',930,630)
    win.setCoords(-0.5,-0.5,30.5,20.5)
    #window=Rectangle(Point(0.4,0.4),Point(10.6,10.6))
    #window.draw(win)
    #return win

def terrain():
    h1=Polygon(Point(-1,-1),Point(3,-1),Point(6,3),Point(-1,3))
    h1.setFill('yellow')
    h1.setOutline('yellow')
    h1.draw(win)
    h1=Polygon(Point(-1,21),Point(3,21),Point(6,17),Point(-1,17))
    h1.setFill('yellow')
    h1.setOutline('yellow')
    h1.draw(win)
    h1=Polygon(Point(10,-1),Point(31,-1),Point(31,3),Point(15,3))
    h1.setFill('yellow')
    h1.setOutline('yellow')
    h1.draw(win)
    h1=Polygon(Point(10,21),Point(31,21),Point(31,17),Point(15,17))
    h1.setFill('yellow')
    h1.setOutline('yellow')
    h1.draw(win)
    tower(27,10)
def impact(object1,object2):# check if the two obejects impact
    if (abs(object1.x-object2.x)+abs(object1.y-object2.y)<1.0):
        if (object1.life and object2.life):
            return True
        else:
            return False
    else:
        return False
def distance(object1,object2):# an approximation of the real distance
    return abs(object1.x-object2.x)+abs(object1.y-object2.y)
def run():
    for sb in tanks:
        
        
        if (not sb.life):
            tanks.remove(sb)
        sb.action()
    for sb in bugs:   
        if (not sb.life):
            bugs.remove(sb)
        sb.action()
    for sb in objects:
        if (not sb.life):
            objects.remove(sb)
        sb.action()
    print 'length of tanks: ',len(tanks)
    print 'length of bugs: ',len(bugs)
    print 'length of objects: ',len(objects)
def main():
    global objects,tanks,bugs
    window()                #draw the window
    terrain()               #draw the terrain or map
    tank1=tank(20.0,10.0)   #set up a tank
    bug1=bug(10.0,10.0)     #set up a bug
    objects=[]              #store bullets,sparks
    tanks=[]                #store all tanks
    bugs=[]                 #store all bugs
    #tank1.fire(bug1)

    tanks.append(tank1)
    tanks.append(tank(18.0,13.0))
    tanks.append(tank(10.0,8.0))
    tanks.append(tank(7.0,4.0))
    tanks.append(tank(8.0,6.0))
    bugs.append(bug1)
    bugs.append(bug(10.0,12.0))
    bugs.append(bug(8.0,9.0))
    bugs.append(bug(1.0,3.0))
    bugs.append(bug(2.0,9.0))
    bugs.append(bug(3.0,4.0))
    bugs.append(bug(4.0,7.0))
    bugs.append(bug(5.0,3.0))
    for i in range(1400):
        if (i%40==9):
            bugs.append(bug(-10,8))
            bugs.append(bug(5,32))
            bugs.append(bug(5,-3))
        #print 'i = ',i
        #pp=win.getMouse()
        run()
        time.sleep(0.001)
                
    win.close()
main()

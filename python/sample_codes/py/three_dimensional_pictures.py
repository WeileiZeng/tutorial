

#three_dimensional.py
#a module to draw three-dimensional pictures
#all three_dimensional features are named by their ordinary name following theletter "t" 
import graphics
import math
from graphics import *
def create_window():
	win=GraphWin('three-dimensional pictures',600,600)
	win.setCoords(-20.0,-20.0,40.0,40.0)
	return win
def draw_coordinate_systerm(win):
	y_axis=Line(Point(0,0),Point(35.0,0))
	y_axis.draw(win)
	y_axis.setArrow('last')
	Text(Point(35,-1),'y').draw(win)
	b=3.0
	for i in range(10):
		Line(Point(b*(i+1.0),0),Point(b*(i+1.0),0.3)).draw(win)
		Text(Point(b*(i+1.0),-1.1),i+1).draw(win)
	z_axis=Line(Point(0,0),Point(0,35.0))
	z_axis.draw(win)
	z_axis.setArrow('last')
	Text(Point(-1.2,35),'z').draw(win)
	c=3.0
	for i in range(10):
		Line(Point(0,c*(i+1.0)),Point(0.3,c*(i+1.0))).draw(win)
		Text(Point(-1.1,c*(i+1.0)),i+1).draw(win)
	x_axis=Line(Point(0,0),Point(-17.5,-17.5))
	x_axis.draw(win)
	x_axis.setArrow('last')
	Text(Point(-17.5-1,-17.5+1),'x').draw(win)
	a=1.5
	for i in range(10):
		Line(Point(-a*(i+1.0),-a*(i+1.0)),Point(-a*(i+1.0)+0.3,-a*(i+1.0)-0.3)).draw(win)
		Text(Point(-a*(i+1.0)-0.8,-a*(i+1.0)+0.8),i+1).draw(win)
def change_dimension(coordinate):
	x,y,z=coordinate[0],coordinate[1],coordinate[2]
	#1.4142135623730949
	a,b,c=1.5,3.0,3.0
	Y=-x*a+z*c
	X=-x*a+y*b
	return [X,Y]
class tpoint():
	def __init__(self,x,y,z):
		self.x,self.y,self.z=x,y,z
		a=change_dimension([x,y,z])
		self.X,self.Y=a[0],a[1]
		self.point=Point(self.X,self.Y)
	def draw(self,win):
		self.point.draw(win)
	def getlenth(self,p2):
		return math.sqrt((self.x-p2.x)**2+(self.y-p2.y)**2+(self.z-p2.z)**2)
class tline():
	def __init__(self,tpoint1,tpoint2):
		self.line=Line(tpoint1.point,tpoint2.point)
		self.first=tpoint1
		self.last=tpoint2
	def draw(self,win):
		self.win=win
		self.line.draw(win)
	def undraw(self):
		self.line.undraw()
	def setArrow(self,direction):
		self.line.setArrow(direction)
	def move(self,dx,dy,dz):
		a=change_dimension([dx,dy,dz])
		dX,dY=a[0],a[1]
		self.line.move(dX,dY)
class dotline():
	def __init__(self,tpoint1,tpoint2,number):
		self.number=number
		self.first=tpoint1
		self.last=tpoint2
	def draw(self,win):
			self.win=win
			self.lines=[]
			self.undraw()
			x1,y1=self.first.X,self.first.Y
			x2,y2=self.last.X,self.last.Y
			num=self.number*2-1
			distance_x,distance_y=(x2-x1)/num*1.0,(y2-y1)/num*1.0
			for j in range(self.number):
				i=j*2.0
				ll=Line(Point(x1+distance_x*i,y1+distance_y*i),
					 Point(x1+distance_x*(i+1.0),y1+distance_y*(i+1.0)))
				ll.draw(self.win)
				self.lines.append(ll)
	def undraw(self):
		for ll in self.lines:
			ll.undraw()
	def move(self,dx,dy,dz):
		a=change_dimension([dx,dy,dz])
		dX,dY=a[0],a[1]
		for ll in self.lines:
					ll.move(dX,dY)
			
class vector():
	def __init__(self,x,y,z):
		self.x,self,y,self.z=x,y,z

def test(win):
	a=tpoint(6,6,6)
	b=tpoint(6,4,6)
	B=tpoint(6,4,4)
	A=tpoint(6,6,4)
	c=tpoint(4,6,6)
	C=tpoint(4,6,4)
	d=tpoint(4,4,6)
	D=tpoint(4,4,4)
	for p1 in [a,b,c,d,A,B,C,D]:
		for p2 in [a,b,c,d,A,B,C,D]:
			if p1.getlenth(p2)==2:
				if D in [p1,p2]:
					print 1
					dotline(p1,p2,10).draw(win)
				else:
					print 2
					tline(p1,p2).draw(win)
	for p1 in [a,b,c,d,A,B,C,D]:
		for p2 in [a,b,c,d,A,B,C,D]:
			if p1.getlenth(p2)==2:
				if D in [p1,p2]:
					print 1
					ll=dotline(p1,p2,10)
					ll.draw(win)
					ll.move(0,4.0,0)
				else:
					print 2
					ll=tline(p1,p2)
					ll.draw(win)
					ll.move(0,4.0,0)
		
	
				

	
	
def main():
	win=create_window()
	draw_coordinate_systerm(win)
	test(win)
main()
##class polygon():
##                def __init__(self,tpoints):
##                        self.lines=[]  
##                        if len(tpoints)<3:
##                                pass
##                        else:
##                                
##                                for i in range(len(tpoints)-1):
##                                        ll=line(tpoints[i],tpoints[i+1])
##                                        self.lines.append(ll)
##                                self.lines.append(line(tpoints[-1],tpoints[0]))
##                def draw(self,win):
##                        self.win=win
##                        for ll in self.lines:
##                                ll.draw(win)
##                def undraw(self):
##                        for ll in self.line:
##                                ll.undraw()
##                                
##                        
##                        
                        
                                    
	

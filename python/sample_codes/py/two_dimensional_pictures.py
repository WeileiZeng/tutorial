

#three_dimensional.py
#a module to draw three-dimensional pictures
#all three_dimensional features are named by their ordinary name following theletter "t" 
import graphics
import math
from graphics import *
from math import *
def create_window():
	win=GraphWin('three-dimensional pictures',600,600)
	win.setCoords(-20.0,-20.0,40.0,40.0)
	return win
def draw_coordinate_systerm(win):
	x_axis=Line(Point(0,0),Point(35.0,0))
	x_axis.draw(win)
	x_axis.setArrow('last')
	Text(Point(35,-1),'x').draw(win)
	a=3.0
	for i in range(10):
		Line(Point(a*(i+1.0),0),Point(a*(i+1.0),0.3)).draw(win)
		Text(Point(a*(i+1.0),-1.1),i+1).draw(win)
	y_axis=Line(Point(0,0),Point(0,35.0))
	y_axis.draw(win)
	y_axis.setArrow('last')
	Text(Point(-1.2,35),'y').draw(win)
	b=3.0
	for i in range(10):
		Line(Point(0,b*(i+1.0)),Point(0.3,b*(i+1.0))).draw(win)
		Text(Point(-1.1,b*(i+1.0)),i+1).draw(win)


class tpoint():
	def __init__(self,x,y):
		self.x,self.y=x,y
		
		self.point=Point(x,y)
	def draw(self,win):
		self.point.draw(win)
	def getlenth(self,p2):
		return math.sqrt((self.x-p2.x)**2+(self.y-p2.y)**2)
def main():
        win=create_window()
        draw_coordinate_systerm(win)
        a,b=0.2,-1.0
        l,h=10.0,5.0
        for i in range(10000):
                x=-l+i/100.0
                y=(x+l)/sqrt((x+l)**2+h*h)+(l-x)/sqrt((l-x)**2+h*h)
                y*=4.0
                Point(x,y).draw(win)
def main2():
        win=create_window()
        draw_coordinate_systerm(win)
        a=30.0
        for i in range(10000):
                x=i/100.0
                y=(a**(2.0/3.0)-x**(2.0/3.0))**1.5
                
                Point(x,y).draw(win)
main2()
	

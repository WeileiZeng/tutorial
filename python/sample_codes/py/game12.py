
# a small module to make some circles
import graphics
from graphics import *

color = ['red','blue','yellow','green','orange']
win =GraphWin("circle",800,800)
win.setCoords(0.0,0.0,40.0,40.0)
times=1

		
def main1():
    for i in range(12):
        x=8+i
        y=20+i
        center=Point(x,y)
        circle(center)
    for i in range(12):
        x=20+i
        y=32-i
        center=Point(x,y)
        circle(center)
    for i in range(12):
        x=32-i
        y=20-i
        center=Point(x,y)
        circle(center)
    for i in range(12):
        x=20-i
        y=8+i
        center=Point(x,y)
        circle(center)
       
def circle(center):
	for i in range(10):
                
		b=(i+1)%5
		c=10-i
		cir=Circle(center,c)
		cir.setFill(color[b])
		cir.draw(win)
def main():
    for i in range(1):
        main1()
        times=times+1
        timetext=Text(Point(3,39),'the times is %d')%times
        timetext.draw(win)
def close():
    win.close()
        


main()

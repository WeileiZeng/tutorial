
# a small module to make some circles
import graphics
from graphics import *

color = ['red','blue','yellow','green','orange']
win =GraphWin("circle",800,800)
win.setCoords(0.0,0.0,40.0,40.0)

		
def main():
    for i in range(10):
        x=10+i
        y=20+i
        center=Point(x,y)
        circle(center)
    for i in range(10):
        x=20+i
        y=30-i
        center=Point(x,y)
        circle(center)
    for i in range(10):
        x=30-i
        y=20-i
        center=Point(x,y)
        circle(center)
    for i in range(10):
        x=20-i
        y=10+i
        center=Point(x,y)
        circle(center)
       
def circle(center):
	for i in range(10):
                
		b=(i+1)%5
		c=10-i
		cir=Circle(center,c)
		cir.setFill(color[b])
		cir.draw(win)


main()

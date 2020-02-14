
# a small module to make some circles
import graphics
from graphics import *

color = ['red','blue','yellow','green','orange']
win =GraphWin("circle",800,800)
win.setCoords(0.0,0.0,40.0,40.0)
		
def main():
    for i in range(20):
        center=win.getMouse()
        circle(center)

def circle(center,):
	for i in range(7):
                
		b=(i+1)%5
		c=10-i
		cir=Circle(center,c)
		cir.setFill(color[b])
		cir.draw(win)


main()

# a small module to make some circles
import graphics
from graphics import *
def main():
	win =GraphWin("circle",400,400)
	win.setCoords(0.0,0.0,20.0,20.0)
	a=Point(5,5)
	color=['red','blue','yellow','green','orange']
	for i in range(10):
		b=(i+1)%5
		c=10-i
		cir=Circle(a,c)
		cir.setFill(color[b])
		cir.draw(win)
	x=raw_input('press any key...')
	win.close()

main()
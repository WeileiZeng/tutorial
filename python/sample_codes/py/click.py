# click me
import graphics
from graphics import *
def main():
	win =GraphWin("circle",400,400)
	b =raw_input('press any key to start...')
	for i in range(10):
		p=win.getMouse()
		p.draw(win)
		cir=Circle(p,10)
		cir.draw(win)
		cir.setFill('yellow')
		
		x=p.getX()
		y=p.getY()
		print "you clicked (%d,%d)"%(x,y)
	a=raw_input('press any key...')
	win.close()

main()

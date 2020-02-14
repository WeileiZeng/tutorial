import graphics
from graphics import *
def main():
	
	
	win = GraphWin("win",400,400)
	for i in range(10):
		a=win.getMouse()
		for i in range(20):
			b=win.getMouse()
			c=Line(a,b)
			c.draw(win)
			a=b
			x = input("enter 1 to continue or 0 for another start: ")
			if x == 0:
				break
		x = input("enter 1 to start or 0 to end...")
		if x == 0:
			win.close()
			break
	win.close

main()
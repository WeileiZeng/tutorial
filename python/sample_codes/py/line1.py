import graphics
from graphics import *
def main():
	
	
	win = GraphWin("win",400,400)
	for i in range(10):
		
		ss =input('enter how many lines you want: ')
		a=win.getMouse()
		for i in range(ss):
			b=win.getMouse()
			c=Line(a,b)
			c.draw(win)
			c.setFill('red')
			a=b
			
		x = input("enter 1 to start or 0 to end...")
		if x == 0:
			win.close()
			break
	win.close

main()
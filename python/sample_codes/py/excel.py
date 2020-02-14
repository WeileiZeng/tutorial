# make a picture of an excel
import graphics
from graphics import *
def main():
	win = GraphWin("Excel",400,400)
	win.setCoords(0.0,0.0,10.0,10.0)
	for i in range(10):
		lin=Line(Point(0,i),Point(10,i)).draw(win)
	for i in range(10):
		lin=Line(Point(i,0),Point(i,10)).draw(win)
	x = raw_input("press any key...")
	win.close()

main()


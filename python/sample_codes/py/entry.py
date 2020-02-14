


import time
import graphics
from graphics import *

win=GraphWin()
en=Entry(Point(100,100),5)
en.draw(win)
import button
from button import *
bb=button(win,Point(100,150),70,20,'calculate')
bb.active()
tt=Text(Point(70,50),'answer=')
tt.draw(win)
def main1():
	ppp=Point(0,0)

	for i in range(200):
		pp=win.checkMouse()
		if type(pp)==type(ppp) and bb.judge(pp):
			a=en.getText()
			if len(a)>0:
				aa=float(a)
				b=aa*2.0
				tt=Text(Point(120,50),b)
				tt.draw(win)
			time.sleep(1.0)
			if len(a)>0:
				tt.undraw()
		else:
			time.sleep(0.1)
def main2():
        a=Rectangle(Point(20,20),Point(60,40))
        a.setFill('red')
        a.draw(win)

main2()

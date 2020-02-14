# a module to get some points quickly
import graphics
from graphics import *
pp=[]
win = GraphWin('window',300,300)
print 'click the screen ten times to get ten points from p0 to p9'
for i in range(10):
	p = win.getMouse()
	pp.append(p)
	print p.getX(),p.getY()
p0=pp[0]
p1=pp[1]
p2=pp[2]
p3=pp[3]
p4=pp[4]
p5=pp[5]
p6=pp[6]
p7=pp[7]
p8=pp[8]
p9=pp[9]



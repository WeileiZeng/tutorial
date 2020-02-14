#zui xiao er cheng fa
#this module can finger out the 'a','b','x_averge','y_average'
import graphics
import math
from math import *
from graphics import *
def draw_coordinate_systerm(x_data,y_data,x,y,a_line,b_line):#x_data is a list as [name,step,first],['U/V',5.0,10.0]
	win=GraphWin('three-dimensional pictures',600,600)
	win.setCoords(x_data[2]-2.0*x_data[1],y_data[2]-2.0*y_data[1],x_data[2]+12.0*x_data[1],y_data[2]+12.0*y_data[1])
	x_axis=Line(Point(x_data[2],y_data[2]),Point(x_data[2]+11.0*x_data[1],y_data[2]))
	x_axis.draw(win)
	x_axis.setArrow('last')
	Text(Point(x_data[2]+11.0*x_data[1],y_data[2]-0.2*y_data[1]),x_data[0]).draw(win)
	a=x_data[1]
	for i in range(10):
		Line(Point(a*(i+1.0)+x_data[2],y_data[2]),Point(a*(i+1.0)+x_data[2],y_data[2]+0.3*y_data[1])).draw(win)
		Text(Point(a*(i+1.0)+x_data[2],y_data[2]-1.1*y_data[1]),x_data[2]+(i+1.0)*x_data[1]).draw(win)
	y_axis=Line(Point(x_data[2],y_data[2]),Point(x_data[2],y_data[2]+y_data[1]*11.0))
	y_axis.draw(win)
	y_axis.setArrow('last')
	Text(Point(x_data[2]-1.2*x_data[1],y_data[2]+11.0*y_data[1]),y_data[0]).draw(win)
	b=y_data[1]
	for i in range(10):
		Line(Point(x_data[2],y_data[2]+b*(i+1.0)),Point(x_data[2]-0.3*x_data[1],y_data[2]+b*(i+1.0))).draw(win)
		Text(Point(x_data[2]-1.1*x_data[1],y_data[2]+b*(i+1.0)),y_data[2]+(i+1.0)*y_data[1]).draw(win)
	ll=len(x)
	pp=[]
	for i in range(ll):
		p=Point(x[i],y[i])
		Circle(p,0.02).draw(win)
		p.draw(win)
		pp.append(p)
		print i
	for i  in range(ll-1):
	    print i
	    Line(pp[i],pp[i+1]).draw(win)
	Line(Point(x_data[2],a_line*x_data[2]+b_line),Point(x_data[2]+x_data[1]*10.0,(x_data[2]+x_data[1]*10.0)*a_line+b_line)).draw(win)
	print x_data[2],a_line*x_data[2]+b_line,x_data[2]+x_data[1]*10.0,(x_data[2]+x_data[1]*10.0)*a_line+b_line
	
def calculate(x,y):
	l=len(x)
	x_average =0
	xx_average =0
	y_average =0
	xy_average =0
	for i in range(l):
		x_average += x[i]
		xx_average +=x[i]*x[i]
		y_average +=y[i]
		xy_average +=x[i]*y[i]
	ll=l*1.0
	x_average /=ll
	xx_average /=ll
	y_average /=ll
	xy_average /=ll
	b=(xy_average*x_average-xx_average*y_average)/(x_average**2-xx_average)
	a=(x_average*y_average-xy_average)/(x_average**2-xx_average)
	x_standardError,y_standardError=0,0
	for i in range(l):
		x_standardError+=(x[i]-x_average)**2
		y_standardError+=(y[i]-y_average)**2
	x_standardError=sqrt(x_standardError)/ll
	y_standardError=sqrt(y_standardError)/ll
	print "[x_average,x_standardError,xx_average,y_average,y_standardError,xy_average,a,b]"
    
	return [x_average,x_standardError,xx_average,y_average,y_standardError,xy_average,a,b]
def calculate2(x):
	l=len(x)
	x_average =0
	xx_average =0
	for i in range(l):
		x_average += x[i]
		xx_average +=x[i]*x[i]

	ll=l*1.0
	x_average /=ll
	xx_average /=ll
	x_standardError=0
	for i in range(l):
		x_standardError+=(x[i]-x_average)**2
	SS=x_standardError/(ll-1.0)
	x_standardError=sqrt(x_standardError)/ll
	ans={}
	ans['x_average'],ans['x_standardError'],ans['xx_average']=x_average,x_standardError,xx_average
	ans['S']=sqrt(SS)
	return ans
    
def main():
	x=[0.400,0.600,0.800,1.000,1.200,1.400,1.600,1.800]
	y=[10.4,15.5,23.5,25.6,30.5,35.5,40.2,45.2]
	p=[500,200,100]
	t=[401.00,400.73,400.67]
	data=calculate(p,t)
	for i in data:
		print i
def test1():
	U=[1,2,3,4,5,6,7,8]
	I=[3.1,4,5.2,6.1,7,7.9,8.9,10.0]
	data=calculate(I,U)
	a,b=data[4],data[5]
	win=draw_coordinate_systerm(['I/10**-3A',1.0,3.0],["U/V",1.0,1.0],I,U,a,b)
def test2():
	U=[0.400,0.600,0.800,1.000,1.200,1.400,1.600,1.800]
	I=[10.4,15.5,23.5,25.6,30.5,35.5,40.2,45.2]
	data=calculate(I,U)
	a,b=data[4],data[5]
	win=draw_coordinate_systerm(['I/10**-3A',5.0,10.0],["U/V",0.2,0.2],I,U,a,b)
	draw_points(win,x,y)
	
def main2():
        x2=[32.96387,32.97861,32.99345,33.00831,33.02333,33.03819]
        x3=[1050,1100,1120,1250,1280]
        a=calculate2(x2)
        print a
main2()

	

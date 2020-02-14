# a program to stimulate the soliton
#this is  the rod-string model of the soliton
from graphics import *
from math import *
import copy
import time
class bar:
    def __init__(self,x,theta,L2,win):
        self.line=Line(Point(x,0),Point(x-L2*sin(theta),-L2*cos(theta)))
        self.line.draw(win)
        self.ball=Circle(Point(x-L2*sin(theta),-L2*cos(theta)),1.5)
        self.ball.draw(win)
        self.ball.setFill('black')
        self.x=x
        self.win=win
        self.L2=L2
    def setTheta(self,theta):
        self.line.undraw()
        self.line=Line(Point(self.x,0),Point(self.x-self.L2*sin(theta),-self.L2*cos(theta)))
        self.line.draw(self.win)
        self.ball.undraw()
        self.ball=Circle(Point(self.x-self.L2*sin(theta),-self.L2*cos(theta)),1.5)
        self.ball.draw(self.win)
        self.ball.setFill('black')
    def undraw(self):
        self.line.undraw()
        self.ball.undraw()
def initial_condition1(rtheta,rw):#1-soliton
        rtheta[1]=11*pi/6
        rtheta[2]=10*pi/6
        rtheta[3]=8*pi/6
        rtheta[4]=7*pi/6
        rtheta[5]=6*pi/6
        rtheta[6]=4*pi/6
        rtheta[7]=2*pi/6
        rtheta[8]=pi/6
        rw[1]=20.0
        rw[2]=20.0
        rw[3]=20.0
        rw[4]=20.0
        rw[5]=10.0
        rw[6]=10.0
def initial_condition2(rtheta,rw):
        rtheta[1]=11*pi/6
        rtheta[2]=10*pi/6
        rtheta[3]=8*pi/6
        rtheta[4]=7*pi/6
        rtheta[5]=6*pi/6
        rtheta[6]=4*pi/6
        rtheta[7]=2*pi/6
        rtheta[8]=pi/6
        rtheta[-1]=11*pi/6
        rtheta[-2]=10*pi/6
        rtheta[-3]=8*pi/6
        rtheta[-4]=7*pi/6
        rtheta[-5]=6*pi/6
        rtheta[-6]=4*pi/6
        rtheta[-7]=2*pi/6
        rtheta[-8]=pi/6
        rtheta[1]=4*pi/6
        rtheta[2]=3*pi/6
        rtheta[3]=2*pi/6
        rtheta[4]=1*pi/6

        rw[1]=30.0
        rw[2]=30.0
        rw[3]=30.0
        rw[4]=20.0
        rw[5]=10.0
        rw[6]=10.0
        rw[-1]=30.0
        rw[-2]=30.0
        rw[-3]=30.0
        rw[-4]=20.0
        rw[-5]=10.0
        rw[-6]=10.0
def initial_condition3(rtheta,rw):
        rtheta[1]=11*pi/6
        rtheta[2]=10*pi/6
        rtheta[3]=8*pi/6
        rtheta[4]=7*pi/6
        rtheta[5]=6*pi/6
        rtheta[6]=4*pi/6
        rtheta[7]=2*pi/6
        rtheta[8]=pi/6
        rtheta[-1]=-11*pi/6
        rtheta[-2]=-10*pi/6
        rtheta[-3]=-8*pi/6
        rtheta[-4]=-7*pi/6
        rtheta[-5]=-6*pi/6
        rtheta[-6]=-4*pi/6
        rtheta[-7]=-2*pi/6
        rtheta[-8]=-pi/6
        rtheta[1]=4*pi/6
        rtheta[2]=3*pi/6
        rtheta[3]=2*pi/6
        rtheta[4]=1*pi/6

        rw[1]=30.0
        rw[2]=30.0
        rw[3]=30.0
        rw[4]=20.0
        rw[5]=10.0
        rw[6]=10.0
        rw[-1]=-30.0
        rw[-2]=-30.0
        rw[-3]=-30.0
        rw[-4]=-20.0
        rw[-5]=-10.0
        rw[-6]=-10.0
def initial_condition4(rtheta,rw):#1-soliton
        rtheta[1]=11*pi/36
        rtheta[2]=10*pi/36
        rtheta[3]=8*pi/36
        rtheta[4]=7*pi/36
        #rw[1]=6.0
        #rw[2]=5.0
        #rw[3]=4.0

def main():
        win=GraphWin('soliton',1280,400)
        win.setCoords(-10,-50,310,50)
        L1=5.0# L1 is the distance between two adjacent soliton
        L2=40.0# L2 is the length of tha bar of each soliton
        k=15.5 # k is the Hooker constant
        m=1.0 # m is the mass of the ball in the top of the soliton
        g=10.0 # g is the gravitational constant
        dt=0.01# t is the infinitesimal change in time
        
        rtheta=[]#theta is the angle of each soliton. rtheta is a list of theta
        nn=60# nn is the number of solitons
        rbar=[]
        for i in range(nn+1):
                rtheta.append(0)
                rbar.append(bar(L1*i,0,L2,win))
        rbar[0].undraw()
        rw=copy.deepcopy(rtheta)#w is the angular velocity
        rwa=copy.deepcopy(rtheta)#wa is the angular accelaration
        initial_condition4(rtheta,rw)

        #F1=k*(sqrt((rtheta[2]-rtheta[1])**2*L2*2+L1**2)-L1)
        F1=k*(sqrt((2*L2*sin((rtheta[nn-1]-rtheta[nn])/2))**2+L1**2)-L1)*(2*L2*sin((rtheta[nn-1]-rtheta[nn])/2))/sqrt((2*L2*sin((rtheta[nn-1]-rtheta[nn])/2))**2+L1**2)
        for i in range(100000):
            #print rtheta[1:5]
            F1=k*(sqrt((2*L2*sin((rtheta[2]-rtheta[1])/2))**2+L1**2)-L1)*(2*L2*sin((rtheta[2]-rtheta[1])/2))/sqrt((2*L2*sin((rtheta[2]-rtheta[1])/2))**2+L1**2)

            # F1 is the force from the second soliton to the first soliton
            rwa[1]=F1/m+g*sin(-rtheta[1])
            for n in range(2,nn):
                F1=k*(sqrt((2*L2*sin((rtheta[n+1]-rtheta[n])/2))**2+L1**2)-L1)*(2*L2*sin((rtheta[n+1]-rtheta[n])/2))/sqrt((2*L2*sin((rtheta[n+1]-rtheta[n])/2))**2+L1**2)

                # F1 is the force from the n+1 soliton to the n soliton
                F2=k*(sqrt((2*L2*sin((rtheta[n-1]-rtheta[n])/2))**2+L1**2)-L1)*(2*L2*sin((rtheta[n-1]-rtheta[n])/2))/sqrt((2*L2*sin((rtheta[n-1]-rtheta[n])/2))**2+L1**2)

                # F2 is the force from the n+1 soliton to the n soliton
                rwa[n]=(F2+F1)/m+g*sin(-rtheta[n])
            F2=k*(sqrt((2*L2*sin((rtheta[nn-1]-rtheta[nn])/2))**2+L1**2)-L1)*(2*L2*sin((rtheta[nn-1]-rtheta[nn])/2))/sqrt((2*L2*sin((rtheta[nn-1]-rtheta[nn])/2))**2+L1**2)
            
            # F2 is the force from the second last soliton to the last soliton
            rwa[nn]=F2/m+g*sin(-rtheta[nn])
            for n in range(1,nn+1):
                rw[n]+=rwa[n]*dt
            for n in range(1,nn+1):
                rtheta[n]+= rw[n]*dt
                rbar[n].setTheta(rtheta[n])
    
main()            
                            
            
            

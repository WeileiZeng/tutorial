# a program to stimulate the soliton
#this is  the rod-spring model of the soliton,
#to distinct it from the programs of rod-string model, I set a '0' before the
#sequence number of the program, such as 01,02,03...and directly use 1,2,3 to
#denote the programs for rod-string model


from graphics import *
from math import *
import copy
import time
class bar:
    def __init__(self,x,theta,L2,win):
        self.line=Line(Point(x,0),Point(x-L2*sin(theta),-L2*cos(theta)))
        self.line.draw(win)
        self.ball=Circle(Point(x-L2*sin(theta),-L2*cos(theta)),0.5)
        #self.ball.draw(win)
        self.ball.setFill('black')
        self.x=x
        self.win=win
        self.L2=L2

        self.phase=Point(x,theta%(2*pi)*100+50)#here, phase means phase
        
        self.sigh=self.phase
        
        self.phase.draw(win)
    def setTheta(self,theta):
        self.line.undraw()
        self.line=Line(Point(self.x,0),Point(self.x-self.L2*sin(theta),-self.L2*cos(theta)))
        self.line.draw(self.win)
##        self.ball.undraw()
##        self.ball=Circle(Point(self.x-self.L2*sin(theta),-self.L2*cos(theta)),0.5)
##        elf.ball.draw(self.win)
##        self.ball.setFill('black')

    def setw(self,w):#a function to draw w
        self.phase.undraw()
        self.phase=Point(self.x,w*2+50)#here, phase means angular velocity
        self.phase.draw(self.win)   
    def undraw(self):
        self.line.undraw()
##        self.ball.undraw()
        self.phase.undraw()
def printlist(ll):
    for i in ll:
        print i
def initial_condition1(rtheta,rw):
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
        
def main():
        win=GraphWin('soliton',1200,600)
        win.setCoords(-10,-50,290,100)
        L1=4.0# L1 is the distance between two adjacent soliton
        L2=40.0# L2 is the length of tha bar of each soliton
        k=500000.0 # k is the Hooker constant
        m=1.0 # m is the mass of the ball in the top of the soliton
        g=10.0 # g is the gravitational constant
        dt=0.01# t is the infinitesimal change in time
        J=m*(L2**2)# J is the rotational inertia of one pendulum
        rtheta=[]#theta is the angle of each soliton. rtheta is a list of theta
        nn=60# nn is the number of solitons
        rbar=[]
        for i in range(nn+1):
                rtheta.append(0)
                rbar.append(bar(L1*i,0,L2,win))
        rbar[0].undraw()
        rw=copy.deepcopy(rtheta)#w is the angular velocity
        initial_condition1(rtheta,rw)

        

        rwa=copy.deepcopy(rtheta)#wa is the angular accelaration
        #T1=k*((rtheta[2]-rtheta[1])
        F1=k*(sqrt((2*L2*sin((rtheta[nn-1]-rtheta[nn])/2))**2+L1**2)-L1)*(2*L2*sin((rtheta[nn-1]-rtheta[nn])/2))/sqrt((2*L2*sin((rtheta[nn-1]-rtheta[nn])/2))**2+L1**2)
        for i in range(100000):
            #print rw[1]
            T1=k*(rtheta[2]-rtheta[1])
            # T1 is the torque from the second soliton to the first soliton
            rwa[1]=T1/J+g*sin(-rtheta[1])
            for n in range(2,nn):
                T1=k*(rtheta[n+1]-rtheta[n])
                
                # F1 is the torque from the n+1 soliton to the n soliton
                T2=k*(rtheta[n-1]-rtheta[n])
                
                # T2 is the torque from the n-1 soliton to the n soliton
                rwa[n]=(T2+T1)/J+g*sin(-rtheta[n])
            T2=k*(rtheta[nn-1]-rtheta[nn])
            
            # T2 is the force from the second last soliton to the last soliton
            rwa[nn]=T2/J+g*sin(-rtheta[nn])
            for n in range(1,nn+1):
                rw[n]+=rwa[n]*dt
            for n in range(1,nn+1):
                rtheta[n]+= rw[n]*dt
                #print n,rw[n]*dt
                rbar[n].setTheta(rtheta[n])
                rbar[n].setw(rw[n])
            printlist(rwa)
    
main()            
                            
            
            

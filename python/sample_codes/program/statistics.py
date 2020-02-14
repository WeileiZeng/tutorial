#gai lu lun ji suan
import math
from math import *
def A(n,m):
    x=1
    for i in range(n):
        x*=m-i
    return x
        
def C(n,m):
    return A(n,m)/A(n,n)
def X_B(k,n,p):#binomial distribution
    return C(k,n)*(p**k)*((1-p)**(n-k))
def ode(a,b,dx=0.001):#definite integral
    ans=0
    #print int((b-a)/dx)+1
    i=0
    while i<int((b-a)/dx)+1:
        x=a+i*dx
        m,k,t=28.0/2.6868e25,1.3806504,273.15
        #f=4*pi*(m/(2*pi*k*t))**1.5*exp(-m*x*x/(2.0*k*t))*x*x
        f=1.0/x
        dy=f*dx
        ans+=dy
        i+=1
    return ans
        
def main1():
    print C(2,1000)*0.003**2*0.997**998
    print C(1,1000)*0.003*0.997**999
    a=0
    print X_B(0,1000,0.003)
    print 0.997**1000
def main2():
    m,k,t=28.0/2.6868e25,1.3806504,273.15
    vp=sqrt((2*k*t/m))
    N=1e-6/22.4*2.6868e25
    print vp
    a=ode(500,501)
def main3():
    print C(1,3)*C(1,2)/C(4,7)
def main4():
    #print ode(1.0,2.718051,0.0001)
    #print ode(1.0,2.718082,0.0001)
    #print ode(1.0,2.718278,0.000001)
    print ode(1.0,2.718279,0.000001)
def main5():
    print C(500,599)

main5()
            
    
    


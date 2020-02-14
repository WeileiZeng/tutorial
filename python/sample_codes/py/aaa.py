import math
from math import *

def main():
    a,b,c=134000,134100,134100
    average=(a+b+c)/3
    print 'average=',average
    ss=0
    for i in [a,b,c]:
        ss+=(i-average)**2
    ss/=3.0
    s=sqrt(ss)
    print 's=',s

    a,b,c=0.001,0.001,2.44/1339.9
    u=sqrt(a*a+b*b+c*c)
    print 'u= ',u
    u1=134000*u

    a,b,c=0.001,0.001,12.44/13406
    u=sqrt(a*a+b*b+c*c)
    print 'u= ',u
    u2=134100*u

    a,b,c=0.001,0.001,12.44/13407
    u=sqrt(a*a+b*b+c*c)
    print 'u= ',u
    u3=134100*u

    a,b,c=u1,u2,u3
    u=sqrt(a*a+b*b+c*c)
    print 'u_= ',u
    
    
    u_r=u/134000
    print 'u_r=',u_r
main()

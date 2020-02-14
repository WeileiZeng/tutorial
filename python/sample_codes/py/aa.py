from math import *
def main(a):
    d1=a[3]-a[0]
    d2=a[4]-a[1]
    d3=a[5]-a[2]
    d=(d1+d2+d3)/3
    print d1,d2,d3,d
    print 'deviation'
    print sqrt(((d1-d)**2+(d2-d)**2+(d3-d)**2)/2)/3*2.48
b=[32.96387,32.97861,32.99345,33.00831,33.02333,33.03819]#sodium light
c=[34.54066,34.55672,34.57313,34.58960,34.60606,34.62281]#plaser
def main2(a):
    d1=a[2]-a[0]
    d2=a[3]-a[1]
    d=(d1+d2)/2
    print d1,d2,d
    print 'deviation'
    print sqrt(((d1-d)**2+(d2-d)**2))/2*2.48
    



b=[35.23887,35.53892,35.81986,36.11276]#difference of lambda
main(c)

# fibonacci.py
from time import*
def fibo1(n):
    if n<0:
        print "false"
    elif n>1:
        return fibo1(n-1)+fibo1(n-2)
        
    else:
        return n


def fibo2(n):
        if n<0:
                print "false"
        elif n>1:
                a=0
                b=1
                for i in range(n-1):
                        c=a+b
                        a=b
                        b=c
                return c
        
        else:
                return n

def testTime():
        n=0
        while True:
                t1=clock()
                fibo1(n)
                t2=clock()
                print "time for ",n," is ",t2-t1
                n+=1

def printF():
        f0=0
        f1=1
        f2=1
        n=2
        An=1
        while True:
                #print n," : ",f2
                #An=n**1.5
                
                An*=1.61803398875
                f2=f0+f1
                print 1.0*f1/An
                f0=f1
                f1=f2
         
                n+=1
                
printF()

#testTime()
#print fibo2(100)

        
    

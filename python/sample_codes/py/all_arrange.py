#to show the all arranges of the sequence:a
import time

def main(a,b):#this function require the first value of b to be 0
    if b==len(a)-1:
        #print a
        return
    for i in range(b,len(a)):
        a[b],a[i]=a[i],a[b]
        main(a,b+1)
        a[b],a[i]=a[i],a[b]
def time_test(n):
    t1=time.clock()
    main(range(1,n+1),0)
    t2=time.clock()
    print t2-t1
a=[1,2,3,4]
c=[]
#main(range(1,10),0)
time_test(11)

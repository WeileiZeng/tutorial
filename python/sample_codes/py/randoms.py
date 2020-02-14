#create randon nnumbers
import random
from time import *
def randoms(n):
    rand=[]
    num=range(n+1)
    for i in range(n):
        a=random.randint(0,n-i-1)
        b=num[a]
        
        rand.append(b)
        del num[a]
    return rand
def main(n):
    a=clock()
    randoms(n)
    b=clock()
    print b-a
        
main(1000)

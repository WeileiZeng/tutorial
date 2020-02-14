#streets.py
# textbook 9.6_16
import random
import math
def main():
    ss=0
    for i in range(1000):   #oprate 1000 times
        x=0
        y=0
        for i in range(100):     # 30 blocks
            a=random.random()
            a=2*math.pi*a
            x=x+math.cos(a)
            y=y+math.sin(a)
        s=x*x+y*y
        ss=ss+s/1000.0
    print 'ss= ',ss
main()
    
                
    

#street.py
# textbook 9.6_15
import random
def main():
    ss=0
    for i in range(1000):   #oprate 1000 times
        x=0
        y=0
        for i in range(30):     # 30 blocks
            a=random.randint(1,4)  #'1,2,3,4'represent'front,back,left,right'
            if a==1:
                y=y+1
            elif a==2:
                y=y-1
            elif a==3:
                x=x-1
            else:
                x=x+1
        s=x*x+y*y
        ss=ss+s/1000.0
    print 'ss= ',ss
    raw_input("press any key to exit...")
main()
    
                
    

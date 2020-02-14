#square_sort.py
def square_sort(x):#find the squared sort of an number in limited accracy
    if x<0:
        return "nagetive number has no real squred sort. please enter a positive one"
    else:
        a=x
        b=0
        c=(a+b)/2.0
        d=c*c
        while abs(d-x)>0.00000001 and a>b:
            if d>x:
                a=c
                
            else:
                b=c
            print "a,b= ",a,b
            #print a>b
            c=(a+b)/2.0
            d=c*c
        print c,d
            
#square_sort(8856579168360000000)
#square_sort(8850000)

def judge_intergal_square_sort(x):#find whether an intergal number has an
    #intergal squared sort or not
    if x<0:
        return "nagetive number has no real squred sort. please enter a positive one"
    else:
        a=x
        b=0
        c=(a+b)/2
        d=c*c
        while a-b>1:
            c=(a+b)/2
            d=c*c           
            if d>x:
                a=c
                
            elif d<x:
                b=c
            else:
                #print x,"has an intergal squared sort: ",c
                return x
            #print "a,b,c= ",a,b,c
            #print "d,x= ",d,x
            #print a>b
        #print c,d
        if d!=x:
            #print x," has no intergal squared sort"
            return False

#judge_intergal_square_sort((121*169*19*18*21*23*37)**2+1)

squarenumbers=[]
for i in range(100000):
    a=judge_intergal_square_sort(i)
    if a>0:
        squarenumbers.append(a)
print squarenumbers
b=[]
for i in range(2,317):
    b.append(i**2)
print b==squarenumbers
    

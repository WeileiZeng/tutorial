from graphics import *

def main():
    win=GraphWin('window',1000,600)
    a=[]
    for i in range(1000):
        b=[]
        if i <20:
            for j in range(600):
                p=Point(i,j)
                p.draw(win)
                b.append(p)

main()

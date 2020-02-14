import py
import math
import button
import graphics
import horse
from graphics import *
class Stark():
    def __init__(self):
        self.stark=[]
    def append(self,x):
        self.stark.append(x)
    def pop(self):#del the last one of the stark and return it
        a=len(self.stark)
        if a>0:
            return self.stark.pop()
        else:
            return 0    

def main():
    win=GraphWin('horse',420,500)
    win.setCoords(0.0,-2.0,11.0,11.0)
    window=Rectangle(Point(0.4,0.4),Point(10.6,10.6))
    window.draw(win)
    back=button.button(win,Point(5.3,-0.9),1.5,1.0,'back')
    back.active()
    eexit=button.button(win,Point(10,-0.9),1.5,1.0,'exit')
    eexit.active()
    ss=horse.Stark()#contain the rectangles in positions the horse has gone
    road=horse.Stark()#to record the road the horse has gone for returning later 
    color=['gray','white']
    room=[]#draw the view of room,the place where the horse walks
    for i in range(10):
        room1=[]
        for j in range(10):
            rect=Rectangle(Point(j+0.5,i+0.5),Point(j+1.5,i+1.5))
            cc=color[(i%2+j%2)%2]
            rect.setFill(cc)
            rect.setOutline(cc)
            rect.draw(win)
            room1.append(rect)
        room.append(room1)
    #xiaoma=Circle(Point(1,1),0.3)#'xiaoma' refer to the horse
    #xiaoma.setFill('red')
    #xiaoma.setOutline('red')
    xiaoma=Image(Point(1,1),'horse6.gif')
    xiaoma.draw(win)
    xx=1
    yy=1
    pp=win.getMouse()
    while not eexit.judge(pp):
        x=pp.getX()
        y=pp.getY()
        print x,y
        if back.judge(pp):#
            last=road.pop()
            print 'last=',last
            if last==0:
                pass
            else:#delete the last rectangle and the last small-list in ss
                c=ss.pop()
                x1,y1=c[0],c[1]
                xiaoma.move(x1-xx,y1-yy)#the horse return
                xx=x1
                yy=y1
                last.undraw()
        elif x<10.5 and x>0.5 and y>0.5 and y<10.5:
            col=int(x+0.5)
            row=int(y+0.5)
            jj=int(1000*math.sqrt((xx-col)*(xx-col)+(yy-row)*(yy-row)))
            #jj is the distance from the place clicked to xiaoma
            if jj==2236:#judge if the horse goes in the right way,'2236'is related to math.sqrt(5)             
                rect=Rectangle(Point(xx-0.5,yy-0.5),Point(xx+0.5,yy+0.5))
                rect.setFill('blue')
                rect.setOutline('blue')
                rect.draw(win)
                road.append(rect)
                ss.append([xx,yy])
                xiaoma.move(col-xx,row-yy)
                xiaoma.undraw()
                xiaoma.draw(win)
                xx=col
                yy=row
        pp=win.getMouse()
                
    win.close()
main()

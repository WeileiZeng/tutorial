# a moving face of smile
# the image is set in a window (300*300)witn the coords(-10,-10,10,10)
# so the coords need be set according to the size of the window,
# otherwise the face would be funny
import py
import button
import time
import graphics
from graphics import *
def main1():
# draw the first smileface
    win=GraphWin('haha',600,600)
    win.setCoords(-30.0,-30.0,30.0,30.0)
    face=Circle(Point(0,0),6)
    eyes1=Oval(Point(-4,4),Point(-1.5,2))
    eyes2=Oval(Point(4,4),Point(1.5,2))
    eye1=Circle(Point(-2.8,2.85),0.8)
    eye2=Circle(Point(2.8,2.85),0.8)
    eye1.setFill('black')
    eye2.setFill('black')
    nose=Oval(Point(-1,1.5),Point(1,-2))
    nose.setFill('black')
    mouth=Circle(Point(0,-4),1.3)
    face.draw(win)
    eyes1.draw(win)
    eyes2.draw(win)
    eye1.draw(win)
    eye2.draw(win)
    nose.draw(win)
    mouth.draw(win)
# draw some button
    left=button.button(win,Point(-25,-28),4,2,'<==')
    right=button.button(win,Point(-15,-28),4,2,'==>')
    auto=button.button(win,Point(-10,-25),4,2,'auto')
    up=button.button(win,Point(-20,-25),4,2,'up')
    down=button.button(win,Point(-20,-28),4,2,'down')
    blink=button.button(win,Point(-5,-28),4,2,'blink')
    quit1=button.button(win,Point(-0,-28),4,2,'quit')
    haha=button.button(win,Point(-0,-25),4,2,'haha')
    soon=button.button(win,Point(5,-25),4,2,'soon')
    slow=button.button(win,Point(5,-28),4,2,'slow')
    left.active()
    right.active()
    auto.active()
    up.active()
    down.active()
    blink.active()
    quit1.active()
    haha.active()
    soon.active()
    slow.active()
    mm=1
    
# operate with the owner's orders
    for i in range(1000):
        pp=win.getMouse()
        jj1=left.judge(pp)
        jj2=right.judge(pp)
        jj3=auto.judge(pp)
        jj4=up.judge(pp)
        jj5=down.judge(pp)
        jj6=blink.judge(pp)
        jj7=quit1.judge(pp)
        jj8=haha.judge(pp)
        jj9=soon.judge(pp)
        jj10=slow.judge(pp)
        if jj1:    #left
            aa=-mm
            bb=0
            face.move(aa,bb)
            eyes1.move(aa,bb)
            eyes2.move(aa,bb)
            eye1.move(aa,bb)
            eye2.move(aa,bb)
            nose.move(aa,bb)
            mouth.move(aa,bb)

        if jj2:    #right
            aa=mm
            bb=0
            face.move(aa,bb)
            eyes1.move(aa,bb)
            eyes2.move(aa,bb)
            eye1.move(aa,bb)
            eye2.move(aa,bb)
            nose.move(aa,bb)
            mouth.move(aa,bb)
        if jj3:    #auto
            pp1=win.getMouse()
            aa1=pp1.getX()
            bb1=pp1.getY()
            pp2=face.getCenter()
            aa2=pp2.getX()
            bb2=pp2.getY()
            aa=aa1-aa2
            bb=bb1-bb2
            
            face.move(aa,bb)
            eyes1.move(aa,bb)
            eyes2.move(aa,bb)
            eye1.move(aa,bb)
            eye2.move(aa,bb)
            nose.move(aa,bb)
            mouth.move(aa,bb)
        if jj4:    #up
            aa=0
            bb=mm
            face.move(aa,bb)
            eyes1.move(aa,bb)
            eyes2.move(aa,bb)
            eye1.move(aa,bb)
            eye2.move(aa,bb)
            nose.move(aa,bb)
            mouth.move(aa,bb)
        if jj5:    #down
            aa=0
            bb=-mm
            face.move(aa,bb)
            eyes1.move(aa,bb)
            eyes2.move(aa,bb)
            eye1.move(aa,bb)
            eye2.move(aa,bb)
            nose.move(aa,bb)
            mouth.move(aa,bb)
        if jj6:    #blink
# this is the blinking opration and the opration is set in the center of
# point(0,0),so there will be some adoption
            pp2=face.getCenter()
            aa2=pp2.getX()
            bb2=pp2.getY()
            blinkoff=button.button(win,Point(-5,-25),5.5,2,'blink off')
            blinkoff.active()
            left.unactive()
            right.unactive()
            auto.unactive()
            up.unactive()
            down.unactive()
            blink.unactive()
            quit1.unactive()
            haha.unactive()
            
            
            for i in range(20):
                #close
                time.sleep(0.5)
                pp=win.checkMouse()
                if pp==None:
                    pass
                else:
                    if blinkoff.judge(pp):
                        blinkoff.close()
                        left.active()
                        right.active()
                        auto.active()
                        up.active()
                        down.active()
                        blink.active()
                        quit1.active()
                        haha.active()
                        break    
                eyes1.undraw()
                eyes2.undraw()
                eye1.undraw()
                eye2.undraw()
                eyes1=Oval(Point(-4+aa2,3+bb2),Point(-1.5+aa2,2+bb2))  #
                eyes2=Oval(Point(4+aa2,3+bb2),Point(1.5+aa2,2+bb2))    #
                eye1=Circle(Point(-2.8+aa2,2.5+bb2),0.5)      #
                eye2=Circle(Point(2.8+aa2,2.5+bb2),0.5)       #
                eye1.setFill('black')
                eye2.setFill('black')
                eyes1.draw(win)
                eyes2.draw(win)
                eye1.draw(win)
                eye2.draw(win)
                # open
                time.sleep(0.5)
                pp=win.checkMouse()
                if pp==None:
                    pass
                else:
                    if blinkoff.judge(pp):
                        blinkoff.close()
                        left.active()
                        right.active()
                        auto.active()
                        up.active()
                        down.active()
                        blink.active()
                        quit1.active()
                        haha.active()
                        break    
                eyes1.undraw()
                eyes2.undraw()
                eye1.undraw()
                eye2.undraw()
                eyes1=Oval(Point(-4+aa2,4+bb2),Point(-1.5+aa2,2+bb2))
                eyes2=Oval(Point(4+aa2,4+bb2),Point(1.5+aa2,2+bb2))
                eye1=Circle(Point(-2.8+aa2,2.85+bb2),0.8)
                eye2=Circle(Point(2.8+aa2,2.85+bb2),0.8)
                eye1.setFill('black')
                eye2.setFill('black')
                eyes1.draw(win)
                eyes2.draw(win)
                eye1.draw(win)
                eye2.draw(win)
        if jj7:    #quit
            win.close()
            break
        if jj8:    #haha
            pp2=face.getCenter()
            aa2=pp2.getX()
            bb2=pp2.getY()
            hh1=Line(Point(aa2,-4+bb2),Point(1.5+aa2,-6.8+bb2))
            hh2=Line(Point(aa2,-4+bb2),Point(2.5+aa2,-6.5+bb2))
            hh3=Oval(Point(aa2,-6.5+bb2),Point(6+aa2,-9+bb2))
            hh4=Text(Point(3+aa2,-7.75+bb2),'haha!!')
            hh4.draw(win)
            hh1.draw(win)
            hh2.draw(win)
            hh3.draw(win)
            time.sleep(1)
            hh1.undraw()
            hh2.undraw()
            hh3.undraw()
            hh4.undraw()
        if jj9:    #soon
            mm=2.0*mm
        if jj10:    #slow
            mm=mm/2.0
            
            
"""





    
      
#   blink
    for i in range(20):
        # close
        time.sleep(0.5)
        eyes1.undraw()
        eyes2.undraw()
        eye1.undraw()
        eye2.undraw()
        eyes1=Oval(Point(-4,3),Point(-1.5,2))  #
        eyes2=Oval(Point(4,3),Point(1.5,2))    #
        eye1=Circle(Point(-2.8,2.5),0.5)      #
        eye2=Circle(Point(2.8,2.5),0.5)       #
        eye1.setFill('black')
        eye2.setFill('black')
        eyes1.draw(win)
        eyes2.draw(win)
        eye1.draw(win)
        eye2.draw(win)
        # open
        time.sleep(0.5)
        eyes1.undraw()
        eyes2.undraw()
        eye1.undraw()
        eye2.undraw()
        eyes1=Oval(Point(-4,4),Point(-1.5,2))
        eyes2=Oval(Point(4,4),Point(1.5,2))
        eye1=Circle(Point(-2.8,2.85),0.8)
        eye2=Circle(Point(2.8,2.85),0.8)
        eye1.setFill('black')
        eye2.setFill('black')
        eyes1.draw(win)
        eyes2.draw(win)
        eye1.draw(win)
        eye2.draw(win)
def close():
    win.close()
def move(dx,dy):
    eyes1.move(dx,dy)
    eyes2.move(dx,dy)
    eye1.move(dx,dy)
    eye2.move(dx,dy)
    nose.move(dx,dy)
    mouth.move(dx,dy)
    face.move(dx,dy)
"""

main1()
        

        

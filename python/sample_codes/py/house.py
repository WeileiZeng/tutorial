#   draw a mini house
import time
import graphics
from graphics import *
win = GraphWin('house',300,300)
win.setCoords(0,0,10.0,10.0)
# draw the roof
words=Text (Point(5,9),'click  the top of the roof ')
words.draw(win)
p1=win.getMouse()
p1.draw(win)
x1=p1.getX()
y1=p1.getY()
words.setText( 'click the leg of the roof')
p2=win.getMouse()
x2=p2.getX()
y2=p2.getY()
while y2>y1 or x2==x1:
    wordss=Text(Point(5,9.6),'the leg cannot be higher than the top!')
    wordss.draw(win)
    words.setText('click the leg of the roof')
    time.sleep(1)
    wordss.undraw()
    p2=win.getMouse()
    x2=p2.getX()
    y2=p2.getY()
y3=y2
x3=2*x1-x2
p3=Point(x3,y3)
roof=Polygon(p1,p2,p3)
roof.draw(win)
# draw the house
words.setText('click the leg of the house')
p4=win.getMouse()
x4=p4.getX()
y4=p4.getY()
if x2>x3:
    a = x3
    b = x2
else:
    a=x2
    b=x3
while x4<a or x4>b or y4>y2:
    wordss=Text(Point(5,9.6),'the leg woundnot be wider than the roof')
    wordss.draw(win)
    words.setText('click the leg of the house')
    time.sleep(1)
    wordss.undraw()
    p4=win.getMouse()
    x4=p4.getX()
    y4=p4.getY()
x5=2*x1-x4
y5=y2
p5=Point(x5,y5)
house=Rectangle(p4,p5)
house.draw(win)
# draw the door
words.setText('click the position of the door')
p6=win.getMouse()
x6=p6.getX()
y6=p6.getY()
if x4>x5:
    c = x4
    d = x5
else:
    c=x5
    d=x4
while x6<d or x6>c or y6<y4 or y6>y2:
    wordss=Text(Point(5,9.6),'the door should be in the square')
    wordss.draw(win)
    words.setText('click the position of the door')
    time.sleep(1)
    wordss.undraw()
    p6=win.getMouse()
    x6=p6.getX()
    y6=p6.getY()
y7=y4
x7=x6+(x1-x6)/2
p7=Point(x7,y7)
door=Rectangle(p6,p7)
door.draw(win)
# draw the window
words.setText('click the position of the window')
p8=win.getMouse()
x8=p8.getX()
y8=p8.getY()
while x8<a or x8>b or y8<y4 or y8>y2:
    wordss=Text(Point(5,9.6),'the window should be in the square')
    wordss.draw(win)
    words.setText('click the position of the window')
    time.sleep(1)
    wordss.undraw()
    p8=win.getMouse()
    x8=p8.getX()
    y8=p8.getY()
x9=x8-(x8-x1)/2
y9=y8+(y2-y8)/2
p9=Point(x9,y9)
window=Rectangle(p8,p9)
window.draw(win)
# end and close
wordss=Text(Point(5,9.5),'the house is beautiful!')
wordss.draw(win)
words.setText('well done!')
time.sleep(5)
Text(Point(5,1),'click any where...').draw(win)
pp=win.getMouse()
win.close()






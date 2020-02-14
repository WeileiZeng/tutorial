# cardplay.py  wrote by Tianyu Zhu
import button
import graphics
import random
from graphics import *
from button import *
def randoms(n):
    randlist = []
    num = range(52)
    for i in range(n):
        a=random.randint(0,51-i)
        b=num[a]
        randlist.append(b)
        del num[a]
    return randlist
def start(filename,win):
    poke=[]                
    randlist=randoms(13)
    for i in range(13):
        image = Image(Point(5+3+(i+1)*2,35),filename[randlist[i]])
        poke.append(image)
        poke[i].draw(win)
    return poke
def play(poke,getlist,win):
    k=0
    for i in getlist:
        if i<>0:
            poke[i].move(-2*i+k,15)
            k=k+2
    while True:
        p=getMouse()
        if Quit.clicked(p):qquit(win)
        if Undo.clicked(p):undo(poke,win)
def getout(poke,p,win):
    get = True
    notgetlist = range(13)
    getlist = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
    while get:
        for j in notgetlist:
            if j==12 and p.getX()<=5+2*j+10 and p.getX()>=5+2*j and p.getY()<=42.5 and p.getY()>=27.5:
                poke[j].move(0,2)
                getlist[j]=j
                notgetlist[j]=-1
            elif p.getX()<=7+2*j and p.getX()>=5+2*j and j<>-1 and p.getY()<=42.5 and p.getY()>=27.5:
                poke[j].move(0,2)
                getlist[j]=j
                notgetlist[j]=0
        for j in getlist:
            if j==12 and p.getX()<=5+2*j+10 and p.getX()>=5+2*j and p.getY()<=44.5 and p.getY()>=29.5:
                poke[j].move(0,2)
                getlist[j]=j
                notgetlist[j]=0
            elif p.getX()<=7+2*j and p.getX()>=5+2*j and j<>-1 and p.getY()<=44.5 and p.getY()>=29.5:
                poke[j].move(0,-2)
                getlist[j]=-1
                notgetlist[j]=j
        Play.activate()
        if Play.clicked(p):
            Play.deactivate()
            Undo.activate()
            play(poke,getlist,win)
            get=False
        p=win.getMouse()
        if Quit.clicked(p):qquit(win)
def qquit(win):
    win.close()
def undo(poke,win):
    for i in range(13):
        poke[i].draw(win)
    while True:
        p=win.getMouse()
        if Quit.clicked(p):qquit(win)
        if p.getX()<=39 and p.getX()>=5 and p.getY()<=44.5 and p.getY()>=29.5:
            Play.activate()
            Undo.deactivate()
            getout(poke,p,win)
def main():
    win=GraphWin('Card',800,700)
    win.setCoords(0.0,0.0,80.0,70.0)
    filename = ['1.gif','2.gif','3.gif','4.gif','5.gif','6.gif','7.gif','8.gif','9.gif','10.gif',
                '11.gif','12.gif','13.gif','14.gif','15.gif','16.gif','17.gif','18.gif','19.gif','20.gif',
                '21.gif','22.gif','23.gif','24.gif','25.gif','26.gif','27.gif','28.gif','29.gif','30.gif',
                '31.gif','32.gif','33.gif','34.gif','35.gif','36.gif','37.gif','38.gif','39.gif','40.gif',
                '41.gif','42.gif','43.gif','44.gif','45.gif','46.gif','47.gif','48.gif','49.gif','50.gif',
                '51.gif','52.gif']
    Start = Button(win,Point(10,10),10,5,'Start')                
    Deal = Button(win,Point(25,10),10,5,'Deal')
    Play = Button(win,Point(40,10),10,5,'Play')
    Undo = Button(win,Point(55,10),10,5,'Undo')
    Quit = Button(win,Point(70,10),10,5,'Quit')
    Start.activate()
    Quit.activate()
    Deal.deactivate()
    Play.deactivate()
    Undo.deactivate()
    flag=True
    while flag:
        p=win.getMouse()
        if Start.clicked(p):
            poke = start(filename,win)
            flag=False
        if Quit.clicked(p):
            qquit(win)
    Start.deactivate()
    Deal.activate()
    flag=True
    while flag:
        p=win.getMouse()
        if Deal.clicked(p):
            poke = start(filename,win)
        if p.getX()<=39 and p.getX()>=5 and p.getY()<=44.5 and p.getY()>=29.5:
            Deal.deactivate()
            Play.activate()
            getout(poke,p,win)
            flag=False
        if Quit.clicked(p):qquit(win)
    win.close()
main()

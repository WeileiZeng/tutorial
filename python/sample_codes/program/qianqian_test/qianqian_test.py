#qianqian_test.py
import graphics
import py
import button
import random
import time
from graphics import *
def create_multiplication():
    a=random.randint(1,9)
    b=random.randint(1,9)
    if a>b:
        a,b=b,a
    question='%d x %d ='%(a,b)
    answer=a*b
    return [question,answer]
def create_addition():
    a=random.randint(1,99)
    b=random.randint(1,99)
    while a+b>100:
        a=random.randint(1,99)
        b=random.randint(1,99)
    question='%d+%d='%(a,b)
    answer=a+b
    return [queston,answer]
def create_subtracton():
    a=random.randint(1,99)
    b=random.randint(1,99)
    while a<b:
        a=random.randint(1,99)
        b=random.randint(1,99)
    question='%d-%d='%(a,b)
    answer=a-b
    return [queston,answer]

        

    
    
    
def main1():#create questons one by one
    win=GraphWin("qinaqian test",400,400)
    win.setCoords(0,0,20.0,20.0)
    start=button.button(win,Point(5.0,2.0),3.0,2.0,"start")
    eexit=button.button(win,Point(15.0,2.0),3.0,2.0,'exit')
    question=Text(Point(7.0,10.0),"")
    answer=Text(Point(15.0,10.0),"")
    question.draw(win)
    answer.draw(win)
    entry=Entry(Point(11.0,10.0),5)
    entry.draw(win)
    pp=win.getMouse()
    for i in range(20):
        q_a=create_multiplication()
        question_text,answer_text=q_a[0],q_a[1]
        print question_text,answer_text
        question.setText(question_text)
        pp=win.getMouse()
        while int(entry.getText()) !=answer_text:
            print entry.getText()
            pp=win.getMouse()
        answer.setText(answer_text)
        pp=win.getMouse()
        answer.setText('')
def main2():#create questons one by one
    win=GraphWin("qinaqian test",400,700)
    win.setCoords(0,0,20.0,40.0)
    start=button.button(win,Point(5.0,2.0),3.0,1.6,"start")
    eexit=button.button(win,Point(15.0,2.0),2.7,1.6,'exit')
    Image(Point(15.0,2.0),'c://Python26/program/qianqian_test/tuichu.gif').draw(win)
    kaishi=Image(Point(5.0,2.0),'c://Python26/program/qianqian_test/kaishi.gif')
    kaishi.draw(win)
    question=Text(Point(7.0,10.0),"")
    answer=Text(Point(15.0,10.0),"")
    question.draw(win)
    answer.draw(win)
    pp=win.getMouse()
    while not start.judge(pp):
        pp=win.getMouse()
    
    Image(Point(5.0,2.0),'c://Python26/program/qianqian_test/jiaojuan.gif').draw(win)
    answer_list=[]
    entry_list=[]
    duicuo=[]
    for i in range(20):
        duicuo.append([])
        duicuo[i].append(Image(Point(15.0,37.5-i*1.75),'c://Python26/program/qianqian_test/dui.gif'))
        duicuo[i].append(Image(Point(16.5,37.5-i*1.75),'c://Python26/program/qianqian_test/cuo.gif'))
        q_a=create_multiplication()
        question_text,answer_text=q_a[0],q_a[1]#
        Text(Point(5.0,37.5-i*1.75),question_text).draw(win)#
        entry=Entry(Point(9.0,37.5-i*1.75),3)
        entry.draw(win)
        entry_list.append(entry)#
        answer=Text(Point(11.0,37.5-i*1.75),answer_text)
        answer_list.append(answer)#
    pp=win.getMouse()
    while not eexit.judge(pp):
        
        if start.judge(pp):
            for i in range(20):
                answer_list[i].draw(win)
                
                if len(entry_list[i].getText())>0 and int(entry_list[i].getText())==answer_list[i].getText():
                    duicuo[i][0].draw(win)
                else:
                    duicuo[i][1].draw(win)
            break
        
        pp=win.getMouse()
    pp=win.getMouse()    
    win.close()
main2()
    

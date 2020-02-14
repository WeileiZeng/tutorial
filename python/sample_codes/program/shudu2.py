#shudu.py
#a program to find the answer of a shudu problem
import py
from graphics import *
from button import *

def getquestion():
    win=GraphWin('shudu',500,500)
    win.setCoords(-2,-2,11,11)
    aa=[]
    for i in range(9):
        aa2=[]
        for j in range(9):
            a=Entry(Point(i,j),2)
            a.draw(win)
            aa2.append(a)
        aa.append(aa2)
    enter=button(win,Point(10,2),2,1,'enter')
    
    if enter.click():
        for i in range(9):
            for j in range(9):
                print aa[i][j].getText()
        
    
    



def check(question):
    for i in range(9):
        if 0 in question[i]:
            return 1
    return 0    
def listprint(lists):
    for i in lists:
        print i
        
def main(question):
    print question
    while check(question)==1:
    
        for i in range(9):
            for j in range(9):
                if question[i][j]==0:
                    #ans=[1,2,3,4,5,6,7,8,9]
                    ans={1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9}
                    for var in range(1,10):
                        #print '111var= ',var
                        for n in range(9):
                            if question[i][n]==var or question[n][j]==var:
##                                print 'var= ',var
##                                print 'question[i][n]= ',question[i][n]
##                                print 'question[n][j]= ',question[n][j]
##                                print 'here, delete var= ', var, ans
                                try:
                                    del ans[var]
                                except:
                                    pass
                            for row in range(3):
                                for col in range(3):
                                    if question[i-i%3+row][j-j%3+col]==var:
                                        try:
                                            del ans[var]
                                        except:
                                            pass
                    if len(ans)==1:
                            #print 'change'
                            question[i][j]=ans.keys()[0]
    listprint(question) 
                            
getquestion()                  
            
question=[
[6,7,4,0,0,2,3,0,0],
[1,0,3,6,0,4,2,7,0],
[5,0,2,0,1,3,0,8,6],
[0,0,6,1,7,0,9,0,8],
[2,0,8,4,0,6,0,5,3],
[0,0,9,0,3,0,6,4,1],
[8,4,5,0,6,0,1,9,2],
[0,6,0,8,0,1,0,3,4],
[3,2,1,5,0,9,8,0,7]]

#main(question)


[[6, 7, 4, 9, 8, 2, 3, 1, 5],
 [1, 8, 3, 6, 5, 4, 2, 7, 9],
 [5, 9, 2, 7, 1, 3, 4, 8, 6],
 [4, 3, 6, 1, 7, 5, 9, 2, 8],
 [2, 1, 8, 4, 9, 6, 7, 5, 3],
 [7, 5, 9, 2, 3, 8, 6, 4, 1],
 [8, 4, 5, 3, 6, 7, 1, 9, 2],
 [9, 6, 7, 8, 2, 1, 5, 3, 4],
 [3, 2, 1, 5, 4, 9, 8, 6, 7]]

# a small module to make some circles
import graphics
import button
import time
from graphics import *
def main():
	win=GraphWin("win",800,400)
	win.setCoords(0.0,0.0,40.0,20.0)
	a=Point(5,5)
	color=['red','blue','yellow','green','orange']
	
	question1="hello!\nI am one of tongxin\'s friends,\nNice to meet you Miss Wang!\nand I want to talk something about him with you,\nwell,you just need to answer the \nfollowing question by 'yes' or 'no'"
	tt=Text(Point(15.0,10.0),question1)
	tt.draw(win)
	time.sleep(2)


	question2="i think that tongxin is a very nice person,\nat all the time he is missing you ,he told me.\n Do you think he gave you enough warmth,enough love and enough happiness?"
	tt.setText(question2)

	#tt1=Text(Point(5.0,12.0),question2)
	
	#tt1.draw(win)
	tt2=Text(Point(5.0,10.0),"yes or no?")
	tt2.draw(win)
	en1=Entry(Point(5.0,8.0),10)
	en1.draw(win)
	yes=button.button(win,Point(4.0,4.0),2.0,1.0,'yes')
	no=button.button(win,Point(8.5,4.0),2.0,1.0,'no')
	Text(Point(6.0,4.0),"or").draw(win)
	Text(Point(10.0,4.0),"?").draw(win)
	pp=win.getMouse()
	if yes.judge(pp):
		Text(Point(5.0,2.0),"I think so,too").draw(win)
		win.getMouse()
	if no.judge(pp):
                pass
        image1= Image(Point(20.0,10.0),"")
        
	win.close()
main()

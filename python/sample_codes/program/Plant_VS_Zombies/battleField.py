from graphics import *


def main():
    win=GraphWin("Plant vs Zombies",800,600)
    
    image = Image(Point(100,100),"gif/accessories_00.gif")
    image = Image(Point(100,100),"gif/Pumpkin_damage2.gif")

    image.draw(win)
    win.getMouse()
    win.close()


#def Credits_Flower_petal():


main()


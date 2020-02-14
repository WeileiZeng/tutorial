import py
import random
import button
import time
import graphics
from graphics import *
def main():
    win=GraphWin('snake',420,500)
    win.setCoords(0.0,-4.0,21.0,21.0)
    window=Rectangle(Point(0.4,0.4),Point(20.6,20.6))
    window.draw(win)
main()

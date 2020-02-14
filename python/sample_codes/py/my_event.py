from Tkinter import *

class KeysApp(Frame):
    def __init__(self): 
        Frame.__init__(self)
        self.txtBox = Text(self)
        self.txtBox.bind("<space>", self.doQuitEvent)
        self.txtBox.bind("<Key>", self.doKeyEvent)
        self.txtBox.pack()
        self.pack()
        
    def doQuitEvent(self,event):
        import sys
        sys.exit()

    def doKeyEvent(self,event):
        str = "%d\n" % event.keycode
        self.txtBox.insert(END, str)
        return "break"
        
myApp = KeysApp()
myApp.mainloop(2)


import Tkinter
from Tkconstants import *



def main():
    tk = Tkinter.Tk()
    frame = Tkinter.Frame(tk, relief=RIDGE, borderwidth=2)
    frame.pack(fill=BOTH,expand=1)
    label = Tkinter.Label(frame, text="Hello, World")
    label.pack(fill=X, expand=1)
    button = Tkinter.Button(frame,text="Exit",command=tk.destroy)
    button.pack(side=BOTTOM)
    tk.mainloop()
    menu=Tkinter.Menu()
    a=Tkinter.Canvas()
    a.create_image(100,100,"gif/Pumpkin_damage2.gif")
    a.pack(fill=X, expand=1)


main()

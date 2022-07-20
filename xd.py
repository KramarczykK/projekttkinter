from tkinter import *

root = Tk()


def MyClick():
    myLabel1 = Label(root, text = "Jazda z tym projektem")
    myLabel2 = Label(root, text = "Hej MEREZINIO")

    myLabel1.pack()
    myLabel2.pack()

    #myLabel1.grid(row = 0, column = 0)
    #myLabel2.grid(row = 1, column = 0)

myButton = Button(root, text = "Click me!", command = MyClick, fg = "green", bg = "pink")
myButton.pack()

root.mainloop()



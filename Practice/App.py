from tkinter import *

root = Tk()


def my_Click():
    myLable = Label(root, text="Label Created")
    myLable.pack()


myBtn = Button(root, text="Click Me!!", padx=50, command=my_Click)
myBtn.pack()

root.mainloop()

from tkinter import *

root = Tk()

e = Entry(root, width=50)
e.pack()
e.insert(0, "Enter your Name : ")

def my_Click():
    hello =  "Hello "+e.get()
    myLable = Label(root, text=hello)
    myLable.pack()


myBtn = Button(root, text="Enter your Name", padx=50, command=my_Click)
myBtn.pack()

root.mainloop()


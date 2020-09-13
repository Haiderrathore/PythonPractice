from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Practicing")
root.iconbitmap("H:/Python Git/PythonPractice/Practice/tnt.ico")

PATTIES = [
    ("Beef", "Beef"),
    ("Mutton", "Mutton"),
    ("Fish", "Fish"),
    ("Chicken", "Chicken"),
]
burger = StringVar()
burger.set("Please Select one Flavor")

for text, patty in PATTIES:
    Radiobutton(root, text=text, variable=burger, value=patty).pack(anchor=W)


def clicked(value):
    my_label = Label(root, text=burger.get())
    my_label.pack()


# Radiobutton(root, text="Option 1", variable=var, value=1, command=lambda: clicked(var.get())).pack()

my_label = Label(root, text=burger.get())
my_label.pack()

my_btn = Button(root, text="Click Me", command=lambda: clicked(burger.get()))
my_btn.pack()

root.mainloop()

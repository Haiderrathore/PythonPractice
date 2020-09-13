from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Practicing")
root.iconbitmap("H:/Python Git/PythonPractice/Practice/tnt.ico")

my_img = ImageTk.PhotoImage(Image.open("Logo.JPG"))
my_label = Label(image=my_img)

btn_quit = Button(root, text="Exit",  command=root.quit)
btn_quit.pack()


root.mainloop()

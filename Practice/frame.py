from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Practicing")
root.iconbitmap("H:/Python Git/PythonPractice/Practice/tnt.ico")
frame = LabelFrame(root, text="My Frame", padx=50, pady=50)
frame.pack(padx=10, pady=10)

btn= Button(frame, text="DONT CLICKK")
btn2= Button(frame, text="OR HERE")

btn.grid(row=0,column=0)
btn2.grid(row=0,column=1)
root.mainloop()

from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Practicing")
root.iconbitmap("H:/Python Git/PythonPractice/Practice/tnt.ico")

my_img1 = ImageTk.PhotoImage(Image.open("Images/IMG_1.jpg"))
my_img2 = ImageTk.PhotoImage(Image.open("Images/IMG_2.jpg"))
my_img3 = ImageTk.PhotoImage(Image.open("Images/IMG_3.jpg"))
my_img4 = ImageTk.PhotoImage(Image.open("Images/IMG_4.jpg"))
my_img5 = ImageTk.PhotoImage(Image.open("Images/IMG_5.jpg"))

image_list = [my_img1, my_img2, my_img3, my_img4, my_img5]

status = Label(root, text="Image 1 of " + str(len(image_list)), bd=1, relief=SUNKEN,
               anchor=E)

my_label = Label(image=my_img1)
my_label.grid(row=0, column=0, columnspan=3)


def forward(image_number):
    global my_label
    global btn_forward
    global btn_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number - 1])
    btn_forward = Button(root, text=">>", command=lambda: forward(image_number + 1))
    btn_back = Button(root, text="<<", command=lambda: back(image_number - 1))

    if image_number == 5:
        btn_forward = Button(root, text=">>", command=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    btn_back.grid(row=1, column=0)
    btn_forward.grid(row=1, column=2)
    status = Label(root, text="Image "+str(image_number)+" of " + str(len(image_list)), bd=1, relief=SUNKEN,
                   anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)


def back(image_number):
    global my_label
    global btn_forward
    global btn_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number - 1])
    btn_forward = Button(root, text=">>", command=lambda: forward(image_number + 1))
    btn_back = Button(root, text="<<", command=lambda: back(image_number - 1))

    if image_number == 1:
        btn_back = Button(root, text="<<", command=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    btn_back.grid(row=1, column=0)
    btn_forward.grid(row=1, column=2)

    status = Label(root, text="Image " + str(image_number) + " of " + str(len(image_list)), bd=1, relief=SUNKEN,
                   anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)



btn_back = Button(root, text="<<", command=back, state=DISABLED)
btn_quit = Button(root, text="Exit Viewer", command=root.quit)
btn_forward = Button(root, text=">>", command=lambda: forward(2))

btn_back.grid(row=1, column=0)
btn_quit.grid(row=1, column=1)
btn_forward.grid(row=1, column=2, pady=10)
status.grid(row=2, column=0, columnspan=3, sticky=W+E)

root.mainloop()

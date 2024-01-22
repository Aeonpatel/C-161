from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import os
from tkinter import messagebox

root = Tk()
root.minsize(600, 600)
root.maxsize(600, 600)

open_img = ImageTk.PhotoImage(Image.open("open.png"))
save_img = ImageTk.PhotoImage(Image.open("save.png"))
run_img = ImageTk.PhotoImage(Image.open("run.jpeg"))

label_file_name = Label(root, text = "File Name :", bg = "white")
label_file_name.place(relx = 0.40, rely = 0.05, anchor = CENTER)

input_file_name = Entry(root)
input_file_name.place(relx = 0.57, rely = 0.05, anchor = CENTER)

my_text = Text(root, height = 33, width = 74, bg = "gray", fg = "white")
my_text.place(relx = 0.5, rely = 0.55, anchor = CENTER)

name=""
def open_file():
    global name
    label_file_name.delete(0,END)
    my_text.delete(1.0,End)
    html_file = filedialog.askopenfile(title="Html file open" , filetypes=(("Htmlfiles","*.html"),))
    htm_file.print()
    name = os.path.basename(html_file)
    formated_name = name.split('.')[0]
    input_file_name.insert(END,formated_name)
    html_file = open(formated_name,'r')
    paragraph = html_file.read()
    my_text.insert(END,paragraph)
    html_file.close()
    

open_button = Button(root, image=open_img, text = "Open File" , command=open_file)
open_button.place(relx = 0.05, rely = 0.05, anchor = CENTER)

save_button = Button(root, image = save_img, text = "Save File")
save_button.place(relx = 0.15, rely = 0.05, anchor = CENTER)



root.mainloop()

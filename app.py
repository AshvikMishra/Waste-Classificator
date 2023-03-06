import classify
import base64

import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from PIL import Image, ImageOps

file_path = tk.filedialog.askopenfilename()

result = classify.analyse(file_path)

print(result)

from tkinter import *
from PIL import ImageTk, Image

win = Tk()

win.geometry("1920x1080")

frame = Frame(win, width=1280, height=720)
frame.pack()
frame.place(anchor='n', relx=0.5, rely=0.1)

img = Image.open(file_path)
resized_img= img.resize((1280,720), Image.ANTIALIAS)
new_img= ImageTk.PhotoImage(img)

label = Label(frame, image = new_img, borderwidth = 0)
label.pack()

T = Text(win, height = 10, width = 1280)
l = Label(win, text = result)
l.config(font = ("Helvetica", 20), wraplength = 1280, justify = "center", foreground = "white", background = "midnightblue")
final = result
l.pack()
T.insert(tk.END, final)

win.attributes('-topmost',True)
win.state('zoomed')
win.configure(bg = 'midnightblue')

win.mainloop()
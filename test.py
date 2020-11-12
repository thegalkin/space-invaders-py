
from tkinter import *
from PIL import Image, ImageTk


root = Tk()
width = 500
height = 500

canvas = Canvas(width=width, height=height)
canvas.pack()

img = ImageTk.PhotoImage(Image.open("oleg.png"))
img = ImageTk.PhotoImage(img)
canvas.create_image(img.size[0],img.size[1], image=img)




canvas.mainloop()
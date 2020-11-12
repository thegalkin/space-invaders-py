
from tkinter import *



root = Tk()
width = 500
height = 500

canvas = Canvas(width=width, height=height)
canvas.pack()


print(PhotoImage(file="coleg.png").width())
olegPhoto = PhotoImage(file="coleg.png")

olegImage = canvas.create_image(0,0, anchor='nw', image=olegPhoto)

for i in range(100):
    canvas.move(olegImage, 1, 1)




canvas.mainloop()
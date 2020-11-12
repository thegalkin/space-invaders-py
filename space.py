# huy
from tkinter import *
root = Tk()


mgl = 100
mgt = 50

li = []

c = Canvas(width = 500, height = 500)
c.pack()


for i in range(3):
    for j in range(5):
        li.append(c.create_rectangle(mgl + 10 + 60*j, mgt + 10 + 50*i, mgl + 10 + 60*j + 40, mgt + 50 + 50*i))


f = 1


def m():
    global f
    for i in li:
        c.move(i, 1*f, 0)
    f += 1
    root.after(100, m)


m()



c.mainloop()


# In[ ]:





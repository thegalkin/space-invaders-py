# huy
from tkinter import *
root = Tk()


marginLeft = 100
marginRight = 50
marginTop = 100

targets = []
targetsCoords = []
targetsVector = "Right" #направление движения целей

canvas = Canvas(width = 500, height = 500)
canvas.pack()


#Параметры спавна целей
numberOfLines = 6
numberOfItemsInLine = 19
basicSize = 5
xTargetsDistance = basicSize
#


"""f = 1


def moveTargets():
    global f
    for i in targets:
        canvas.move(i, 1*f, 0)
    f += 1
    root.after(100, moveTargets)"""


#moveTargets()


def createTargets():
    for line in range(3):
        for item in range(5):
            currentTarget = [marginLeft + 10 + xObjectDistance*item, marginRight + 10 + 50*line, marginLeft + 10 + xObjectDistance*item + 40, marginRight + 50 + 50*line]
            currentTarget = [marginLeft + basicSize + xTargetsDistance*item, marginTop + ]
            targets.append(canvas.create_rectangle(currentTarget))
            targetsCoords.append(currentTarget)



def moveTarget(obj, coords):
    return



createTargets()









canvas.mainloop()


# In[ ]:





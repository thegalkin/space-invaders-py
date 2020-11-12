# huy
from tkinter import *
root = Tk()
width = 500
height = 500

targetStopPadding = 10

marginLeft = 10
marginRight = 50
marginTop = 100

targetsObjects = []
targetsCoords = []
targetsVector = "Right" #направление движения целей

canvas = Canvas(width = width, height = height)
canvas.pack()


#Параметры спавна целей
numberOfLines = 6
numberOfItemsInLine = 19
basicSize = 5
xTargetsDistance = 60
speed = 2
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
    for line in range(numberOfLines):
        for item in range(numberOfItemsInLine):
            currentTarget = [marginLeft  + xTargetsDistance*item,       marginRight + 10 + basicSize*2*line,
                                                                                                            
                                                                                                            marginLeft+ xTargetsDistance*item + basicSize,       marginRight + 10 + basicSize + basicSize*2*line]
            #currentTarget = [marginLeft + basicSize + xTargetsDistance*item, marginTop + ]
            targetsObjects.append(canvas.create_rectangle(currentTarget))
            targetsCoords.append(currentTarget)
            
            



def moveTargets():
    global targetsVector
    if targetsVector == "Right":
        for object in targetsObjects:
            canvas.move(object, speed, 0)
    else:
        for object in targetsObjects:
            canvas.move(object, speed, 0)


    #трекаем столкновение стака целей с границами для изменения вектора
    if targetsCoords[len(targetsCoords)-1][2] > width - targetStopPadding:
        targetsVector = "Left"
    if targetsCoords[0][0] > 0 + targetStopPadding:
        targetsVector = "Right"
    root.after(100, moveTargets)




createTargets()

moveTargets()








canvas.mainloop()


# In[ ]:





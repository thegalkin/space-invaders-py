# huy
from tkinter import *
root = Tk()
width = 500
height = 500



targetsObjects = []
targetsCoords = []
targetsVector = "Right" #направление движения целей

canvas = Canvas(width = width, height = height)
canvas.pack()


#Параметры спавна целей

basicSize = 10

numberOfLines = 6
numberOfItemsInLine = 19

targetsMargin = basicSize
speedX = 2
speedY = 1
targetStopPadding = 10
marginLeft = 100
marginTop = 50
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
            currentTarget = [(basicSize + targetsMargin)*item,       (basicSize + targetsMargin)*line+marginTop,
                                                                                                            
                                                                                    (basicSize + targetsMargin)*item + basicSize,       (basicSize + targetsMargin)*line + basicSize+marginTop]
            #currentTarget = [marginLeft + basicSize + xTargetsDistance*item, marginTop + ]
            targetsObjects.append(canvas.create_rectangle(currentTarget))
            targetsCoords.append(currentTarget)
            
            



def moveTargets():
    global targetsVector
    if targetsVector == "Right":
        for object in targetsObjects:
            canvas.move(object, speedX, 0)
    else:
        for object in targetsObjects:
            canvas.move(object, speedX, 0)


    #трекаем столкновение стака целей с границами для изменения вектора
    if targetsCoords[len(targetsCoords)-1][2] > width - targetStopPadding:
        targetsVector = "Left"
        for object in targetsObjects:
            canvas.move(object, 0, speedY)
    if targetsCoords[0][0] > 0 + targetStopPadding:
        targetsVector = "Right"
        for object in targetsObjects:
            canvas.move(object, 0, speedY)
    root.after(100, moveTargets)




createTargets()

moveTargets()








canvas.mainloop()


# In[ ]:





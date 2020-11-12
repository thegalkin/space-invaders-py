# huy
from tkinter import *
root = Tk()
width = 500
height = 500

# Дима переменные

ml = 100
mt = 50
numberOfItemsInLine = 15
numberOFLines = 5
cellSize = 16
mg = 10
li = []



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
speedX = 0.5
speedY = 1.5
targetStopPadding = 10
marginLeft = 100
marginTop = 50
#



# Игрок
cellToStick = canvas.coords(len(targetsObjects)//2)
playerSize = 30
player = canvas.create_rectangle(cellToStick[0], 300, cellToStick[0]+playerSize, 320)

# Бинды


def arrowLeft(event):
    canvas.move(player, -(cellSize + mg), 0)


def arrowRight(event):
    canvas.move(player, cellSize + mg, 0)


ballList = []
ballI = 0


def spacebar(event):
    global ball
    global ballList
    global ballI
    playerCoords = canvas.coords(player)
    playerCenter = (canvas.coords(player)[2] - canvas.coords(player)[0]) / 2
    playerLeft = canvas.coords(player)[0]
    playerTop = canvas.coords(player)[1]
    ballList.append(
        canvas.create_oval(playerLeft + playerCenter - 5, playerTop - 15, playerLeft + playerCenter + 5, playerTop - 5))
    ballI += 1
    shoot(ballI)


def shoot(ballI):
    global afterFunc
    global ballList
    print(ballList)
    print(ballI)
    if canvas.coords(ballList[ballI])[1] <= 0:
        return None
    else:
        canvas.move(ballList[ballI], 0, -3)
        afterFunc = root.after(10, shoot, ballI)


root.bind("<Left>", arrowLeft)
root.bind("<Right>", arrowRight)
root.bind("<space>", spacebar)



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
        
        for i, object in enumerate(targetsObjects):
            canvas.move(object, speedX, 0)
            targetsCoords[i] = canvas.coords(object)
    if targetsVector == "Left":
        for i, object in enumerate(targetsObjects):
            canvas.move(object, -speedX, 0)
            targetsCoords[i] = canvas.coords(object)


    #трекаем столкновение стака целей с границами для изменения вектора
    if targetsCoords[len(targetsCoords)-1][2] > width-2:
        targetsVector = "Left"
        for i, object in enumerate(targetsObjects):
            canvas.move(object, 0, speedY)
            targetsCoords[i] = canvas.coords(object)
        print("Vector changed to Left")
    if targetsCoords[0][0] < 2 :
        targetsVector = "Right"
        for i, object in enumerate(targetsObjects):
            canvas.move(object, 0, speedY)
            targetsCoords[i] = canvas.coords(object)
        print("Vector changed to Right")
    root.after(10, moveTargets)




createTargets()

moveTargets()








canvas.mainloop()


# In[ ]:





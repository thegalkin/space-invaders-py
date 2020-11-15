from random import randint
from tkinter import *

root = Tk()
width = 500
height = 500

ballList = []
ballI = -1

targetsObjects = []
targetsCoords = []
targetsVector = "Right"  # направление движения целей

canvas = Canvas(width=width, height=height)
canvas.pack()

# Параметры спавна целей

basicSize = 10

numberOfLines = 6
numberOfItemsInLine = 19

targetsMargin = basicSize
speedX = 0.5
speedY = 1.5
targetStopPadding = 10
marginLeft = 100
marginTop = 50


def randomColor():
    return "#%06x" % randint(0, 0xFFFFFF)


class Space:

    def __init__(self):
        self.player = None

    # Создание целей + движение

    def createTargets(self):
        for line in range(numberOfLines):
            for item in range(numberOfItemsInLine):
                currentTarget = [(basicSize + targetsMargin) * item, (basicSize + targetsMargin) * line + marginTop,

                                 (basicSize + targetsMargin) * item + basicSize,
                                 (basicSize + targetsMargin) * line + basicSize + marginTop]
                targetsObjects.append(canvas.create_rectangle(currentTarget, fill=randomColor(), tags="cell"))
                targetsCoords.append(currentTarget)

        # Игрок
        cellToStick = canvas.coords(len(targetsObjects) // 2)
        playerSize = 30
        self.player = canvas.create_rectangle(cellToStick[0], 300, cellToStick[0] + playerSize, 320)

    def moveTargets(self):
        global targetsVector
        if targetsVector == "Right":

            for i, object in enumerate(targetsObjects):
                canvas.move(object, speedX, 0)
                targetsCoords[i] = canvas.coords(object)
        if targetsVector == "Left":
            for i, object in enumerate(targetsObjects):
                canvas.move(object, -speedX, 0)
                targetsCoords[i] = canvas.coords(object)

        # трекаем столкновение стака целей с границами для изменения вектора
        if targetsCoords[len(targetsCoords) - 1][2] > width - 2:
            targetsVector = "Left"
            for i, object in enumerate(targetsObjects):
                canvas.move(object, 0, speedY)
                targetsCoords[i] = canvas.coords(object)
        #             print("Vector changed to Left")
        if targetsCoords[0][0] < 2:
            targetsVector = "Right"
            for i, object in enumerate(targetsObjects):
                canvas.move(object, 0, speedY)
                targetsCoords[i] = canvas.coords(object)
        #             print("Vector changed to Right")
        root.after(10, self.moveTargets)

    def endGame(self, win):
        if not win:
            return
        else:
            return


    # Бинды + выстрел

    def spacebar(self, event):
        global ball
        global ballList
        global ballI
        playerCoords = canvas.coords(self.player)
        playerCenter = (canvas.coords(self.player)[2] - canvas.coords(self.player)[0]) / 2
        playerLeft = canvas.coords(self.player)[0]
        playerTop = canvas.coords(self.player)[1]
        ball = canvas.create_rectangle(playerLeft + playerCenter - 5, playerTop - 15, playerLeft + playerCenter + 5,
                                       playerTop - 5)
        ballList.append(ball)
        ballI += 1
        self.shoot(ballI)

    def shoot(self, ballI):
        global afterFunc
        global ballList

        endsOfLines = [numberOfItemsInLine * i for i in range(1, numberOfLines + 1)][::-1]

        for i in endsOfLines:
            if canvas.coords(ballList[ballI])[1] <= canvas.coords(targetsObjects[i - 1])[3]:
                tempCoords = canvas.coords(ballList[ballI])
                tempTarget = canvas.find_overlapping(tempCoords[0],
                                                     tempCoords[1],
                                                     tempCoords[2],
                                                     tempCoords[3])
                if canvas.itemcget(tempTarget[0], "outline") == "black" and canvas.itemcget(tempTarget[0],
                                                                                            "tags") == "cell":
                    canvas.itemconfig(tempTarget[0], fill="white", outline="")
                    canvas.delete(ballList[ballI])
                    if len(ballList) == 0:
                        self.endGame(True)
                    return None

        if canvas.coords(ballList[ballI])[1] <= 0:
            canvas.delete(ballList[ballI])
            return None
        else:
            canvas.move(ballList[ballI], 0, -3)
            afterFunc = root.after(10, self.shoot, ballI)

    def arrowLeft(self, event):
        canvas.move(self.player, -(basicSize + targetsMargin), 0)

    def arrowRight(self, event):
        canvas.move(self.player, basicSize + targetsMargin, 0)


s = Space()

root.bind("<Left>", s.arrowLeft)
root.bind("<Right>", s.arrowRight)
root.bind("<KeyRelease-space>", s.spacebar)
root.bind("a", s.arrowLeft)
root.bind("d", s.arrowRight)

s.createTargets()

s.moveTargets()


canvas.mainloop()
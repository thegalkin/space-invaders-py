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

gameFinished = False

deletedTargets = 0


def randomColor():
    return "#%06x" % randint(0, 0xFFFFFF)


class Space:

    def __init__(self):
        self.player = None
        root.bind("<Left>", self.arrowLeft)
        root.bind("<Right>", self.arrowRight)
        root.bind("<KeyPress-space>", self.spacebar)
        root.bind("<KeyRelease-s>", self.arrowRight)
        root.bind("<KeyRelease-a>", self.arrowLeft)


    #Удаление повторений в таблице координат целей - вспомогательная функция
    def deleteTwices(l):
        n = []
        for i in l:
            if i not in n:
                n.append(i)
        return n


    # Рисование целей из своей карты
    def drawMapFromFile(self, mapName):
        global gameFinished
        global targetsCoords
        global targetsObjects
        tempObjects = []  
        targetsCoords = []                                                  #Чистим таблицу целей и их объектов
        for item in targetsObjects:                                         
            canvas.delete(item)
        
        with open("{}.map".format(mapName), 'r') as mapFile:
            for target in mapFile:
                tempLine = list(target.split(","))                          #Читаем файл карты и вычленяем данные
                for i in range(len(tempLine)):
                    tempLine[i] = int(tempLine[i])                          #Создаем по данным объекты и их записи
                    targetsObjects.append(canvas.create_rectangle(
                        tempLine, fill="#eae100", tags="cell", outline=""))
                    targetsCoords.append(target)


    #Создание целей
    def createTargets(self):
        for line in range(numberOfLines):
            for item in range(numberOfItemsInLine):
                currentTarget = [(basicSize + targetsMargin) * item, (basicSize + targetsMargin) * line + marginTop,

                                 (basicSize + targetsMargin) * item + basicSize,
                                 (basicSize + targetsMargin) * line + basicSize + marginTop]
                targetsObjects.append(canvas.create_rectangle(
                    currentTarget, fill=randomColor(), tags="cell"))
                targetsCoords.append(currentTarget)

        # Игрок
        cellToStick = canvas.coords(len(targetsObjects) // 2)
        playerSize = 30
        self.player = canvas.create_rectangle(
            cellToStick[0], 300, cellToStick[0] + playerSize, 320, fill="gray")
    

    #Движение целей
    def moveTargets(self):
        global gameFinished
        global targetsVector
        if gameFinished:
            return
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

        if targetsCoords[0][0] < 2:
            targetsVector = "Right"
            for i, object in enumerate(targetsObjects):
                canvas.move(object, 0, speedY)
                targetsCoords[i] = canvas.coords(object)


        # проверяем проигрыш
        if deletedTargets != len(targetsObjects) and targetsCoords[len(targetsCoords)-1][3] >= canvas.coords(self.player)[1]:
            self.endGame(False)                                         #Если цели достигли игрока и он не убил их - проигрыш
        if not gameFinished:                                            #Если не проиграли - продолжаем движение целей
            root.after(10, self.moveTargets)
    

    #Старт конца игры
    def endGame(self, win):                                             #Просто развилка концовки
        global gameFinished
        gameFinished = True
        if not win:
            self.drawMapFromFile("youLoose")

        else:
            self.drawMapFromFile("youWin")


    # Бинды + выстрел
    def spacebar(self, event):
        global ball
        global ballList
        global ballI
        global gameFinished
        if gameFinished:
            return
        playerCoords = canvas.coords(self.player)
        playerCenter = (canvas.coords(self.player)[
                        2] - canvas.coords(self.player)[0]) / 2
        playerLeft = canvas.coords(self.player)[0]
        playerTop = canvas.coords(self.player)[1]
        ball = canvas.create_rectangle(playerLeft + playerCenter - 5, playerTop - 15, playerLeft + playerCenter + 5,
                                       playerTop - 5, fill="#e6a200", outline="")
        ballList.append(ball)
        ballI += 1
        self.shoot(ballI)


    # Стрельба
    def shoot(self, ballI):
        global afterFunc
        global ballList
        global deletedTargets
        global gameFinished
        if gameFinished:
            return
        endsOfLines = [numberOfItemsInLine *
                       i for i in range(1, numberOfLines + 1)][::-1]
        
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

                    deletedTargets += 1
                    canvas.delete(ballList[ballI])

                    if deletedTargets == len(targetsObjects):                   #Проверка на выигрыш - если уничтожены все цели
                        self.endGame(True)
                    return None

        if canvas.coords(ballList[ballI])[1] <= 0:
            canvas.delete(ballList[ballI])
            return None
        else:
            canvas.move(ballList[ballI], 0, -3)
            afterFunc = root.after(10, self.shoot, ballI)


    #Движение игрока влево
    def arrowLeft(self, event):
        if canvas.coords(self.player)[0] > 20:
            canvas.move(self.player, -(basicSize + targetsMargin), 0)


    # Движение игрока вправо
    def arrowRight(self, event):
        if canvas.coords(self.player)[2] <= width-20:
            canvas.move(self.player, basicSize + targetsMargin, 0)


s = Space()





s.createTargets()

s.moveTargets()


canvas.mainloop()

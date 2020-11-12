from tkinter import *
from PIL import Image, ImageTk


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
nastyPhotos = []

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
                nastyPhoto = PhotoImage(file="nasty.png")

                currentPhoto = canvas.create_image((basicSize + targetsMargin) * item, (basicSize + targetsMargin) * line + marginTop, image=nastyPhoto)
                nastyPhoto.image = nastyPhoto
                nastyPhotos.append(nastyPhoto.image)
                targetsObjects.append(currentPhoto)
                targetsCoords.append(currentTarget)
                

        # Игрок
        cellToStick = canvas.coords(len(targetsObjects) // 2)
        # print(targetsObjects)
        playerSize = 30
        self.player = canvas.create_rectangle(cellToStick[0], 300, cellToStick[0] + playerSize, 320)

    def moveTargets(self):
        global targetsVector
        if targetsVector == "Right":

            for i, object in enumerate(targetsObjects):
                canvas.move(object, speedX, 0)
                targetsCoords[i] = [canvas.coords(object)[0], canvas.coords(object)[1], canvas.coords(object)[0]+basicSize, canvas.coords(object)[1]+ basicSize]
        if targetsVector == "Left":
            for i, object in enumerate(targetsObjects):
                canvas.move(object, -speedX, 0)
                targetsCoords[i] = [canvas.coords(object)[0], canvas.coords(object)[1], canvas.coords(object)[0]+basicSize, canvas.coords(object)[1]+ basicSize]

        # трекаем столкновение стака целей с границами для изменения вектора
        if targetsCoords[len(targetsCoords) - 1][0] > width - 2:
            targetsVector = "Left"
            for i, object in enumerate(targetsObjects):
                canvas.move(object, 0, speedY)
                targetsCoords[i] = [canvas.coords(object)[0], canvas.coords(object)[1], canvas.coords(object)[0]+basicSize, canvas.coords(object)[1]+ basicSize]
            #print("Vector changed to Left")
        if targetsCoords[0][0] < 2:
            targetsVector = "Right"
            for i, object in enumerate(targetsObjects):
                canvas.move(object, 0, speedY)
                targetsCoords[i] = [canvas.coords(object)[0], canvas.coords(object)[1], canvas.coords(object)[0]+basicSize, canvas.coords(object)[1]+ basicSize]
            #print("Vector changed to Right")
        root.after(10, self.moveTargets)

    # Бинды + выстрел

    def spacebar(self, event):
        global ball
        global ballList
        global ballI
        playerCoords = canvas.coords(self.player)
        playerCenter = (canvas.coords(self.player)[2] - canvas.coords(self.player)[0]) / 2
        playerLeft = canvas.coords(self.player)[0]
        playerTop = canvas.coords(self.player)[1]
        olegPhoto = PhotoImage(file="coleg.png")

        ball = canvas.create_image(playerLeft + playerCenter - 5, playerTop - 15, image=olegPhoto)

        
        #ball = canvas.create_oval(playerLeft + playerCenter - 5, playerTop - 15, playerLeft + playerCenter + 5,
                                  #playerTop - 5)
        olegPhoto.image = olegPhoto
        ballList.append(ball)
        ballI += 1
        self.shoot(ballI)

    def shoot(self, ballI):
        global afterFunc
        global ballList
        
        for i, item in enumerate(targetsCoords):

            if len(canvas.find_overlapping(item[0], item[1], item[2], item[3])) > 4:
                
                print(len(canvas.find_overlapping(item[0], item[1], item[2], item[3])))
                canvas.move(ballList[ballI], -10000, -10000)
                canvas.move(targetsObjects[i], -1000, -100)
                canvas.move(targetsCoords[i], -1000, -1000)
                return None

        if canvas.coords(ballList[ballI])[1] <= 0:
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
root.bind("<space>", s.spacebar)
root.bind("a", s.arrowLeft)
root.bind("d", s.arrowRight)
root.bind("<space>", s.spacebar)


s.createTargets()

s.moveTargets()

canvas.mainloop()

# In[ ]:

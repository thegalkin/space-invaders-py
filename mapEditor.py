
from tkinter import *
from random import randint
from time import time

root = Tk()
width = 500
height = 500

canvas = Canvas(width=width, height=height)
canvas.pack()

basicSize = 20

numberOfLines = 6
numberOfItemsInLine = 19

targetsMargin = 0
speedX = 0.5
speedY = 1.5
targetStopPadding = 10
marginLeft = 100
marginTop = 50

targetsObjects = []
targetsCoords = []
layout = []
timePrev = time()


def deleteTwices(l):
    n = []
    for i in l:
        if i not in n:
            n.append(i)
    return n

def save(event):
    print("saving")
    fileName = input("Enter File Name: ")
    with open("{}.txt".format(fileName), "w+") as mapFile:
        for line in targetsCoords:
            strLine = ','.join(str(e) for e in line)
            strLine = "[" + strLine + "]"
            mapFile.write(strLine)

for item in range(50):
    for line in range(250):
        currentTarget = [(basicSize + targetsMargin) * item, (basicSize + targetsMargin) * line + marginTop,

                (basicSize + targetsMargin) * item + basicSize,
                (basicSize + targetsMargin) * line + basicSize + marginTop]
        
        layout.append(currentTarget)

def randomColor():
    return "#%06x" % randint(0, 0xFFFFFF)
def boxCreation(event):
    global targetsCoords
    global targetsObjects
    

    currentTarget = [event.x-basicSize, event.y-basicSize,event.x+basicSize, event.y+basicSize]

    for item in layout:

        if item[0] < event.x < item[2] and item[1] < event.y < item[3]:
            if not (item in targetsCoords):
                
                targetsObjects.append(canvas.create_rectangle(item, fill="#eae100", tags="cell", outline=""))
            targetsCoords.append(item)
            print(len(targetsCoords))
            targetsCoords = deleteTwices(targetsCoords)
            print(len(targetsCoords))
            #print(targetsCoords)    

def boxDeletion(event):
    global targetsCoords
    global targetsObjects
    currentTarget = [event.x-basicSize, event.y-basicSize,event.x+basicSize, event.y+basicSize]

    for item in layout :
        try:
            if item[0] < event.x < item[2] and item[1] < event.y < item[3] and item in targetsCoords:
                
                print("trying to delete")
                
                canvas.delete(targetsObjects[targetsCoords.index(item)])
                del targetsObjects[targetsCoords.index(item)]
                print(targetsObjects)
                del targetsCoords[targetsCoords.index(item)]
                
                
        except ValueError:
            
            print(targetsCoords)    
            return

canvas.bind('<Button-1>', boxCreation)
canvas.bind('<B1-Motion>', boxCreation)
canvas.bind('<Button-2>', boxDeletion)
canvas.bind('<B2-Motion>', boxDeletion)
root.bind('s', save)


canvas.mainloop()
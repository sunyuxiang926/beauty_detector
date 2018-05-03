#Animation code templete from 15112 course website
#https://www.cs.cmu.edu/~112/notes/notes-animations-part2.html#starter-code

import cv2
from tkinter import *
import numpy as np
from PIL import ImageTk, Image
from minorMode import *
from shootMode import *
from editMode import *
from featureEditMode import *
from chooseMode import *
from scoreMode import *
from analyzeMode import *

# Mode Demo

####################################
# init
####################################

def init(data):
    # There is only one init, not one-per-mode
    data.mode = "userInformation"
    data.name = ''
    data.img=None
    data.scoreImg=None
    data.faceCoor=[]
    data.noseCoor=[]
    data.mouthCoor=[]
    data.rEyes=[]
    data.lEyes=[]
    data.faceL=[]
    data.rEyeL=[]
    data.lEyeL=[]
    data.mouthL=[]
    data.noseL=[]
    data.faceImg=None
    data.ReyeImg=None
    data.LeyeImg=None
    data.mouthImg=None
    data.noseImg=None
    data.angel=None
    data.cat=None
    data.dog=None
    data.fox=None
    data.panda=None
    data.pikachu=None
    data.rabbit=None
    data.text=None
    data.text2=None
    data.text3=None
    data.text4=None
    data.scorer=None
    data.feature=None
    data.result=None
    data.low1=None
    data.low2=None
    data.high1=None
    data.high2=None
    data.high3=None
    data.high4=None
    data.high5=None
    data.text3=None
    data.background=None
    data.start=None
    data.enter=False
    data.drawEnter=False
    data.textEnter=''
    data.numEnter=0
    data.timer=0
    data.next=None
    data.camera=None
    data.analyze=None
    data.startA=None
    data.done=None
    data.doneA=False
    data.timerA=0
    data.finish=False
    data.back=None
    data.camera2=None
    data.screenshot=None
    data.forward=None
    data.frame=[None]*31
    getFrames(data)
    data.i=0
    data.timerS=0
    data.take=False
    data.save=None
    data.i2=0
    data.frame2=[None]*19
    getFrames2(data)

#minions image from https://www.google.com/search?tbm=isch&q=thank+you+gif&chips=q:thanks+you+gi
#f,g_5:transparent+background&sa=X&ved=0ahUKEwiU6YnVyeTaAhWrc98KHYG
#-CD8Q4lYILygA&biw=1200&bih=703&dpr=2#imgdii=K6InSIFjhMQITM:&imgrc=eXuVSuEtJAwoEM:
def getFrames(data):
    for i in range(31):
        data.frame[i]=PhotoImage(file='images/minions.gif', format="gif -index "+str(i))

#thank you image from https://www.google.com/search?q=thank+you+gif&tbs=rimg:CefuEH
#hY5GkyIjjx1-7-XSnXLccrCK91_1RZ6LIs8xAI90Fr3OwEvaUIbyFTTtAqfD8oo4A
#pDQ2l02ZEDvPFgSe4AcSoSCfHX7v5dKdctESynDAfMBod0KhIJxysIr3X9FnoREGY8Tt_1p4
#UEqEgksizzEAj3QWhHF24rtPaKTNyoSCfc7AS9pQhvIEV_1DsJBrBs14KhIJVNO0Cp8PyigR8KC
#-A7Gr9PMqEgngCkNDaXTZkRHgnin4ZU_1FwSoSCQO88WBJ7gBxEd4RNphJrnSh,isz:m&tbm=isch&source
#=lnt&sa=X&ved=0ahUKEwi5857yzuTaAhUtT98KHfF_CIwQpwUIHg&biw=1200&bih=666&dpr=2#imgdii=
#i1MupnkkjS5Q_M:&imgrc=Kg_uajrxSni17M:
def getFrames2(data):
    for i in range(19):
        data.frame2[i]=PhotoImage(file='images/thank.gif', format="gif -index "+str(i))

####################################
# mode dispatcher
####################################

def mousePressed(event, data):
    if (data.mode == "userInformation"): userInformationMousePressed(event, data)
    elif (data.mode == "start"): startMousePressed(event, data)
    elif (data.mode == "shoot"):   shootMousePressed(event, data)
    elif (data.mode == 'analyze'): analyzeMousePressed(event,data)
    elif (data.mode == "edit"):       editMousePressed(event, data)
    elif (data.mode == 'faceEdit'): faceEditMousePressed(event,data)
    elif (data.mode == 'ReyeEdit'): ReyeEditMousePressed(event,data)
    elif (data.mode == 'LeyeEdit'): LeyeEditMousePressed(event,data)
    elif (data.mode == 'mouthEdit'): mouthEditMousePressed(event,data)
    elif (data.mode == 'noseEdit'): noseEditMousePressed(event,data)
    elif (data.mode == 'choose'): chooseMousePressed(event,data)
    elif (data.mode == 'score'): scoreMousePressed(event,data)
    elif (data.mode == 'final'): finalMousePressed(event,data)

def keyPressed(event, data):
    if (data.mode == "userInformation"): userInformationKeyPressed(event, data)
    elif (data.mode == "start"): startKeyPressed(event, data)
    elif (data.mode == "shoot"):   shootKeyPressed(event, data)
    elif (data.mode == 'analyze'): analyzeKeyPressed(event,data)
    elif (data.mode == "edit"):       editKeyPressed(event, data)
    elif (data.mode == 'faceEdit'): faceEditKeyPressed(event,data)
    elif (data.mode == 'ReyeEdit'): ReyeEditKeyPressed(event,data)
    elif (data.mode == 'LeyeEdit'): LeyeEditKeyPressed(event,data)
    elif (data.mode == 'mouthEdit'): mouthEditKeyPressed(event,data)
    elif (data.mode == 'noseEdit'): noseEditKeyPressed(event,data)
    elif (data.mode == 'choose'): chooseKeyPressed(event,data)
    elif (data.mode == 'score'): scoreKeyPressed(event,data)
    elif (data.mode == 'final'): finalKeyPressed(event,data)


def redrawAll(canvas, data):
    if (data.mode == "userInformation"): userInformationRedrawAll(canvas,data)
    elif (data.mode == "start"): startRedrawAll(canvas, data)
    elif (data.mode == "shoot"):   shootRedrawAll(canvas, data)
    elif (data.mode == 'analyze'): analyzeRedrawAll(canvas,data)
    elif (data.mode == "edit"):       editRedrawAll(canvas, data)
    elif (data.mode == 'faceEdit'): faceEditRedrawAll(canvas, data)
    elif (data.mode == 'ReyeEdit'): ReyeEditRedrawAll(canvas, data)
    elif (data.mode == 'LeyeEdit'): LeyeEditRedrawAll(canvas, data)
    elif (data.mode == 'mouthEdit'): mouthEditRedrawAll(canvas, data)
    elif (data.mode == 'noseEdit'): noseEditRedrawAll(canvas, data)
    elif (data.mode == 'choose'): chooseRedrawAll(canvas, data)
    elif (data.mode == 'score'): scoreRedrawAll(canvas,data)
    elif (data.mode == 'final'): finalRedrawAll(canvas,data)

def timerFired(data):
    if (data.mode=='userInformation'): userInformationTimerFired(data)
    elif (data.mode == 'analyze'): analyzeTimerFired(data)
    elif (data.mode == 'score'): scoreTimerFired(data)
    elif (data.mode == 'final'): finalTimerFired(data)
    else: pass

####################################
# use the run function as-is
####################################
def run(width=600, height=600):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds
    root = Tk()
    root.geometry('600x600+0+0')
    root.title('Beauty Detector')
    init(data)
    # create the root and the canvas
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(600,600)
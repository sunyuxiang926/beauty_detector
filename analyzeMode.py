import cv2
from tkinter import *
import numpy as np
from PIL import Image, ImageTk
import string

####################################
# analyze mode
####################################
def detectFace(path):
    faceL=[]
    rEyeL=[]
    lEyeL=[]
    mouthL=[]
    noseL=[]
    
    img = cv2.imread(path)
    
    face = cv2.CascadeClassifier('haarcascades/model1/face.xml')
    Reye = cv2.CascadeClassifier('haarcascades/model1/Reye.xml') 
    Leye = cv2.CascadeClassifier('haarcascades/model1/Leye.xml') 
    mouth = cv2.CascadeClassifier('haarcascades/model1/mouth.xml') 
    nose = cv2.CascadeClassifier('haarcascades/model1/nose.xml') 
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    faceC = face.detectMultiScale(gray, 1.3, 5)
    
    for (x,y,w,h) in faceC:
        faceL.append((x,y,w,h))

        roiGray = gray[y:y+h, x:x+w]
        roiImg = img[y:y+h, x:x+w] #eyes, nose, and mouth always on face, bounding box useful

        ReyeC = Reye.detectMultiScale(roiGray)
        LeyeC = Leye.detectMultiScale(roiGray)
        mouthC = mouth.detectMultiScale(roiGray)
        noseC = nose.detectMultiScale(roiGray)
        
        for (x,y,w,h) in ReyeC:
                rEyeL.append((x,y,w,h))
        
        for (x,y,w,h) in LeyeC:
                lEyeL.append((x,y,w,h))
        
        for (x,y,w,h) in mouthC:
                mouthL.append((x,y,w,h))
        
        for (x,y,w,h) in noseC:
                noseL.append((x,y,w,h))

    return (faceL,rEyeL,lEyeL,mouthL,noseL)
    cv2.waitKey(0)

def getFeature(data):
    path='images/'+data.name+'.png'
    feature=detectFace('images/'+data.name+'.png')
    
    data.faceL=feature[0]
    data.rEyeL=feature[1]
    data.lEyeL=feature[2]
    data.mouthL=feature[3]
    data.noseL=feature[4]
    
    data.faceCoor=[None]*len(data.faceL)
    for i in range(len(data.faceL)):
        data.faceCoor[i]=list(data.faceL[i])
    
    data.rEyes=[None]*len(data.rEyeL)
    for i in range(len(data.rEyeL)):
        data.rEyes[i]=list(data.rEyeL[i])

    data.lEyes=[None]*len(data.lEyeL)
    for i in range(len(data.lEyeL)):
        data.lEyes[i]=list(data.lEyeL[i])
    
    data.mouthCoor=[None]*len(data.mouthL)
    for i in range(len(data.mouthL)):
        data.mouthCoor[i]=list(data.mouthL[i])
    
    data.noseCoor=[None]*len(data.noseL)
    for i in range(len(data.noseL)):
        data.noseCoor[i]=list(data.noseL[i])

def analyzeMousePressed(event,data):
    if 0<=event.x<=100 and 400<=event.y<=500:
        data.doneA=True
        getFeature(data)
    if data.finish==True and 500<=event.x<=600 and 550<=event.y<=600:
        data.mode='edit'

def analyzeTimerFired(data):
    if data.doneA==True:
        data.timerA+=1
    if data.timerA==5:
        data.finish=True
        data.doneA=False

def analyzeKeyPressed(event,data):
    pass

def analyzeRedrawAll(canvas,data):
    #image from https://www.google.com/search?q=analyze&source=lnm
    #s&tbm=isch&sa=X&ved=0ahUKEwjzs-6H3eLaAhVmUN8KHQ7HCykQ_AUICigB&
    #biw=1200&bih=664#imgrc=YYtsxUsczbGK4M:
    analyze=Image.open('images/analyze.jpg')
    resizeAnalyze=analyze.resize((600,400),Image.ANTIALIAS)
    data.analyze=ImageTk.PhotoImage(resizeAnalyze)
    
    #image from https://www.google.com/search?biw=1200&bih=662&tbm=isch&sa=1
    #&ei=jm7nWseOBsPk_Aa_pYToBA&q=done&oq=done&gs_l=psy-ab.3..0i
    #67k1j0l2j0i67k1l2j0l5.3774.5827.0.6126.5.5.0.0.0.0.59.264.5.5.0.
    #...0...1c.1.64.psy-ab..0.5.263...0i24k1j0i5i30k1.0.ZepBEQHyJb4#imgrc=wgi70QYWvvnANM:
    done=Image.open('images/done.jpg')
    resizeDone=done.resize((300,210),Image.ANTIALIAS)
    data.done=ImageTk.PhotoImage(resizeDone)
    
    #image from https://www.google.com/search?biw=1200&bih=664&tbm=isch&sa=1&ei=im3nW
    #qeJDoqf_QaCkawo&q=start+pink&oq=start+pink&gs_l=psy-ab.3..0i8i
    #30k1l8.2709.3708.0.3932.5.5.0.0.0.0.59.275.5.5.0....0...1c.1.64.psy
    #-ab..0.5.275...0j0i67k1j0i5i30k1.0.YrEVElVG0Sg#imgrc=6wIODKti4KCvzM:
    startA=Image.open('images/startA.png')
    resizeStartA=startA.resize((100,100),Image.ANTIALIAS)
    data.startA=ImageTk.PhotoImage(resizeStartA)
    
    canvas.create_image(0,0,image=data.analyze,anchor=NW)
    canvas.create_text(data.width/2,460,text="Press the start button to analyze your photo",font="Arial 20")
    canvas.create_text(data.width/2,480,text="It will take about 5 seconds",font="Arial 20")
    canvas.create_text(data.width/2,500,text="Once done, there'll be a 'Done' tag",font="Arial 20")
    canvas.create_text(data.width/2,520,text="When you see the tag, feel free to move on by click 'Next'",font="Arial 20")
    canvas.create_image(500,550,image=data.next,anchor=NW)

    if data.finish==False:
        canvas.create_image(0,400,image=data.startA,anchor=NW)
    else:
        canvas.create_image(0,180,image=data.done,anchor=NW)
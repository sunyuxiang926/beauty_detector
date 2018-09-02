import cv2
from tkinter import *
import numpy as np
from PIL import Image, ImageTk
from sklearn import decomposition
from sklearn import linear_model
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.metrics import mean_absolute_error
import random
import pyscreenshot

import pickle

def scoreMousePressed(event,data):
    if 5<=event.x<=55 and 495<=event.y<=545:
        data.mode='choose'
    elif 5<=event.x<=55 and 445<=event.y<=495:
        data.take=True
    elif 5<=event.x<=55 and 545<=event.y<=595:
        data.mode='final'

def takeScreenShot(data):
    img=pyscreenshot.grab(bbox=(0,45,600,645))
    img.save('images/'+data.name+data.scorer+'Screenshot'+'.png')
    img=Image.open('images/'+data.name+data.scorer+'Screenshot'+'.png')
    resizeImg=img.resize((400,400),Image.ANTIALIAS)
    data.screenshot=ImageTk.PhotoImage(resizeImg)

def scoreKeyPressed(event,data):
    pass

def scoreTimerFired(data):
    if data.take==True:
        data.timerS+=1
        if data.timerS%3==True:
            takeScreenShot(data)
        if data.timerS%8==0:
            data.timerS=0
            data.take=False

def distance(p1,p2):
    return ((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)**0.5

def faceFeature(data):
    A=(data.faceCoor[0][0],data.faceCoor[0][1])
    B=(data.faceCoor[0][0],data.faceCoor[0][1]+data.faceCoor[0][3])
    C=(data.faceCoor[0][0]+data.faceCoor[0][2],data.faceCoor[0][1]+data.faceCoor[0][3])
    D=(data.faceCoor[0][0]+data.faceCoor[0][2],data.faceCoor[0][1])
    
    width=distance(A,D)
    height=distance(A,B)
    lDiag=distance(A,C)
    rDiag=distance(B,D)
    
    Leye=(data.lEyes[0][0]+data.lEyes[0][2]/2,data.lEyes[0][1]+data.lEyes[0][3]/2)
    Reye=(data.rEyes[0][0]+data.rEyes[0][2]/2,data.rEyes[0][1]+data.rEyes[0][3]/2)
    nose=(data.noseCoor[0][0]+data.noseCoor[0][2]/2,data.noseCoor[0][1]+data.noseCoor[0][3]/2)
    mouth=(data.mouthCoor[0][0]+data.mouthCoor[0][2]/2,data.mouthCoor[0][1]+data.mouthCoor[0][3]/2)
    
    E=(Leye[0],A[1])
    F=(Reye[0],A[1])
    G=(A[0],Leye[1])
    H=(D[0],Reye[1])
    I=(Leye[0]+distance(Leye,Reye)/2,G[1])
    J=(data.mouthCoor[0][0]-data.mouthCoor[0][2]/2,mouth[1])
    K=(data.mouthCoor[0][0]+data.mouthCoor[0][2]/2,mouth[1])
    L=(A[0],mouth[1])
    M=(D[0],mouth[1])
    N=(mouth[0],B[1])
    O=(A[0]+distance(A,D)/2,A[1])
    
    data.feature=[distance(A,Leye)/lDiag*100,
             distance(D,Reye)/rDiag*100,
             distance(Leye,Reye)/width*100,
             distance(E,Leye)/height*100,
             distance(F,Reye)/height*100,
             distance(G,Leye)/width*100,
             distance(H,Reye)/width*100,
             distance(I,nose)/height*100,
             distance(Leye,nose)/lDiag*100,
             distance(Reye,nose)/rDiag*100,
             distance(nose,mouth)/height*100,
             distance(J,nose)/rDiag*100,
             distance(K,nose)/lDiag*100,
             distance(L,J)/width*100,
             distance(M,K)/width*100,
             distance(N,mouth)/height*100,
             distance(O,I)/height*100]
    
    data.feature=[data.feature]

def score(data):
    faceFeature(data)
    
    if data.scorer=='cat':
        model=pickle.load(open('result/adtModel.sav', 'rb'))
    elif data.scorer=='fox':
        model=pickle.load(open('result/dtModel.sav', 'rb'))
    elif data.scorer=='rabbit':
        model=pickle.load(open('result/lrModel.sav', 'rb'))
    elif data.scorer=='pikachu':
        model=pickle.load(open('result/lsvm1Model.sav', 'rb'))
    elif data.scorer=='dog':
        model=pickle.load(open('result/rbfsvmModel.sav', 'rb'))
    elif data.scorer=='panda':
        model=pickle.load(open('result/rfModel.sav', 'rb'))
    
    data.result=model.predict(data.feature)
    data.result=data.result.tolist()
    data.result=abs(getScore(data.result))
    
    if data.result>5:
        data.result=5-(data.result-5)/10

def getScore(l):
    if isinstance(l,float):
        return l
    elif isinstance(l,list):
        return getScore(l[0])

def scoreRedrawAll(canvas,data):
    score(data)
    
    #image from https://www.google.com/search?biw=1200&bih=666&tbm=isch&sa=1&ei=t
    #I_nWsd376GCB7mvr-AN&q=back+arrow+pink&oq=back+arrow+pink&gs_l=psy
    #-ab.3...24947.26760.0.27189.7.7.0.0.0.0.116.434.6j1.7.0....0...1c.1.64.psy
    #ab..1.4.282...0j0i7i10i30k1j0i7i30k1j0i7i5i30k1j0i5i30k1j0i8i7i30k1j0i8i7i1
    #0i30k1j0i8i13i30k1.0.PkuVskcptZE#imgrc=r-6MpaPPHiCfpM:
    back=Image.open('images/back.png')
    resizeBack=back.resize((50,50),Image.ANTIALIAS)
    data.back=ImageTk.PhotoImage(resizeBack)
    
    forward=Image.open('images/forward.png')
    resizeForward=forward.resize((50,50),Image.ANTIALIAS)
    data.forward=ImageTk.PhotoImage(resizeForward)
    
    img=Image.open('images/'+data.name+'.png')
    resizeImg=img.resize((580,435),Image.ANTIALIAS)
    data.scoreImg=ImageTk.PhotoImage(resizeImg)
    
    high1=Image.open('images/high1.png')
    resizeHigh1=high1.resize((200,50),Image.ANTIALIAS)
    data.high1=ImageTk.PhotoImage(resizeHigh1)
    
    high2=Image.open('images/high2.png')
    resizeHigh2=high2.resize((250,52),Image.ANTIALIAS)
    data.high2=ImageTk.PhotoImage(resizeHigh2)
    
    high3=Image.open('images/high3.png')
    resizeHigh3=high3.resize((300,85),Image.ANTIALIAS)
    data.high3=ImageTk.PhotoImage(resizeHigh3)
    
    high4=Image.open('images/high4.png')
    resizeHigh4=high4.resize((300,85),Image.ANTIALIAS)
    data.high4=ImageTk.PhotoImage(resizeHigh4)
    
    high5=Image.open('images/high5.png')
    resizeHigh5=high5.resize((250,52),Image.ANTIALIAS)
    data.high5=ImageTk.PhotoImage(resizeHigh5)
    
    low1=Image.open('images/low1.png')
    resizeLow1=low1.resize((200,54),Image.ANTIALIAS)
    data.low1=ImageTk.PhotoImage(resizeLow1)
    
    low2=Image.open('images/low2.png')
    resizeLow2=low2.resize((200,52),Image.ANTIALIAS)
    data.low2=ImageTk.PhotoImage(resizeLow2)
    
    save=Image.open('images/save.png')
    resizeSave=save.resize((200,44),Image.ANTIALIAS)
    data.save=ImageTk.PhotoImage(resizeSave)

    if data.scorer=='cat':
        canvas.create_image(410,460,image=data.cat,anchor=NW)
        canvas.create_image(10,0,image=data.scoreImg,anchor=NW)
        if data.result<2.5:
            data.text3=data.low1
        else:
            data.text3=data.high1
        if data.text3 in [data.high1,data.low1,data.low2]:
            canvas.create_image(205,500,image=data.text3,anchor=NW)
        elif data.text3 in [data.high2,data.high5]:
            canvas.create_image(155,500,image=data.text3,anchor=NW)
        elif data.text3 in [data.high3,data.high4]:
            canvas.create_image(105,500,image=data.text3,anchor=NW)

    elif data.scorer=='fox':
        canvas.create_image(350,415,image=data.fox,anchor=NW)
        canvas.create_image(10,0,image=data.scoreImg,anchor=NW)
        if data.result<2.5:
            data.text3=data.low1
        else:
            data.text3=data.high2
        if data.text3 in [data.high1,data.low1,data.low2]:
            canvas.create_image(165,500,image=data.text3,anchor=NW)
        elif data.text3 in [data.high2,data.high5]:
            canvas.create_image(115,500,image=data.text3,anchor=NW)
        elif data.text3 in [data.high3,data.high4]:
            canvas.create_image(45,500,image=data.text3,anchor=NW)

    elif data.scorer=='rabbit':
        canvas.create_image(420,420,image=data.rabbit,anchor=NW)
        canvas.create_image(10,0,image=data.scoreImg,anchor=NW)
        if data.result<2.5:
            data.text3=data.low1
        else:
            data.text3=data.high3
        if data.text3 in [data.high1,data.low1,data.low2]:
            canvas.create_image(215,500,image=data.text3,anchor=NW)
        elif data.text3 in [data.high2,data.high5]:
            canvas.create_image(165,500,image=data.text3,anchor=NW)
        elif data.text3 in [data.high3,data.high4]:
            canvas.create_image(115,500,image=data.text3,anchor=NW)

    elif data.scorer=='pikachu':
        canvas.create_image(360,430,image=data.pikachu,anchor=NW)
        canvas.create_image(10,0,image=data.scoreImg,anchor=NW)
        if data.result<2.5:
            data.text3=data.low2
        else:
            data.text3=data.high4
        if data.text3 in [data.high1,data.low1,data.low2]:
            canvas.create_image(155,500,image=data.text3,anchor=NW)
        elif data.text3 in [data.high2,data.high5]:
            canvas.create_image(105,500,image=data.text3,anchor=NW)
        elif data.text3 in [data.high3,data.high4]:
            canvas.create_image(65,500,image=data.text3,anchor=NW)

    elif data.scorer=='dog':
        canvas.create_image(370,428,image=data.dog,anchor=NW)
        canvas.create_image(10,0,image=data.scoreImg,anchor=NW)
        if data.result<2.5:
            data.text3=data.low2
        else:
            data.text3=data.high5
        if data.text3 in [data.high1,data.low1,data.low2]:
            canvas.create_image(165,500,image=data.text3,anchor=NW)
        elif data.text3 in [data.high2,data.high5]:
            canvas.create_image(115,500,image=data.text3,anchor=NW)
        elif data.text3 in [data.high3,data.high4]:
            canvas.create_image(65,500,image=data.text3,anchor=NW)

    elif data.scorer=='panda':
        canvas.create_image(400,415,image=data.panda,anchor=NW)
        canvas.create_image(10,0,image=data.scoreImg,anchor=NW)
        if data.result<2.5:
            data.text3=data.low2
        else:
            data.text3=data.high4
        if data.text3 in [data.high1,data.low1,data.low2]:
            canvas.create_image(195,500,image=data.text3,anchor=NW)
        elif data.text3 in [data.high2,data.high5]:
            canvas.create_image(145,500,image=data.text3,anchor=NW)
        elif data.text3 in [data.high3,data.high4]:
            canvas.create_image(95,500,image=data.text3,anchor=NW)
    
    #image from https://www.google.com/search?q=camera+pink+icon&source=lnms&t
    #bm=isch&sa=X&ved=0ahUKEwjYuq72_
    #-LaAhUKPN8KHXGMDdcQ_AUICigB&biw=1200&bih=666&dpr=2#imgrc=oZU8TRjqcDr0CM:
    camera=Image.open('images/camera2.png')
    resizeCamera=camera.resize((50,50),Image.ANTIALIAS)
    data.camera2=ImageTk.PhotoImage(resizeCamera)

    canvas.create_rectangle(10,4,160,29,fill='white')
    canvas.create_text(15,4,text='Score',font='Arial 20',anchor=NW)
    canvas.create_line(70,4,70,29)
    canvas.create_text(115,16,text=str(round(data.result,3))+'/5',font='Arial 20')
    
    canvas.create_image(5,445,image=data.camera2,anchor=NW)
    canvas.create_image(5,495,image=data.back,anchor=NW)
    canvas.create_image(5,545,image=data.forward,anchor=NW)
    
    if data.take==True:
        canvas.create_image(200,445,image=data.save,anchor=NW)

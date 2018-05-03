import cv2
from tkinter import *
import numpy as np
from PIL import Image, ImageTk

####################################
# faceEdit mode
####################################

def faceEditMousePressed(event, data):
    if len(data.faceCoor)>1:
        for face in data.faceCoor:
            if face[0]<=event.x<=face[0]+face[2] and face[1]<=event.y<=face[1]+10:
                data.faceCoor.remove(face)
            elif face[0]<=event.x<=face[0]+10 and face[1]<=event.y<=face[1]+face[3]:
                data.faceCoor.remove(face)
            elif face[0]+face[1]<=event.x<=face[0]+face[1]+10 and face[1]<=event.y<=face[1]+face[3]:
                data.faceCoor.remove(face)
            elif face[0]<=event.x<=face[0]+face[2] and face[1]+face[3]<=event.y<=face[1]+face[3]+10:
                data.faceCoor.remove(face)
    if 525<=event.x<=600 and 540<=event.y<=600:
        data.mode='edit'

def faceEditKeyPressed(event, data):
    if event.char=='w':
        data.faceCoor[0][2]+=2
    elif event.char=='h':
        data.faceCoor[0][3]+=2
    elif event.char=='e':
        data.faceCoor[0][2]-=2
    elif event.char=='j':
        data.faceCoor[0][3]-=2
    elif event.keysym=='Up':
        data.faceCoor[0][1]-=3
    elif event.keysym=='Down':
        data.faceCoor[0][1]+=3
    elif event.keysym=='Right':
        data.faceCoor[0][0]+=3
    elif event.keysym=='Left':
        data.faceCoor[0][0]-=3
    elif event.char==' ':
        data.faceCoor=[[200,200,100,100]]

def faceEditRedrawAll(canvas, data):
    canvas.create_image(data.width/2,data.height/2,image=data.img)
    canvas.create_image(5,5,image=data.faceImg,anchor=NW)
    canvas.create_image(525,540,image=data.angel,anchor=NW)
    
    for face in data.faceCoor:
        canvas.create_rectangle(face[0],face[1],face[0]+face[2],face[1]+face[3],outline='red',width=10)
    
    canvas.create_text(300, 10,
                       text="First determine the best rectangle (until only one left)", font="Arial 13 bold")
    canvas.create_text(300, 23,
                       text="Then use 'h' and 'j' to increase or decrease rectangle height", font="Arial 13 bold")
    canvas.create_text(300, 36,
                       text="and use 'w' and 'e' to increase or decrease rectangle width", font="Arial 13 bold")
    canvas.create_text(300, 49,
                       text="use up, down, left, right to move the rectangle", font="Arial 13 bold")
    canvas.create_text(300,560, text="If there's no rectangle, press 'Space' to generate one", font="Arial 18 bold")
    canvas.create_text(300,580, text="Once done, click the angel on the right to go back", font="Arial 18 bold")

####################################
# leftEyeEdit mode
####################################

def LeyeEditMousePressed(event, data):
    if len(data.lEyes)>1:
        for eye in data.lEyes:
            x0=eye[0]+data.faceCoor[0][0]
            x1=eye[0]+data.faceCoor[0][0]+eye[2]
            y0=eye[1]+data.faceCoor[0][1]
            y1=eye[1]+data.faceCoor[0][1]+eye[3]
            if x0<=event.x<=x1 and y0<=event.y<=y0+10:
                data.lEyes.remove(eye)
            elif x0<=event.x<=x1 and y1<=event.y<=y1+10:
                data.lEyes.remove(eye)
            elif x0<=event.x<=x0+10 and y0<=event.y<=y1:
                data.lEyes.remove(eye)
            elif x1<=event.x<=x1+10 and y0<=event.y<=y1:
                data.lEyes.remove(eye)
    if 525<=event.x<=600 and 540<=event.y<=600:
        data.mode='edit'

def LeyeEditKeyPressed(event, data):
    if event.char=='w':
        data.lEyes[0][2]+=2
    elif event.char=='h':
        data.lEyes[0][3]+=2
    elif event.char=='e':
        data.lEyes[0][2]-=2
    elif event.char=='j':
        data.lEyes[0][3]-=2
    elif event.keysym=='Up':
        data.lEyes[0][1]-=3
    elif event.keysym=='Down':
        data.lEyes[0][1]+=3
    elif event.keysym=='Right':
        data.lEyes[0][0]+=3
    elif event.keysym=='Left':
        data.lEyes[0][0]-=3
    elif event.char==' ':
        data.lEyes=[[50,50,50,50]]

def LeyeEditRedrawAll(canvas, data):
    canvas.create_image(data.width/2,data.height/2,image=data.img)
    canvas.create_image(5,5,image=data.LeyeImg,anchor=NW)
    canvas.create_image(525,540,image=data.angel,anchor=NW)
    
    for eyes in data.lEyes:
        x0=eyes[0]+data.faceCoor[0][0]
        x1=eyes[0]+data.faceCoor[0][0]+eyes[2]
        y0=eyes[1]+data.faceCoor[0][1]
        y1=eyes[1]+data.faceCoor[0][1]+eyes[3]
        canvas.create_rectangle(x0,y0,x1,y1,outline='red',width=10)
    
    canvas.create_text(300, 10,
                       text="First determine the best rectangle (until only one left)", font="Arial 13 bold")
    canvas.create_text(300, 23,
                       text="Then use 'h' and 'j' to increase or decrease rectangle height", font="Arial 13 bold")
    canvas.create_text(300, 36,
                       text="and use 'w' and 'e' to increase or decrease rectangle width", font="Arial 13 bold")
    canvas.create_text(300, 49,
                       text="use up, down, left, right to move the rectangle", font="Arial 13 bold")
    canvas.create_text(300,560, text="If there's no rectangle, press 'Space' to generate one", font="Arial 18 bold")
    canvas.create_text(300,580, text="Once done, click the angel on the right to go back", font="Arial 18 bold")
    
####################################
# rightEyeEdit mode
####################################

def ReyeEditMousePressed(event, data):
    if len(data.rEyes)>1:
        for eye in data.rEyes:
            x0=eye[0]+data.faceCoor[0][0]
            x1=eye[0]+data.faceCoor[0][0]+eye[2]
            y0=eye[1]+data.faceCoor[0][1]
            y1=eye[1]+data.faceCoor[0][1]+eye[3]
            if x0<=event.x<=x1 and y0<=event.y<=y0+10:
                data.rEyes.remove(eye)
            elif x0<=event.x<=x1 and y1<=event.y<=y1+10:
                data.rEyes.remove(eye)
            elif x0<=event.x<=x0+10 and y0<=event.y<=y1:
                data.rEyes.remove(eye)
            elif x1<=event.x<=x1+10 and y0<=event.y<=y1:
                data.rEyes.remove(eye)
    if 525<=event.x<=600 and 540<=event.y<=600:
        data.mode='edit'

def ReyeEditKeyPressed(event, data):
    if event.char=='w':
        data.rEyes[0][2]+=2
    elif event.char=='h':
        data.rEyes[0][3]+=2
    elif event.char=='e':
        data.rEyes[0][2]-=2
    elif event.char=='j':
        data.rEyes[0][3]-=2
    elif event.keysym=='Up':
        data.rEyes[0][1]-=3
    elif event.keysym=='Down':
        data.rEyes[0][1]+=3
    elif event.keysym=='Right':
        data.rEyes[0][0]+=3
    elif event.keysym=='Left':
        data.rEyes[0][0]-=3
    elif event.char==' ':
        data.rEyes=[[50,50,50,50]]

def ReyeEditRedrawAll(canvas, data):
    canvas.create_image(data.width/2,data.height/2,image=data.img)
    canvas.create_image(5,5,image=data.ReyeImg,anchor=NW)
    canvas.create_image(525,540,image=data.angel,anchor=NW)
    
    for eyes in data.rEyes:
        x0=eyes[0]+data.faceCoor[0][0]
        x1=eyes[0]+data.faceCoor[0][0]+eyes[2]
        y0=eyes[1]+data.faceCoor[0][1]
        y1=eyes[1]+data.faceCoor[0][1]+eyes[3]
        canvas.create_rectangle(x0,y0,x1,y1,outline='red',width=10)
    
    canvas.create_text(300, 10,
                       text="First determine the best rectangle (until only one left)", font="Arial 13 bold")
    canvas.create_text(300, 23,
                       text="Then use 'h' and 'j' to increase or decrease rectangle height", font="Arial 13 bold")
    canvas.create_text(300, 36,
                       text="and use 'w' and 'e' to increase or decrease rectangle width", font="Arial 13 bold")
    canvas.create_text(300, 49,
                       text="use up, down, left, right to move the rectangle", font="Arial 13 bold")
    canvas.create_text(300,560, text="If there's no rectangle, press 'Space' to generate one", font="Arial 18 bold")
    canvas.create_text(300,580, text="Once done, click the angel on the right to go back", font="Arial 18 bold")

####################################
# mouthEdit mode
####################################

def mouthEditMousePressed(event, data):
    if len(data.mouthCoor)>1:
        for mouth in data.mouthCoor:
            x0=mouth[0]+data.faceCoor[0][0]
            x1=mouth[0]+data.faceCoor[0][0]+mouth[2]
            y0=mouth[1]+data.faceCoor[0][1]
            y1=mouth[1]+data.faceCoor[0][1]+mouth[3]
            if x0<=event.x<=x1 and y0<=event.y<=y0+10:
                data.mouthCoor.remove(mouth)
            elif x0<=event.x<=x1 and y1<=event.y<=y1+10:
                data.mouthCoor.remove(mouth)
            elif x0<=event.x<=x0+10 and y0<=event.y<=y1:
                data.mouthCoor.remove(mouth)
            elif x1<=event.x<=x1+10 and y0<=event.y<=y1:
                data.mouthCoor.remove(mouth)
    if 525<=event.x<=600 and 540<=event.y<=600:
        data.mode='edit'

def mouthEditKeyPressed(event, data):
    if event.char=='w':
        data.mouthCoor[0][2]+=2
    elif event.char=='h':
        data.mouthCoor[0][3]+=2
    elif event.char=='e':
        data.mouthCoor[0][2]-=2
    elif event.char=='j':
        data.mouthCoor[0][3]-=2
    elif event.keysym=='Up':
        data.mouthCoor[0][1]-=3
    elif event.keysym=='Down':
        data.mouthCoor[0][1]+=3
    elif event.keysym=='Right':
        data.mouthCoor[0][0]+=3
    elif event.keysym=='Left':
        data.mouthCoor[0][0]-=3
    elif event.char==' ':
        data.mouthCoor=[[50,50,50,50]]

def mouthEditRedrawAll(canvas, data):
    canvas.create_image(data.width/2,data.height/2,image=data.img)
    canvas.create_image(5,5,image=data.mouthImg,anchor=NW)
    canvas.create_image(525,540,image=data.angel,anchor=NW)
    
    for mouth in data.mouthCoor:
        x0=mouth[0]+data.faceCoor[0][0]
        x1=mouth[0]+data.faceCoor[0][0]+mouth[2]
        y0=mouth[1]+data.faceCoor[0][1]
        y1=mouth[1]+data.faceCoor[0][1]+mouth[3]
        canvas.create_rectangle(x0,y0,x1,y1,outline='red',width=10)
    
    canvas.create_text(300, 10,
                       text="First determine the best rectangle (until only one left)", font="Arial 13 bold")
    canvas.create_text(300, 23,
                       text="Then use 'h' and 'j' to increase or decrease rectangle height", font="Arial 13 bold")
    canvas.create_text(300, 36,
                       text="and use 'w' and 'e' to increase or decrease rectangle width", font="Arial 13 bold")
    canvas.create_text(300, 49,
                       text="use up, down, left, right to move the rectangle", font="Arial 13 bold")
    canvas.create_text(300,560, text="If there's no rectangle, press 'Space' to generate one", font="Arial 18 bold")
    canvas.create_text(300,580, text="Once done, click the angel on the right to go back", font="Arial 18 bold")
    
####################################
# noseEdit mode
####################################

def noseEditMousePressed(event, data):
    if len(data.noseCoor)>1:
        for nose in data.noseCoor:
            x0=nose[0]+data.faceCoor[0][0]
            x1=nose[0]+data.faceCoor[0][0]+nose[2]
            y0=nose[1]+data.faceCoor[0][1]
            y1=nose[1]+data.faceCoor[0][1]+nose[3]
            if x0<=event.x<=x1 and y0<=event.y<=y0+10:
                data.noseCoor.remove(nose)
            elif x0<=event.x<=x1 and y1<=event.y<=y1+10:
                data.noseCoor.remove(nose)
            elif x0<=event.x<=x0+10 and y0<=event.y<=y1:
                data.noseCoor.remove(nose)
            elif x1<=event.x<=x1+10 and y0<=event.y<=y1:
                data.noseCoor.remove(nose)
    if 525<=event.x<=600 and 540<=event.y<=600:
        data.mode='edit'

def noseEditKeyPressed(event, data):
    if event.char=='w':
        data.noseCoor[0][2]+=2
    elif event.char=='h':
        data.noseCoor[0][3]+=2
    elif event.char=='e':
        data.noseCoor[0][2]-=2
    elif event.char=='j':
        data.noseCoor[0][3]-=2
    elif event.keysym=='Up':
        data.noseCoor[0][1]-=3
    elif event.keysym=='Down':
        data.noseCoor[0][1]+=3
    elif event.keysym=='Right':
        data.noseCoor[0][0]+=3
    elif event.keysym=='Left':
        data.noseCoor[0][0]-=3
    elif event.char==' ':
        data.noseCoor=[[50,50,50,50]]

def noseEditRedrawAll(canvas, data):
    canvas.create_image(data.width/2,data.height/2,image=data.img)
    canvas.create_image(5,5,image=data.noseImg,anchor=NW)
    canvas.create_image(525,540,image=data.angel,anchor=NW)
    
    for nose in data.noseCoor:
        x0=nose[0]+data.faceCoor[0][0]
        x1=nose[0]+data.faceCoor[0][0]+nose[2]
        y0=nose[1]+data.faceCoor[0][1]
        y1=nose[1]+data.faceCoor[0][1]+nose[3]
        canvas.create_rectangle(x0,y0,x1,y1,outline='red',width=10)
    
    canvas.create_text(300, 10,
                       text="First determine the best rectangle (until only one left)", font="Arial 13 bold")
    canvas.create_text(300, 23,
                       text="Then use 'h' and 'j' to increase or decrease rectangle height", font="Arial 13 bold")
    canvas.create_text(300, 36,
                       text="and use 'w' and 'e' to increase or decrease rectangle width", font="Arial 13 bold")
    canvas.create_text(300, 49,
                       text="use up, down, left, right to move the rectangle", font="Arial 13 bold")
    canvas.create_text(300,560, text="If there's no rectangle, press 'Space' to generate one", font="Arial 18 bold")
    canvas.create_text(300,580, text="Once done, click the angel on the right to go back", font="Arial 18 bold")
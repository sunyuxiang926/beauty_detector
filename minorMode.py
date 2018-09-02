import cv2
from tkinter import *
import numpy as np
from PIL import Image, ImageTk
import string

####################################
# userInformation mode
####################################

def userInformationMousePressed(event, data):
    if 250<=event.x<=350 and 140<=event.y<=180 and data.name!='':
        data.mode='start'
    elif 267<=event.x<=400 and 100<=event.y<=125:
        data.enter=True

def userInformationKeyPressed(event, data):
    if event.char in string.ascii_letters and data.enter==True:
        data.numEnter+=1
        data.textEnter+=event.char
    if event.keysym=='BackSpace':
        data.textEnter=data.textEnter[:-1]
        data.numEnter-=1
    if event.keysym=='Return':
        data.name=data.textEnter
        data.enter=False

def userInformationTimerFired(data):
    if data.timer%3==0 and data.enter==True:
        data.drawEnter=True
    else:
        data.drawEnter=False
    data.timer+=1

def userInformationRedrawAll(canvas, data):
    #image from https://www.google.com/search?biw=1200&bih=703&tbm=isch&sa=1&ei=SEDnW
    #puFHarp_QbcyqzQDA&q=jackson+wang+background&oq=jackson+wang+background&gs_l=psy
    #-ab.3..0.17059.18284.0.18549.8.8.0.0.0.0.180.722.5j3.8.0....0...1c.1.64.psy
    #-ab..1.2.236...0i30k1.0.2QijbgaUfVg#imgrc=LE5yJWOD7vfSHM:
    background=Image.open('images/background.png')
    resizeBackground=background.resize((600,600),Image.ANTIALIAS)
    data.background=ImageTk.PhotoImage(resizeBackground)
    
    #image from https://www.google.com/search?biw=1200&bih=662&tbm=isch&sa=1&ei=dU7nWsLFG
    #om1ggfp0orABg&q=pink+start+button&oq=pink+start+button&gs_l=psy-ab.3...120
    #32.12946.0.13227.4.4.0.0.0.0.71.228.4.4.0....0...1c.1.64.psy
    #-ab..0.2.130...0i7i30k1j0i8i7i30k1.0.AEt4DEAQNFY#imgrc=sgBWIHzl9oNvRM:
    start=Image.open('images/start.png')
    resizeStart=start.resize((100,40),Image.ANTIALIAS)
    data.start=ImageTk.PhotoImage(resizeStart)
    
    canvas.create_image(0,0,image=data.background,anchor=NW)
    canvas.create_image(250,140,image=data.start,anchor=NW)

    canvas.create_text(data.width/2, 30,
                       text="Welcome to Beauty Detector!", font="Arial 26 bold")
    canvas.create_text(data.width/2, 55,
                       text="Enter your name below!", font="Arial 20")
    canvas.create_text(data.width/2, 75,
                       text="Then press 'Start' to begin!", font="Arial 20")
    
    canvas.create_rectangle(200,100,400,125,fill='white')
    canvas.create_text(205,100,text='Name',anchor=NW,font='Arial 22')
    canvas.create_line(267,100,267,125)
    if data.enter==True and data.drawEnter==True:
        canvas.create_line(272+12*data.numEnter,103,272+12*data.numEnter,122)
    if data.enter==True:
        canvas.create_text(272,100,text=data.textEnter,anchor=NW,font='Arial 22')
    if data.name!='':
        canvas.create_text(272,100,text=data.name,anchor=NW,font='Arial 22')

####################################
# start mode
####################################

def startMousePressed(event, data):
    if 250<=event.x<=350 and 115<=event.y<=165:
        data.mode='shoot'

def startKeyPressed(event, data):
    pass

def startRedrawAll(canvas, data):
    canvas.create_image(0,0,image=data.background,anchor=NW)
    
    #image from https://www.google.com/search?biw=1200&bih=666&tbm=isch&sa=1&ei=hJPnW
    #sDqBuqj_QbW97O4Bg&q=next+button+pink&oq=next+button+pink&gs_l=psy
    #-ab.3...2242.4846.0.5050.9.8.1.0.0.0.54.352.7.7.0....0...1c.1.64.psy
    #ab..1.4.160...0j0i67k1j0i7i30k1j0i8i7i30k1.0.yYBG11KEzF4#im
    #gdii=4CztaIpY8Hp2ZM:&imgrc=Kw2A1bhScWpj4M:
    next=Image.open('images/next.png')
    resizeNext=next.resize((100,50),Image.ANTIALIAS)
    data.next=ImageTk.PhotoImage(resizeNext)
    
    canvas.create_image(250,115,image=data.next,anchor=NW)
    
    canvas.create_text(data.width/2, 15,
                       text="You need to take a picture of yourself first", font="Arial 20 bold")
    canvas.create_text(data.width/2, 35,
                       text="Then please help me to locate your facial features", font="Arial 20 bold")
    canvas.create_text(data.width/2, 55,
                       text="Once done, choose your favorite scorer!", font="Arial 20 bold") 
    canvas.create_text(data.width/2, 75,
                       text="Feel free to change your scorer!", font="Arial 20 bold")   
    canvas.create_text(data.width/2, 95,
                       text="Press 'Next' to take a picture!", font="Arial 20 bold")

####################################
# final mode
####################################

def finalMousePressed(event,data):
    pass

def finalKeyPressed(event,data):
    pass

def finalTimerFired(data):
    data.i=(data.i+1)%31
    data.i2=(data.i2+1)%19

def finalRedrawAll(canvas,data):
    canvas.create_image(0,0,image=data.frame2[data.i2],anchor=NW)
    canvas.create_image(50,330,image=data.frame[data.i],anchor=NW)
    
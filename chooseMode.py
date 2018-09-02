import cv2
from tkinter import *
import numpy as np
from PIL import Image, ImageTk

def chooseMousePressed(event, data):
    if 410<=event.x<=590 and 300<=event.y<=454:
        data.scorer='cat'
        data.mode='score'
    elif 135<=event.x<=420 and 0<=event.y<=214:
        data.scorer='fox'
        data.mode='score'
    elif 0<=event.x<=170 and 300<=event.y<=470:
        data.scorer='rabbit'
        data.mode='score'
    elif 170<=event.x<=410 and 400<=event.y<=580:
        data.scorer='pikachu'
        data.mode='score'
    elif 400<=event.x<=575 and 50<=event.y<=300:
        data.scorer='dog'
        data.mode='score'
    elif 0<=event.x<=200 and 100<=event.y<=300:
        data.scorer='panda'
        data.mode='score'

def chooseKeyPressed(event, data):
    if event.char=='k':
        data.mode='score'

def chooseRedrawAll(canvas, data):
    #image from https://www.google.com/search?q=cute+cartoon+animals&tbm=isch&tbo=u&source=univ&s
    #a=X&ved=0ahUKEwicipO-xt7aAhVEdt8KHYstBp0QsAQIJg&biw=1200&bih=703&dpr=2#imgrc=NEBPmE3N5ELTVM:
    cat=Image.open('images/cat.jpg')
    resizeCat=cat.resize((180,154),Image.ANTIALIAS)
    data.cat=ImageTk.PhotoImage(resizeCat)
    
    #image from https://www.google.com/search?q=cute+cartoon+animals&tbm=isch&tbo=u&sou
    #rce=univ&sa=X&ved=0ahUKEwicipO-xt7aAhVEdt8KHYstBp0QsAQIJg&biw=1200
    #&bih=703&dpr=2#imgrc=_M4sMJxTqujnRM:
    fox=Image.open('images/fox.jpg')
    resizeFox=fox.resize((285,214),Image.ANTIALIAS)
    data.fox=ImageTk.PhotoImage(resizeFox)
    
    #image from https://www.google.com/search?q=cute+cartoon+animals&tb
    #m=isch&tbo=u&source=univ&sa=X&ved=0ahUKEwicipO-xt7aAhVEdt
    #8KHYstBp0QsAQIJg&biw=1200&bih=703&dpr=2#imgrc=4yQabK_IdKkjKM:
    rabbit=Image.open('images/rabbit.jpg')
    resizeRabbit=rabbit.resize((170,170),Image.ANTIALIAS)
    data.rabbit=ImageTk.PhotoImage(resizeRabbit)
    
    #image from https://www.google.com/search?biw=1200&bih=703&tbm=isch&sa=1&ei=Hz3lWruVGs
    #zm_QaD_KSoBA&q=pikachu&oq=pi&gs_l=psy-ab.3.0.0i67k1l10.245008.24516
    #5.0.247821.2.2.0.0.0.0.60.116.2.2.0....0...1c.1.64.psy
    #-ab..0.2.116...0.0.ZeYWNAbwv_o#imgrc=btSnMLIibeQXIM:
    pikachu=Image.open('images/pikachu.jpg')
    resizePikachu=pikachu.resize((240,180),Image.ANTIALIAS)
    data.pikachu=ImageTk.PhotoImage(resizePikachu)
    
    #image from https://www.google.com/search?q=cartoon+dog&source=lnms&tbm=isch&sa=X&ved
    #=0ahUKEwicw6eh6N_aAhVNT98KHSpBBusQ_AUICigB&biw=1200&bih=703#imgrc=t1TKIksU37Do0M:
    dog=Image.open('images/dog.png')
    resizeDog=dog.resize((202,180),Image.ANTIALIAS)
    data.dog=ImageTk.PhotoImage(resizeDog)
    
    #image from https://www.google.com/search?tbm=isch&q=cartoon+panda&chips=q:ca
    #rtoon+panda,g_3:adorable&sa=X&ved=0ahUKEwin7eGdyN7aAhWomeAKHSnNA
    #94Q4lYIKygA&biw=1200&bih=669&dpr=2#imgrc=HJARg_jdzr86cM:
    panda=Image.open('images/panda.jpg')
    resizePanda=panda.resize((200,200),Image.ANTIALIAS)
    data.panda=ImageTk.PhotoImage(resizePanda)
    
    canvas.create_image(0,100,image=data.panda,anchor=NW)
    canvas.create_image(125,0,image=data.fox,anchor=NW)
    canvas.create_image(380,110,image=data.dog,anchor=NW)
    canvas.create_image(0,285,image=data.rabbit,anchor=NW)
    canvas.create_image(180,400,image=data.pikachu,anchor=NW)
    canvas.create_image(410,300,image=data.cat,anchor=NW)
    
    text=Image.open('images/text.png')
    resizeText=text.resize((180,104),Image.ANTIALIAS)
    data.text=ImageTk.PhotoImage(resizeText)
    
    text2=Image.open('images/text2.png')
    resizeText2=text2.resize((185,95),Image.ANTIALIAS)
    data.text2=ImageTk.PhotoImage(resizeText2)
    
    text3=Image.open('images/text3.png')
    resizeText3=text3.resize((200,116),Image.ANTIALIAS)
    data.text3=ImageTk.PhotoImage(resizeText3)
    
    text4=Image.open('images/text4.png')
    resizeText4=text4.resize((200,98),Image.ANTIALIAS)
    data.text4=ImageTk.PhotoImage(resizeText4)
    
    canvas.create_image(210,290,image=data.text,anchor=NW)
    canvas.create_image(5,450,image=data.text2,anchor=NW)
    canvas.create_image(395,450,image=data.text3,anchor=NW)
    canvas.create_image(360,10,image=data.text4,anchor=NW)
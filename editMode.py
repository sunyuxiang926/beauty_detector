import cv2
from tkinter import *
import numpy as np
from PIL import Image, ImageTk

####################################
# edit mode
####################################

def editMousePressed(event, data):
    if 5<=event.x<=55 and 5<=event.y<=55:
        data.mode='faceEdit'
    elif 60<=event.x<=110 and 5<=event.y<=55:
        data.mode='LeyeEdit'
    elif 115<=event.x<=165 and 5<=event.y<=55:
        data.mode='ReyeEdit'
    elif 170<=event.x<=220 and 5<=event.y<=55:
        data.mode='mouthEdit'
    elif 225<=event.x<=275 and 5<=event.y<=55:
        data.mode='noseEdit'
    elif 500<=event.x<=600 and 0<=event.y<=50:
        data.mode='choose'

def editKeyPressed(event, data):
    pass

def editRedrawAll(canvas, data):
    path='images/'+data.name+'.png'

    img=Image.open(path)
    data.img=ImageTk.PhotoImage(img)
    
    #image from https://www.google.com/search?biw=1200&bih=703&tbm=isch&sa=1&ei=YQblWvei
    #PPKIggfll4CoCw&q=face+emoji&oq=face+emoji&gs_l=psy-ab.
    #3..0l10.39294.40601.0.40850.9.8.0.1.1.0.62.444.8.8.0....0...1c.1.64.psy
    #-ab..0.9.446...0i67k1.0.rYjLo5LfJbM#imgrc=GBmr2pMlOUUYoM:
    face=Image.open('images/face.png')
    resizeFace=face.resize((50,50),Image.ANTIALIAS)
    data.faceImg=ImageTk.PhotoImage(resizeFace)
    
    #image from https://www.google.com/search?biw=1200&bih=664&tbm=isch&sa=1&ei=iS7lWpfdJuGj_Qa
    #coZSgBw&q=eye+blink+emoji&oq=eye+blink+emoji&gs_l=psy-ab.3..0.2181.2
    #634.0.2925.2.1.0.1.1.0.52.52.1.1.0....0...1c.1.64.psy
    #-ab..0.2.54....0._IVsLQZDxFM#imgrc=b3ULkU6qOS4SYM:
    Leye=Image.open('images/leftEye.jpg')
    resizeLEye=Leye.resize((50,50),Image.ANTIALIAS)
    data.LeyeImg=ImageTk.PhotoImage(resizeLEye)

    #image from https://www.google.com/search?biw=1200&bih=664&tbm=isch&sa=1&ei=iS7lW
    #pfdJuGj_QacoZSgBw&q=eye+blink+emoji&oq=eye+blink+emoji&gs_l=psy-ab.3..0.218
    #1.2634.0.2925.2.1.0.1.1.0.52.52.1.1.0....0...1c.1.64.psy
    #-ab..0.2.54....0._IVsLQZDxFM#imgrc=kBtgcm79yF9XyM:
    Reye=Image.open('images/rightEye.jpg')
    resizeREye=Reye.resize((50,50),Image.ANTIALIAS)
    data.ReyeImg=ImageTk.PhotoImage(resizeREye)
    
    #image from https://www.google.com/search?biw=1200&bih=662&tbm=isch&sa=1&ei=Og3lWvPcEuWW
    #_QanvoiwCQ&q=mouth+emoji&oq=mouth+emoji&gs_l=psy-ab.3..0l4j0
    #i7i30k1l6.171729.174186.0.174412.13.12.1.0.0.0.110.777.11j1.12.0....0...
    #1c.1.64.psy-ab..0.13.779...0i7i5i30k1j0i13k1j0i67k1.0.40puxwcUfcI#imgrc=2yJKoCu_bQ_WMM:
    mouth=Image.open('images/mouth.jpg')
    resizeMouth=mouth.resize((50,50),Image.ANTIALIAS)
    data.mouthImg=ImageTk.PhotoImage(resizeMouth)
    
    #https://www.google.com/search?biw=1200&bih=662&tbm=isch&sa=1&ei=6Q3lWufVH62Rg
    #gfI-4ToCw&q=nose+emoji&oq=nose+emoji&gs_l=psy-ab.3..0l5j0i7i30k1l5.182320.182718.0
    #.182956.4.4.0.0.0.0.106.284.3j1.4.0....0...1c.1.64.psy-ab..1.3.224...0i6
    #7k1.0.VGW4--Hukow#imgrc=uWWLhMmxQu24vM:
    nose=Image.open('images/nose.jpg')
    resizeNose=nose.resize((50,50),Image.ANTIALIAS)
    data.noseImg=ImageTk.PhotoImage(resizeNose)
    
    #image from https://image.baidu.com/search/detail?ct=503316480&z=0&ipn=d&word=%E
    #5%B0%8F%E5%A4%A9%E4%BD%BF&step_word=&hs=0&pn=6&spn=0&di=141609152740&pi=0&rn=1&
    #tn=baiduimagedetail&is=0%2C0&istype=0&ie=utf-8&oe=utf-8&in=&cl=2&lm=-1&st=undef
    #ined&cs=1740069886%2C3593734650&os=24386632%2C1475642463&simid=4245439472%2C713
    #769172&adpicid=0&lpn=0&ln=1978&fr=&fmq=1524965698649_R&fm=&ic=undefined&s=undefined&se
    #=&sme=&tab=0&width=undefined&height=undefined&face=undefined&ist=&jit=&cg=&bdtype=0&oriquery
    #=&objurl=http%3A%2F%2Fpic5.photophoto.cn%2F20071116%2F0044040919335658_b.jpg&fro
    #murl=ippr_z2C%24qAzdH3FAzdH3Fooo_z%26e3Bri5p5ri5p5_z%26e3B
    #vgAzdH3FrtvAzdH3Fab8caacd_z%26e3Bip4s&gsm=0&rpstart=0&rpnum=0&islist=&querylist=
    angel=Image.open('images/angel.jpg')
    resizeAngel=angel.resize((75,60),Image.ANTIALIAS)
    data.angel=ImageTk.PhotoImage(resizeAngel)

    canvas.create_image(data.width/2,data.height/2-5,image=data.img)
    canvas.create_image(5,5,image=data.faceImg,anchor=NW)
    canvas.create_image(60,5,image=data.LeyeImg,anchor=NW)
    canvas.create_image(115,5,image=data.ReyeImg,anchor=NW)
    canvas.create_image(170,5,image=data.mouthImg,anchor=NW)
    canvas.create_image(225,5,image=data.noseImg,anchor=NW)
    
    canvas.create_text(300, 545,
                       text="Now help me to locate your facial features", font="Arial 18 bold")
    canvas.create_text(300, 565,
                       text="by clicking the emoji above", font="Arial 18 bold")
    canvas.create_text(300, 585,
                       text="Once done, press 'next' to proceed", font="Arial 18 bold")
    
    canvas.create_image(500,0,image=data.next,anchor=NW)
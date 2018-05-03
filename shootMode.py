import cv2
from tkinter import *
import numpy as np
from PIL import Image, ImageTk
import string

####################################
# shoot mode
####################################

def shootMousePressed(event, data):
    if 175<=event.x<=275 and 120<=event.y<=200:
        capturePic(data,data.name)
    elif 325<=event.x<=425 and 120<=event.y<=170:
        data.mode='analyze'

def shootKeyPressed(event, data):
    pass

def capturePic(data,name):
    cam=cv2.VideoCapture(0) #create a VideoCapture object with device index 0
    
    cam.set(cv2.CAP_PROP_FRAME_WIDTH,480);
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT,640)
    
    cv2.namedWindow("shoot") #give specific name to the window we create
    
    while True: #run until break
        ret, frame = cam.read() #ret is whether the reading is successful
                                #frame is the returned image
        cv2.imshow("shoot", frame) #display an image in a window
        if not ret: #read not successful
            break
        k = cv2.waitKey(1) #call every 1 ms (1 ms delay) to get the key pressed
    
        if k%256 == 32:
            # SPACE pressed
            imgName = "%s.png" %name
            cv2.imwrite('images/'+imgName, frame) #save the image
            print("%s saved!" %imgName)
            break
    
    #release from job and close window
    cam.release()

def shootRedrawAll(canvas, data):
    canvas.create_image(0,0,image=data.background,anchor=NW)
    
    canvas.create_text(data.width/2, 15,
                       text="Press the camera to take a picture", font="Arial 20 bold")
    canvas.create_text(data.width/2, 35,
                       text="When the camera opens, press space to capture picture", font="Arial 20")
    canvas.create_text(data.width/2, 55,
                       text="You can take as many pictures as you want,", font="Arial 20")
    canvas.create_text(data.width/2, 75,
                       text="but only the last one will be used to score", font="Arial 20")
    canvas.create_text(data.width/2, 105,
                       text="If you finished, press 'next' to proceed!", font="Arial 20 bold")              
    
    #image from https://www.google.com/search?q=camera+pink+icon&source=lnms&tbm=isch&sa=X&ved=0a
    #hUKEwjYuq72_-LaAhUKPN8KHXGMDdcQ_AUICigB&biw=1200&bih=666&dpr=2#imgrc=CC5OFSzZNFVftM:
    camera=Image.open('images/camera.png')
    resizeCamera=camera.resize((100,60),Image.ANTIALIAS)
    data.camera=ImageTk.PhotoImage(resizeCamera)
    
    canvas.create_image(325,135,image=data.next,anchor=NW)
    canvas.create_image(175,130,image=data.camera,anchor=NW)
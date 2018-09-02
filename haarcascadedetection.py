import numpy as np
import cv2
from matplotlib import pyplot as plt

#datasets used in this file were downloaded from https://www.kaggle.com/c/
#facial-keypoints-detection/data

#Using Haar Feature-based Cascade Classifiers to do facial recognition

#Table of 15 facial keypoints
# Left eye center             Right eye center
# Left eye inner corner       Right eye inner corner
# Left eye outer corner       Right eye outer corner
# Left eyebrow inner end      Right eyebrow inner end
# Left eyebrow outer end      Right eyebrow outer end
# Mouth left corner           Mouth right corner
# Mouth center top lip        Mouth center bottom lip
# Nose tip

#Haar Cascade xml file for face, eyes, nose, and mouse are from 
#http://alereimondo.no-ip.org/OpenCV/34 
#https://github.com/opencv/opencv

def capturePic(name):
    cam=cv2.VideoCapture(0) #create a VideoCapture object with device index 0
    
    cam.set(cv2.CAP_PROP_FRAME_WIDTH,480);
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT,640)
    
    cv2.namedWindow("shoot") #give specific name to the window we create
    
    counter=0 #used in image name
    
    while True: #run until break
        ret, frame = cam.read() #ret is whether the reading is successful
                                #frame is the returned image
        cv2.imshow("shoot", frame) #display an image in a window
        if not ret: #read not successful
            break
        k = cv2.waitKey(1) #call every 1 ms (1 ms delay) to get the key pressed
    
        if k%256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break
        elif k%256 == 32:
            # SPACE pressed
            imgName = "%s.png" %name
            cv2.imwrite('images/'+imgName, frame) #save the image
            print("%s saved!" %imgName)
            counter += 1
            detectFace('images/'+imgName)
    
    #release from job and close window
    cam.release()
    
    #code from stack overflow, usual code result in window freezed
    #https://stackoverflow.com/questions/6116564/
    #destroywindow-does-not-close-window-on-mac-using-python-and-opencv
    cv2.waitKey(0) # close window when a key press is detected
    cv2.destroyWindow('shoot')
    cv2.waitKey(1)

def detectFace(path):
    faceL=[]
    rEyeL=[]
    lEyeL=[]
    mouthL=[]
    noseL=[]
    
    # img = cv2.imread(path)
    # 
    # face = cv2.CascadeClassifier('haarcascades/model1/face.xml')
    # Reye = cv2.CascadeClassifier('haarcascades/model1/Reye.xml') 
    # Leye = cv2.CascadeClassifier('haarcascades/model1/Leye.xml') 
    # mouth = cv2.CascadeClassifier('haarcascades/model1/mouth.xml') 
    # nose = cv2.CascadeClassifier('haarcascades/model1/nose.xml') 
    # 
    # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 
    # faceC = face.detectMultiScale(gray, 1.3, 5)
    # 
    # for (x,y,w,h) in faceC:
    #     faceL.append((x,y,w,h))

   ##       roiGray = gray[y:y+h, x:x+w]
    #     roiImg = img[y:y+h, x:x+w] #eyes, nose, and mouth always on face, bounding box useful

   ##       ReyeC = Reye.detectMultiScale(roiGray)
    #     LeyeC = Leye.detectMultiScale(roiGray)
    #     mouthC = mouth.detectMultiScale(roiGray)
    #     noseC = nose.detectMultiScale(roiGray)
    #     
    #     for (x,y,w,h) in ReyeC:
    #             rEyeL.append((x,y,w,h))
    #     
    #     for (x,y,w,h) in LeyeC:
    #             lEyeL.append((x,y,w,h))
    #     
    #     for (x,y,w,h) in mouthC:
    #             mouthL.append((x,y,w,h))
    #     
    #     for (x,y,w,h) in noseC:
    #             noseL.append((x,y,w,h))
    # 
    # print (faceL,rEyeL,lEyeL,mouthL,noseL)
    
    img = cv2.imread(path)
    
    face = cv2.CascadeClassifier('haarcascades/model1/face.xml')
    Reye = cv2.CascadeClassifier('haarcascades/model1/Reye.xml') 
    Leye = cv2.CascadeClassifier('haarcascades/model1/Leye.xml') 
    mouth = cv2.CascadeClassifier('haarcascades/model1/mouth.xml') 
    nose = cv2.CascadeClassifier('haarcascades/model1/nose.xml') 
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    faceC = face.detectMultiScale(gray, 1.3, 5)
    
    for (x,y,w,h) in faceC:
        cv2.rectangle(img,(x,y),(x+w,x+h),(255,0,0)) #red for faces
        faceL.append((x,y,w,h))

        roiGray = gray[y:y+h, x:x+w]
        roiImg = img[y:y+h, x:x+w] #eyes, nose, and mouth always on face, bounding box useful

        ReyeC = Reye.detectMultiScale(roiGray)
        LeyeC = Leye.detectMultiScale(roiGray)
        mouthC = mouth.detectMultiScale(roiGray)
        noseC = nose.detectMultiScale(roiGray)
    
        for (x,y,w,h) in ReyeC:
                cv2.rectangle(roiImg,(x,y),(x+w,x+h),(0,255,0)) #green for right eyes
                rEyeL.append((x,y,w,h))
        
        for (x,y,w,h) in LeyeC:
                cv2.rectangle(roiImg,(x,y),(x+w,x+h),(0,0,255)) #blue for left eyes
                lEyeL.append((x,y,w,h))
        
        for (x,y,w,h) in mouthC:
                cv2.rectangle(roiImg,(x,y),(x+w,x+h),(255,0,255)) #magenta for mouth
                mouthL.append((x,y,w,h))
        
        for (x,y,w,h) in noseC:
                cv2.rectangle(roiImg,(x,y),(x+w,x+h),(255,255,0)) #yellow for nose
                noseL.append((x,y,w,h))
                
    print (faceL,rEyeL,lEyeL,mouthL,noseL)
    cv2.imshow('detect',img)
    cv2.imwrite('images/detect1.png',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


#data from https://github.com/HCIILAB/SCUT-FBP5500-Database-Release

import numpy
import os
import math
import string
import csv

def distance(p1,p2):
    return ((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)**0.5

fileLst=[]
for files in os.listdir('readable data'):
    fileLst.append(files)

def generateReducedFile():
    dst='reduced data'
    
    if not os.path.exists(dst):
        os.mkdir(dst)
    
    for file in fileLst:
        landmarks=(numpy.loadtxt('readable data/'+file,delimiter=' '))
        featureSrc=[]
        for i in range(len(landmarks)):
            if i in [0, 1, 4, 5, 6, 8, 11, 14, 16, 17, 18, 21, 58, 59, 60, 62, 70, 72, 73, 79]:
                featureSrc.append(landmarks[i])
    
        A=[featureSrc[0][0]-distance(featureSrc[0],featureSrc[3])/(2**0.5),featureSrc[0][1]]
        B=[featureSrc[0][0]+distance(featureSrc[0],featureSrc[3])/(2**0.5),featureSrc[0][1]]
        C=[featureSrc[6][0]-distance(featureSrc[6],featureSrc[4])/(2**0.5),featureSrc[6][1]]
        D=[featureSrc[6][0]+distance(featureSrc[6],featureSrc[4])/(2**0.5),featureSrc[6][1]]
        E=[featureSrc[14][0]+distance(featureSrc[14],featureSrc[17])/2,featureSrc[14][1]]
        F=[featureSrc[15][0]+distance(featureSrc[15],featureSrc[16])/2,featureSrc[15][1]]
        G=[featureSrc[19][0]+distance(featureSrc[19],featureSrc[18])/2,featureSrc[19][1]]
        
        width=(distance(A,B)+distance(C,D))/2
        height=(distance(A,C)+distance(B,D))/2
        lDiag=distance(A,D)
        rDiag=distance(B,C)
        
        feature=[distance(A,featureSrc[12])/lDiag*100,
                 distance(B,featureSrc[13])/rDiag*100,
                 distance(featureSrc[12],featureSrc[13])/width*100,
                 distance(featureSrc[1],featureSrc[12])/height*100,
                 distance(featureSrc[11],featureSrc[13])/height*100,
                 distance(featureSrc[3],featureSrc[12])/width*100,
                 distance(featureSrc[9],featureSrc[13])/width*100,
                 distance(E,F)/height*100,
                 distance(featureSrc[12],F)/lDiag*100,
                 distance(featureSrc[13],F)/rDiag*100,
                 distance(G,F)/height*100,
                 distance(featureSrc[19],F)/rDiag*100,
                 distance(featureSrc[18],F)/lDiag*100,
                 distance(featureSrc[5],featureSrc[19])/width*100,
                 distance(featureSrc[7],featureSrc[18])/width*100,
                 distance(featureSrc[6],G)/height*100,
                 distance(featureSrc[0],E)/height*100]
        
        newFile=open(dst+'/'+file,'w')
        for row in feature:
            newFile.write(str(row)+'\n')
        
        newFile.close()

reFileLst=[]
for files in os.listdir('reduced data'):
    reFileLst.append(files)

def generateFeatureMatrix():
    labelFile=open('SCUT-FBP5500_with_Landmarks/train_test_files/SCUT-FBP5500.txt', 'r')
    labelLst=[line.split(',') for line in labelFile.readlines()]
    
    label=[]
    feature=[]
    
    for i in range(len(labelLst)):
        for files in reFileLst:
            if os.path.splitext(labelLst[i][0].split(' ')[0])[0] == os.path.splitext(files)[0]:
                label.append(labelLst[i][0].split(' ')[1][:-1])
                feature.append(numpy.loadtxt('reduced data/'+files))
    
    numpy.savetxt('generated data/features.csv', feature, delimiter=',',fmt='%.4f')


    with open('generated data/label.csv', "w") as output:
        writer = csv.writer(output, lineterminator='\n')
        for val in label:
            writer.writerow([val])
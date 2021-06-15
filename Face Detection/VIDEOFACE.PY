# importing opencv liberary
import cv2

from random import randrange as r

# dataset load
trainedData=cv2.CascadeClassifier('face.xml')

# start the webcam
cam = cv2.VideoCapture('My Video.mp4')

while True:

    success,frame=cam.read()


    # converstion of image in black and white (grayscale)
    grayimg=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    #detect faces
    faceCoordinates=trainedData.detectMultiScale(frame)


    for x,y,w,h in faceCoordinates:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(r(0,256),r(0,256),r(0,256)),2)

    #display image
    cv2.imshow('window',frame)

    #pause execution of the program until any key is pressed
    key = cv2.waitKey(1)
    if(key==81 or key==113):
        break
cam.release()    
 
print('END OF PROGRAM')


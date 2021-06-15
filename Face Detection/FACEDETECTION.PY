# importing opencv liberary
import cv2

# dataset load
trainedData=cv2.CascadeClassifier('face.xml')

# choose a image
img=cv2.imread('one.jpg')

# converstion of image in black and white (grayscale)
grayimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#detect faces
faceCoordinates=trainedData.detectMultiScale(grayimg)

#print(faceCoordinates)
# [[173 179 371 371]]

x,y,w,h=faceCoordinates[0]

cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)

#display image
cv2.imshow('Single Person',img)

#pause execution of the program until any key is pressed
cv2.waitKey()
 
print('END OF PROGRAM')
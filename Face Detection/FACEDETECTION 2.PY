# importing opencv liberary
import cv2

# dataset load
trainedData=cv2.CascadeClassifier('face.xml')

# choose a image
img=cv2.imread('two.jpg')

# converstion of image in black and white (grayscale)
grayimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#detect faces
faceCoordinates=trainedData.detectMultiScale(grayimg)

#print(faceCoordinates)
# [[ 866  557  226  226]
# [ 195  604  290  290]
# [1448  608  289  289]
# [1657  405  739  739]
# [1171  573  237  237]
#[ 616  738  260  260]
#[1663 1338   46   46]
#[2026 1292   91   91]]

for i in range (0,6):
    x,y,w,h=faceCoordinates[i]
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)

img_scaled = cv2.resize(img,None,fx=0.25,fy=0.25)
cv2.imshow('Scaling - Linear Interplotation',img_scaled)
cv2.waitKey()

#display image
#cv2.imshow('Single Person',img_scaled)

#pause execution of the program until any key is pressed
cv2.waitKey()

 
print('END OF PROGRAM')


 
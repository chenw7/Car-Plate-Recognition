#This program uses existing libraries (cv2, matplotlib, numpy, imutils, easyocr) to 
#identify the license plate number of the image of a car provided.
#Author @Wei-cen Chen
#Version April 23, 2022

#Importing all the necessary libraries for this program
import cv2
from matplotlib import pyplot as plt
import numpy as np
import imutils
import easyocr

#Read image and convert to grayscale
img = cv2.imread('plate1.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
plt.imshow(cv2.cvtColor(gray, cv2.COLOR_BGR2RGB))

#Find edges in the picture by using a bilateralFilter on the car image
bfilter = cv2.bilateralFilter(gray, 11, 17, 17) #reduces noise in picture
edged = cv2.Canny(bfilter, 30, 200)
plt.imshow(cv2.cvtColor(edged, cv2.COLOR_BGR2RGB))

#Find contours by identifying keypoints in the image
keypoints = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contours = imutils.grab_contours(keypoints)
contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]

location = None
for contour in contours:
    approx = cv2.approxPolyDP(contour, 10, True)
    if len(approx) == 4:
        location = approx
        break
        
#After finding contour, draw it out and crop out an image of the car's license plate
mask = np.zeros(gray.shape, np.uint8)
new_image = cv2.drawContours(mask, [location], 0,255, -1)
new_image = cv2.bitwise_and(img, img, mask=mask)

#The resulting image will ideally be a rectangle that contains the plate number
plt.imshow(cv2.cvtColor(new_image, cv2.COLOR_BGR2RGB))

#Reads the text/numbers in the license plate using easyOCR
reader = easyocr.Reader(['en'])
result = reader.readtext(cropped_image)

#Identify license plate, draw a rectangle around it, and print plate number on screen
text = result[0][-2]
font = cv2.FONT_HERSHEY_SIMPLEX
res = cv2.putText(img, text=text, org=(approx[0][0][0], approx[1][0][1]+60), fontFace=font, fontScale=1, color=(0,255,0), thickness=2, lineType=cv2.LINE_AA)
res = cv2.rectangle(img, tuple(approx[0][0]), tuple(approx[2][0]), (0,255,0),3)
plt.imshow(cv2.cvtColor(res, cv2.COLOR_BGR2RGB))

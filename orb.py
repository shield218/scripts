import cv2
import os

path = 'f:/video/card.png'

img = cv2.imread(path)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# orb = cv2.ORB()
orb = cv2.ORB_create()
# find the keypoints with orb
# kp = orb.detect(img,None)
kp, des = orb.detectAndCompute(img, None)
print(kp)
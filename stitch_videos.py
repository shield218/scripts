import cv2
import numpy as np

cap1 = cv2.VideoCapture('f:/video/ttrack_out.avi')
cap2 = cv2.VideoCapture('f:/video/lk_orb1.avi')
out = cv2.VideoWriter('f:/video/comparison1.mp4',cv2.VideoWriter_fourcc('M','J','P','G'), 30, (640, 720))

cnt=0
while(cnt<473):
    ret1,frame1 = cap1.read()
    ret2,frame2 = cap2.read()
    
    frame = np.concatenate((frame1, frame2), 0)
    frame = cv2.resize(frame, (640, 720))
    out.write(frame)
    cnt+=1

cap1.release()
cap2.release()
out.release()

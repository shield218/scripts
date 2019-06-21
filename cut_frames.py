import cv2

cap = cv2.VideoCapture('f:/video/lk_orb.avi')
out = cv2.VideoWriter('f:/video/lk_orb1.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 30, (1280,720))

for i in range(474):
    ret, frame = cap.read()
    if i>0:
        out.write(frame)

cap.release()
out.release()
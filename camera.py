import cv2
import sys

source=0
if len(sys.argv)>1:
    s=sys.argv[1]
cap=cv2.VideoCapture(source)
win_name='Camera Preview'
cv2.namedWindow(win_name,cv2.WINDOW_NORMAL)
while cv2.waitKey(1) != 27:
    has_frame, frame=cap.read()
    if not has_frame:
        break
    cv2.imshow (win_name,frame)
cap.release()
cv2.destroyWindow(win_name)

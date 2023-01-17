import cv2
print(cv2.__version__)
cam=cv2.VideoCapture(0)
while True:

    ret,frame=cam.read()
    cv2.imshow ('nanocam' , frame)
    if cv2.waitkey(1)==ord('v') :
        break
cam.release()
cv2.destroyAllWindows

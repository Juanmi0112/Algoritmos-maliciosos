import cv2
import telepot
import keyboard
import token 


def receiver_id():


print(cv2.__version__)
cam=cv2.VideoCapture(0)
while True:

    ret,frame=cam.read()
    cv2.imshow ('nanocam' , frame)
    if cv2.waitkey(1)==ord('v') :
        break
cam.release()
cv2.destroyAllWindows

def ctrlX():
    def press_ctrl_x():
        takePhoto()


hotkeys = {'<ctrl>+x': press_ctrl_x}

with keyboard.GlobalHotKeys(hotkeys) as listener:
    listener.join()

def takePhoto():
   
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cv2.imshow('C:\Users\juanm\Downloads',frame)   #colocar direccion de la imagen reemplazar por la x
    cap.release()
    bot = telepot.Bot(token)
    bot.notifyMessage(receiver_id,'picture taken.')
    bot.sendPicture(receiver_id, photo=open('SCREENSHOT' + img + 'jpeg', 'rb')) #envia la foto



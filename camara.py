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

def ctrlX():
    def press_ctrl_x():
        takePhoto()


hotkeys = {'<ctrl>+x': press_ctrl_x}

with keyboard.GlobalHotKeys(hotkeys) as listener:
    listener.join()

def takePhoto():
    import cv2
    import telepot
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cv2.imwrite('c:xxxxxxxxxxxxxxxxxxx,frame)   #colocar direccion de la imagen reemplazar por la x
    cap.release()
    bot = telepot.Bot(token)
    bot.Message(receiver_id,'picture taken.')
    bot.sendphoto(receiver_id, photo=open('SCREENSHOT', 'rb')) #sustituir rb por frame



import cv2

cam = cv2.VideoCapture(0)

img_counter = 0
        
while True:
    ret, frame = cam.read()
    if not cam.isOpened():
        raise IOError("Cannot use webcam")
    elif cam.isOpened():
        cv2.imshow('frame', frame)
    if not ret:
        break
    if cv2.waitKey(1) == 27:
        #ESC pressed
        break
    elif cv2.waitKey(1) == 32:
        #SPACE pressed
        img_name = 'students_{}.png'.format(img_counter)
        cv2.imwrite(img_name, frame)
        print(img_name + 'was captured')
        img_counter += 1
cam.release()
cv2.destroyAllWindows()
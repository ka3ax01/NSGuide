from kivy.app import App
# from kivy.tools.packaging.pyinstaller_hooks.pyi_rth_kivy import root
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
import cv2
import time
import algo


class MainWindow(Screen):
    pass

class LanguageWindow(Screen):
    pass

class ResultWindow(Screen):
    pass

class PhotoWindow(Screen):
    def capture(self):
        cam = cv2.VideoCapture(0)
        img_counter = 0
        #cam = self.ids['camera']
        
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
                img_name = 'image_{}.png'.format(img_counter)
                cv2.imwrite(img_name, frame)
                print(img_name + 'was captured')
                img_counter += 1
        cam.release()
        cv2.destroyAllWindows()
        
        print(algo.predicts(img_name))
# =============================================================================
#         '''
#         Function to capture the images and give them the names
#         according to their captured time and date.
#         '''
#         captureDevice = cv2.VideoCapture(0, cv2.CAP_DSHOW) #captureDevice = camera
#         camera = self.ids['camera']
#         timestr = time.strftime("%Y%m%d_%H%M%S")
#         photoname = "IMG_{}.png".format(timestr)
#         camera.export_to_png(photoname)
#         print("Captured")
# 
#         '''
#         We choose captured photo and make a prediction by our
#          convolutional neural network and print it to the console.
#         '''
#         print(algo.predicts(photoname))
# =============================================================================




class TextWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("TheGuidance.kv")

class TheGuidanceApp(App):
    def build(self):
        return kv


TheGuidanceApp().run()

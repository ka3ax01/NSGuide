# =============================================================================
# import scipy as sp
# import pylab as pl
# 
# v = sp.array([[1.],[0.5]])
# v = v*2
# pl.plot([0,v[0]],[0,v[1]])
# pl.xlim([-3,3])
# pl.ylim([-3,3])
# print(v.shape)
# print(v.T.shape)
# =============================================================================
from kivy.app import App
# from kivy.tools.packaging.pyinstaller_hooks.pyi_rth_kivy import root
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
import time

class MainWindow(Screen):
    pass

class LanguageWindow(Screen):
    pass

class PhotoWindow(Screen):
    def capture(self):
        '''
        Function to capture the images and give them the names
        according to their captured time and date.
        '''
        camera = self.ids['camera']
        timestr = time.strftime("%Y%m%d_%H%M%S")
        camera.export_to_png("IMG_{}.png".format(timestr))
        print("Captured")

class TextWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("TheGuidance.kv")

class TheGuidanceApp(App):
    def build(self):
        return kv


TheGuidanceApp().run()

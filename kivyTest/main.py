import kivy
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label

class MainWindow(Screen):
    pass


#Run

#kv = Builder.load_file("guidance.kv")

class TheGuidanceApp(App):
    def build(self):
        return Label(text='Hello world')


TheGuidanceApp().run()
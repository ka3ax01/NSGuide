from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout 
from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
import time
import algo

class WindowManager(ScreenManager):
    pass

class MainWindow(Screen):
    pass

class LanguageWindow(Screen):
    pass

class TextWindow(Screen):
    def on_pre_enter(self, *args):
        b = BoxLayout(orientation ='vertical')
  
        # Adding the text input
        t = TextInput(font_size = 50,
                      size_hint_y = None,
                      height = 100)
          
        f = FloatLayout()
  
        # By this you are able to move the
        # Text on the screen to anywhere you want
        s = Scatter()
  
        l = Label(text ="Hello !",
                  font_size = 50)
  
        f.add_widget(s)
        s.add_widget(l)
  
        b.add_widget(t)
        b.add_widget(f)
  
        # Binding it with the label
        t.bind(text = l.setter('text'))
  
          
        return b
        

class TextConfirmationWindow(Screen):
    def on_pre_enter(self, *args):
        self.ids.img.source = self.manager.ids.entry.image

class InformationWindow(Screen):
    def on_pre_enter(self, *args):
        self.ids.img.source = self.manager.ids.entry.image
        self.ids.txts.source = self.manager.ids.entry.text


class PhotoConfirmationWindow(Screen):
    def on_pre_enter(self, *args):
        self.ids.img.source = self.manager.ids.entry.image
        #self.ids.txts.source = self.manager.ids.entry.text

class PhotoWindow(Screen):
    
    image = None
    
    
    
    def capture(self):
        
        '''
        Function to capture the images and give them the names
        according to their captured time and date.
        '''
        
        
        camera = self.ids['camera']
        timestr = time.strftime("%Y%m%d_%H%M%S")
        img_name = "IMG_"+timestr+".jpg"
        camera.export_to_png(img_name)
        result, score, classes = (algo.predicts(img_name))
        
        self.image = "images/" + str(result) +".jpg"
        #self.text = textL[str(result)]
        self.text = "text/" + str(result) +".png"
        
        print("Captured")
        #print(result)
        print("Our algorithm consider that it is {} with {} percent".format(result, score[classes.index(result)]*100))




class TestCamera(MDApp):
    
    def build(self):
        return Builder.load_file("Guidance.kv")


TestCamera().run()
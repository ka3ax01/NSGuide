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
        #textL = {"Baiterek": "Baiterek is a monument and observation tower in Nur-Sultan, the capital city of Kazakhstan. A tourist attraction popular with foreign visitors and Kazakhstanis, it is emblematic of the city, which became capital of the country in 1997.",
        #     "Expo": "Exhibition Expo-2017 – was held in the capital of Kazakhstan, Nur-Sultan cityfrom June 10 to September 10, 2017. 115 states and 22 international organizations took part in it. The exhibition was visited by more than 3 million people."
        #   , "container": "a container made of glass or clay that is used for storing food, especially liquids."
        #   , "Bottle":"a glass or plastic container with a narrow neck, used for storing drinks or other liquids."
        #   }
        
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
        print("Our algorithm consider that it {} with {} percent".format(result, score[classes.index(result)]*100))




class TestCamera(MDApp):
    #textL = {"Baiterek": "Baiterek is a monument and observation tower in Nur-Sultan, the capital city of Kazakhstan. A tourist attraction popular with foreign visitors and Kazakhstanis, it is emblematic of the city, which became capital of the country in 1997.",
    #         "Expo": "Exhibition Expo-2017 – was held in the capital of Kazakhstan, Nur-Sultan cityfrom June 10 to September 10, 2017. 115 states and 22 international organizations took part in it. The exhibition was visited by more than 3 million people."
    #       }
    #image ="IMG_0.png"
    #text = textL["Expo"]
    def build(self):
        return Builder.load_file("Guidance.kv")


TestCamera().run()
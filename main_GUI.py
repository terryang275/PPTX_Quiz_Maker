from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.properties import ObjectProperty
from kivy.uix.actionbar import ActionItem
from kivy.uix.boxlayout import BoxLayout


#Uploading Files Library
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.factory import Factory
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
import os


from kivymd.uix.navigationdrawer import NavigationDrawerIconButton
#from kivymd.uix import toolbar
from kivymd.uix.button import MDIconButton, MDFloatingActionButton
from kivymd.uix.toolbar import MDToolbar
from kivymd.theming import ThemeManager
from kivymd.toast import toast



#Builder lets us use KV file no matter what
kv = Builder.load_file("flashcard.kv")

class MainWindow(Screen):
    def select(self, *args): 
        try: self.label.text = args[1][0] 
        except: pass


class Decks(Screen):
    #self.available_decks = {}
    #def display_decks():
    
    #Select deck

    #Display Altered text in one section of grid

    #loop through Length of [answer]:

        #find "___", replace with input temporarily

        #move to next word

        #Store into variable[]
    #for loop to length of answer:
        #compare each element of answer to the user response
        #Calculate % correct
        #Store % Correctlness back into question

    pass

class Add_Deck(Screen):
    #self.name = ""
    #self.data = {}

    #Choose File using File Choser

    #Name file of deck

    #Convert file from PPTX to dictionary

    #Store dictionary into Self.data

    #Upload Self.data to Deck.available_Decks
    #Decks.available_decks[self.name] = self.data
    pass

class Delete_Deck(Screen):
    #self.name = ""

    #get name of deck to delete

    #looks up name in the Decks_available

    #remove from decks_available
    pass



class Reports(Screen):
    pass

class Our_Team(Screen):
    pass

class WindowManager(ScreenManager):
    pass


class FlashCardApp(App):
    theme_cls = ThemeManager()
    def build(self):
        return kv

if __name__ == "__main__":
    FlashCardApp().run()


from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.button import Button

class TestApp(App):
  def build(self):
    return Button(text = "hello")
TestApp().run()
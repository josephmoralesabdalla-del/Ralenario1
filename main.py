from kivy.app import App
from kivy.uix.label import Label

class RaleniorApp(App):
    def build(self):
        return Label(text="Hola Mundo desde Ralenior 1")

if __name__ == "__main__":
    RaleniorApp().run()

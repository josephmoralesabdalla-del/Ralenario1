from kivy.app import App
from kivy.uix.label import Label

class Ralenario1App(App):
    def build(self):
        return Label(text="Hello NEXX World!")

if __name__ == "__main__":
    Ralenario1App().run()

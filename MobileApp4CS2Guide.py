from kivymd.app import MDApp
from kivymd.uix.label import MDLabel


class MobileApp4CS2Guide(MDApp):
    def build(self):
        return MDLabel(text="Hello, World", halign="center")


MobileApp4CS2Guide().run()
from kivymd.app import MDApp
from kivy.factory import Factory

from kivy.lang import Builder

Factory.register("TextField", module="textfield")


# print(hasattr(Factory, "TextField"))

app = MDApp()
kv = Builder.load_string("""
TextField:
    hint_text: "Choose a username"
""")
app.root = kv
app.run()
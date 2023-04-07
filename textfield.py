from kivy.core.text import DEFAULT_FONT
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import StringProperty, NumericProperty, ColorProperty, BooleanProperty, ObjectProperty, \
    OptionProperty
from kivy.lang import Builder

from kivymd.uix.button import MDIconButton


Builder.load_file("textfield.kv")


class TextField(MDBoxLayout):
    hint_text = StringProperty()
    text = StringProperty()
    icon_left_size = NumericProperty("35sp")
    cursor_color = ColorProperty("black")
    font_size = NumericProperty("35sp")
    multiline = BooleanProperty(False)
    input_filter = ObjectProperty(None, allownone=True)
    font_name = StringProperty(DEFAULT_FONT)
    input_type = OptionProperty('null', options=('null', 'text', 'number',
                                                 'url', 'mail', 'datetime',
                                                 'tel', 'address'))
    password = BooleanProperty(False)
    separator_height = NumericProperty("2dp")
    separator_color = ColorProperty("black")
    icon_left = StringProperty("account")
    icon_right = StringProperty("information-outline")
    icon_right_size = NumericProperty("24sp")


    def __init__(self, *args, **kwargs):
        self.register_event_type("on_icon_right_release")
        super().__init__(*args, **kwargs)

    def on_icon_right_release(self):
        pass




if __name__ == "__main__":
    from kivymd.app import MDApp

    app = MDApp()
    app.root = TextField(hint_text="Choose a username", on_icon_right_release=lambda _: print("hey don't click me", _))
    app.run()

from kivy.app import App
from kivy.uix.button import Button
from kivy.properties import NumericProperty, StringProperty


class TestButton(Button):
    counter = NumericProperty()
    say = StringProperty(force_dispatch=True)

    def __init__(self, **kwargs):
        self.register_event_type("on_click")
        super().__init__(**kwargs)

    def on_counter(self, *_):
        print(_[1])
        print(f"counter just updated to: {self.counter}")

    def on_say(self, insance, value):
        print(value)

    def on_click(self):
        print("I just clicked")

    def on_release(self):
        self.counter += 1
        self.say = "anything"
        self.dispatch("on_click")

app = App()
app.root = TestButton()
app.run()
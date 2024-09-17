from kivy.app import App
from kivy.graphics import Color, Rectangle
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.uix.stacklayout import StackLayout

from datetime import datetime

from schedule_display import bind_single


class WallClockDisplay(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.datetime = datetime(2023, 9, 11, 12, 0, 0)
        self.texture = Image(source='images/clock_image.png')

        with self.canvas:
            Color(255, 0, 255, 1)
            rect = Rectangle()
            bind_single(self, 'size', rect, 'size', lambda s: s)

        stack = StackLayout()
        stack.add_widget(self.texture)
        self.add_widget(stack)
        bind_single(self, 'size', stack, 'size', lambda s: s)



    def update_datetime(self, _timedelta):
        self.datetime = self.datetime + _timedelta

    def tick(self, dt):
        self.update_datetime(dt)



class MyApp(App):
    def build(self):
        clock = WallClockDisplay()
        return clock

if __name__ == '__main__':
    MyApp().run()

__all__ = ['WallClockDisplay']

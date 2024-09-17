from kivy.app import App
from kivy.graphics import Color, Rectangle
from kivy.clock import Clock
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.uix.floatlayout import  FloatLayout

from datetime import datetime, timedelta

from utensils import bind_single, Colors, create_rotated_rectangle

from clock_arm import ClockArm


class WallClockDisplay(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.datetime = datetime(2023, 9, 11, 12, 0, 0)
        self.clock_image = Image(source='images/clock_image.png')
        self.clock_arm_hour = ClockArm(size=(50, 350))
        self.clock_arm_minute = ClockArm(size=(30, 400))
        self.clock_arm_second = ClockArm(size=(10, 450))


        with self.canvas:
            Color(1, 0, 1, 1)
            rect = Rectangle()
            bind_single(self, 'size', rect, 'size', lambda s: s)

        layout = FloatLayout()
        layout.add_widget(self.clock_image)
        layout.add_widget(self.clock_arm_hour.get_widget())
        layout.add_widget(self.clock_arm_minute.get_widget())
        layout.add_widget(self.clock_arm_second.get_widget())
        self.add_widget(layout)
        bind_single(self, 'size', layout, 'size', lambda s: s)

    def update_datetime(self, _timedelta):
        self.datetime = self.datetime + _timedelta

    def tick(self, dt):
        dt *= 100
        self.update_datetime(timedelta(seconds=dt))
        self.clock_arm_hour.set_angle(self.datetime.hour * 30 + self.datetime.minute * 0.5)
        self.clock_arm_minute.set_angle(self.datetime.minute * 6)
        self.clock_arm_second.set_angle(self.datetime.second * 6)


if __name__ == '__main__':
    class MyApp(App):
        def build(self):
            clock = WallClockDisplay()
            Clock.schedule_interval(clock.tick, 1 / 144)
            return clock

    MyApp().run()

__all__ = ['WallClockDisplay']

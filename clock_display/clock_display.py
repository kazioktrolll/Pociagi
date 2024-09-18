from kivy.app import App
from kivy.clock import Clock
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.uix.relativelayout import RelativeLayout

from datetime import datetime, timedelta

from utensils import bind_single

if __name__ != "__main__": from .clock_arm import ClockArm


class WallClockDisplay(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.datetime = datetime(2023, 9, 11, 12, 5, 10)
        self.clock_image = Image(source='images/clock_image.png')
        self.clock_arm_hour = ClockArm(size=(50, 350))
        self.clock_arm_minute = ClockArm(size=(30, 400))
        self.clock_arm_second = ClockArm(size=(10, 450))


        layout = RelativeLayout(size=self.size)
        bind_single(self, 'size', layout, 'size', lambda s: s)
        self.add_widget(layout)
        layout.add_widget(self.clock_image)
        layout.add_widget(self.clock_arm_hour.get_widget())
        layout.add_widget(self.clock_arm_minute.get_widget())
        layout.add_widget(self.clock_arm_second.get_widget())
        bind_single(self, 'pos', layout, 'pos', lambda p: p)

    def update_datetime(self, _timedelta):
        self.datetime = self.datetime + _timedelta

    def tick(self, dt):
        dt *= 100
        self.update_datetime(timedelta(seconds=dt))
        self.clock_arm_hour.set_angle(self.datetime.hour * 30 + self.datetime.minute * 0.5)
        self.clock_arm_minute.set_angle(self.datetime.minute * 6)
        self.clock_arm_second.set_angle(self.datetime.second * 6)


if __name__ == '__main__':
    from clock_arm import ClockArm
    class MyApp(App):
        def build(self):
            clock = WallClockDisplay()
            Clock.schedule_interval(clock.tick, 1 / 144)
            return clock

    MyApp().run()

__all__ = ['WallClockDisplay']

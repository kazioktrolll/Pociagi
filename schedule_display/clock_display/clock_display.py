from kivy.app import App
from kivy.clock import Clock
from kivy.uix.image import Image
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.widget import Widget

from utensils import bind_single

if __name__ != "__main__": from .clock_arm import ClockArm


class WallClockDisplay(Widget):
    def __init__(self, database, **kwargs):
        super().__init__(**kwargs)
        self.database = database
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

    def tick(self, dt):
        current_time = self.database.get_time()
        self.clock_arm_hour.set_angle(current_time.hour * 30 + current_time.minute * 0.5)
        self.clock_arm_minute.set_angle(current_time.minute * 6)
        self.clock_arm_second.set_angle(current_time.second * 6)


if __name__ == '__main__':
    from clock_arm import ClockArm
    from database import Database


    class MyApp(App):
        def build(self):
            clock = WallClockDisplay(Database())
            Clock.schedule_interval(clock.tick, 1 / 144)
            Clock.schedule_interval(clock.database.tick, 1 / 144)
            return clock


    MyApp().run()

__all__ = ['WallClockDisplay']

from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window

from schedule_display import ScheduleDisplay


class MyApp(App):
    def __init__(self, **kwargs):
        super(MyApp, self).__init__(**kwargs)
        self.app_screen = ScheduleDisplay()

    def build(self):
        Window.maximize()
        Clock.schedule_interval(self.tick, 1/144)
        return self.app_screen

    def tick(self, dt):
        self.app_screen.tick(dt)


if __name__ == '__main__':
    MyApp().run()

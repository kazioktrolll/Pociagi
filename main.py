from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window

from schedule_display import ScheduleDisplay, TrainDisplay

from datetime import datetime


class MyApp(App):
    def __init__(self, **kwargs):
        super(MyApp, self).__init__(**kwargs)
        self.app_screen = ScheduleDisplay()

        self.app_screen.queue_train(TrainDisplay(
            czas=datetime(2024, 9, 11, 8, 3), do=".", przez=",", peron="!"))
        self.app_screen.queue_train(TrainDisplay(
            czas=datetime(2024, 9, 11, 8, 15), do="Praha", przez="Cokolwiek", peron="2"))
        self.app_screen.queue_train(TrainDisplay(
            czas=datetime(2024, 9, 11, 8, 47), do="Gdynia Główna", przez="Nie wiem", peron="3"))
        self.app_screen.queue_train(TrainDisplay(
            czas=datetime(2024, 9, 11, 8, 58), do="Katowice", przez="Test, Test, Test", peron="1"))

    def build(self):
        Window.maximize()
        Clock.schedule_interval(self.tick, 1/144)
        return self.app_screen

    def tick(self, dt):
        self.app_screen.tick(dt)


if __name__ == '__main__':
    MyApp().run()

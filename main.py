from kivy.app import App
from kivy.core.window import Window

from schedule_display import ScheduleDisplay



class MyApp(App):
    def build(self):
        app_screen = ScheduleDisplay()
        Window.maximize()
        return app_screen


if __name__ == '__main__':
    MyApp().run()
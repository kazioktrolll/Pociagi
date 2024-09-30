from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse

from utensils import Colors
from schedule_display import ScheduleDisplay


class Station(Widget):
    def __init__(self, database, pos, name):
        super().__init__(pos=pos, size_hint=(None, None), size=(30, 30))

        self.database = database
        self.schedule_display = ScheduleDisplay(database)
        self.__name = name

        with self.canvas:
            Color(*Colors.white)
            Ellipse(size=self.size, pos=(self.x - self.width // 2, self.y - self.height // 2))

    def tick(self, dt):
        self.schedule_display.tick(dt)

    @property
    def name(self):
        return self.__name

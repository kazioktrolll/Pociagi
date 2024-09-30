from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse

from utensils import Colors
from schedule_display import ScheduleDisplay


class Station(Widget):
    def __init__(self, database, pos):
        super().__init__(pos=pos, size_hint=(None, None), size=(30, 30))

        self.database = database
        self.schedule_display = ScheduleDisplay(database)

        with self.canvas:
            Color(*Colors.white)
            Ellipse(size=self.size, pos=(self.x - self.width // 2, self.y - self.height // 2))

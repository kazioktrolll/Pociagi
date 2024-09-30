from kivy.uix.widget import Widget
from database import Database
from datetime import timedelta
from schedule_display import ScheduleDisplay


class Station(Widget):
    def __init__(self, database: Database, pos: tuple[float, float]) -> None:
        self.schedule_display: ScheduleDisplay
        ...

    def tick(self, dt: timedelta) -> None: ...
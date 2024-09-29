from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.image import Image

from datetime import datetime, timedelta
from database import Database


class WallClockDisplay(Widget):
    def __init__(self,database: Database, **kwargs):
        super().__init__(**kwargs)
        self.texture: Image

    def tick(self, dt: int) -> None: ...


class MyApp(App):
    def build(self) -> WallClockDisplay: ...

__all__: list[str]

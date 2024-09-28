from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.image import Image

from datetime import datetime, timedelta


class WallClockDisplay(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.datetime: datetime
        self.texture: Image


    def update_datetime(self, _timedelta: timedelta) -> None: ...

    def get_datetime(self) -> datetime: ...

    def tick(self, dt: int) -> None: ...


class MyApp(App):
    def build(self) -> WallClockDisplay: ...

__all__: list[str]

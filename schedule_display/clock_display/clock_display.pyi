from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.widget import Widget

from database import Database


class WallClockDisplay(Widget):
    def __init__(self, database: Database, **kwargs):
        super().__init__(**kwargs)
        self.texture: Image

    def tick(self, dt: int) -> None: ...


class MyApp(App):
    def build(self) -> WallClockDisplay: ...


__all__: list[str]

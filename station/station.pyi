from kivy.uix.widget import Widget
from database import Database


class Station(Widget):
    def __init__(self, database: Database, pos: tuple[float, float]) -> None: ...

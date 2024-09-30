from kivy.uix.widget import Widget
from database import Database


class Connection(Widget):
    def __init__(self, station_A_name: str, station_B_name: str,
                 database: Database) -> None: ...

    @property
    def len(self) -> float: ...

from datetime import timedelta

from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.widget import Widget

from train import Train


class Map(Widget):
    def __init__(self, **kwargs) -> None:
        self.stations: dict[str, Station]
        self.trains: dict[str, Train]
        self.center_layout: RelativeLayout

    def tick(self, dt: timedelta) -> None: ...

    def add_train(self, name: str, path: list[str]) -> None: ...

    def add_station(self, name: str, pos: tuple[int, int]) -> None: ...

    def connect_stations(self, station_1_name: str, station_2_name: str) -> None: ...

    def update_connections(self) -> None: ...

    def on_touch_down(self, touch) -> None: ...


class Station(Widget):
    def __init__(self, **kwargs) -> None: ...

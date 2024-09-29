from datetime import datetime, timedelta

from kivy.uix.stacklayout import StackLayout
from kivy.uix.widget import Widget

from map import Station


class TrainDisplay(StackLayout):
    height: int

    def __init__(self, czas: datetime, do: str, przez: str, peron: str, **kwargs) -> None:
        super().__init__()
        self.bind: super().bind
        ...


class StationsPathIterator(object):
    def __init__(self, path: list[str], stations: dict[str, Station]) -> None:
        ...

    def __iter__(self) -> StationsPathIterator: ...

    def __next__(self) -> Station: ...


class Train(Widget):
    def __init__(self, name: str, path: list[str], stations_dict: dict[str, Station]) -> None:
        self.name: str
        self.path_by_stations: list[str]
        self.path_by_points: list[tuple[int, int]]
        self.speed: int

    def tick(self, dt: timedelta) -> None: ...

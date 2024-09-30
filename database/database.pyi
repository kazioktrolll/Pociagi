from datetime import datetime, timedelta
from station import Station
from train import Train


class Database:
    def __init__(self) -> None:
        self.__datetime: datetime = None
        self.connections: list[tuple[str, str]] = None
        self.stations: dict[str, Station] = None
        self.trains: dict[str, Train] = None

    def tick(self, dt: timedelta) -> None: ...

    @classmethod
    def timespan_real_to_simulated(cls, time: int) -> timedelta: ...

    def get_time(self) -> datetime: ...

    def add_train(self, name: str, path: list[str]) -> None: ...

    def add_station(self, name: str, pos: tuple[float, float]) -> None: ...

    def get_station(self, name: str) -> Station: ...

    def connect_stations(self, station_1_name: str, station_2_name: str) -> None: ...

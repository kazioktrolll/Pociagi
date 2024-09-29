from datetime import datetime, timedelta


class Database:
    def __init__(self) -> None:
        self.datetime: datetime = None

    def tick(self, dt: timedelta) -> None: ...

    @classmethod
    def timespan_real_to_simulated(cls, time: int) -> timedelta: ...

    def get_time(self) -> datetime: ...

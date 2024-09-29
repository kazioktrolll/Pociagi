from datetime import datetime, timedelta


class Database:
    def __init__(self):
        self.datetime = datetime(2024, 9, 11, 8, 5, 10)

    def tick(self, dt):
        self.datetime += dt

    @staticmethod
    def timespan_real_to_simulated(time):
        return timedelta(seconds=time * 100)

    def get_time(self):
        return self.datetime


__all__ = ['Database']

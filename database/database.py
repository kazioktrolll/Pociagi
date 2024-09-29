from datetime import datetime, timedelta

class Database:
    def __init__(self):
        self.datetime = datetime(2024, 9, 11, 8, 5, 10)

    def tick(self, dt):
        self.datetime += timedelta(seconds=self.time_real_to_ingame(dt))

    def time_real_to_ingame(self, time):
        return time * 100

    def get_time(self):
        return self.datetime


__all__ = ['Database']

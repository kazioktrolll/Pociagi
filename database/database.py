from datetime import datetime, timedelta
from train import Train
from station import Station
from connection import Connection


class Database:
    def __init__(self):
        self.__datetime = datetime(2024, 9, 11, 8, 5, 10)
        self.connections = {}
        self.stations = {}
        self.trains = {}

    def tick(self, dt):
        self.__datetime += dt

        for tickable in (self.trains | self.stations).values():
            tickable.tick(dt)

    @staticmethod
    def timespan_real_to_simulated(time):
        return timedelta(seconds=time * 100)

    def get_time(self):
        return self.__datetime


    def add_train(self, name, path):
        train = Train(name, path, self.stations)
        self.trains[name] = train

    def add_station(self, name, pos):
        s = Station(database=self, pos=pos, name=name)
        self.stations[name] = s

    def get_station(self, name):
        return self.stations[name]

    def connect_stations(self, station_1_name, station_2_name):
        name = station_1_name + '-' + station_2_name
        con = Connection(station_1_name, station_2_name, self)
        self.connections[name] = con


__all__ = ['Database']

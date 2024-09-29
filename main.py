from datetime import datetime

from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window

from database import Database
from map import Map
from schedule_display import ScheduleDisplay
from train import TrainDisplay


class MyApp(App):
    def __init__(self, **kwargs):
        super(MyApp, self).__init__(**kwargs)
        self.database = Database()
        self.app_screen = ScheduleDisplay(self.database)
        self.train_map = Map()

        def setup_schedule_display():
            self.app_screen.queue_train(TrainDisplay(
                czas=datetime(2024, 9, 11, 8, 3), do=".", przez=",", peron="!"))
            self.app_screen.queue_train(TrainDisplay(
                czas=datetime(2024, 9, 11, 8, 15), do="Praha", przez="Cokolwiek", peron="2"))
            self.app_screen.queue_train(TrainDisplay(
                czas=datetime(2024, 9, 11, 8, 47), do="Gdynia Główna", przez="Nie wiem", peron="3"))
            self.app_screen.queue_train(TrainDisplay(
                czas=datetime(2024, 9, 11, 8, 58), do="Katowice", przez="Test, Test, Test", peron="1"))

        def setup_map():
            self.train_map.add_station('A', (0, 0))
            self.train_map.add_station('D', (200, 50))
            self.train_map.add_station('C', (0, 300))
            self.train_map.add_station('B', (100, 100))

            self.train_map.connect_stations('A', 'B')
            self.train_map.connect_stations('A', 'C')
            self.train_map.connect_stations('A', 'D')
            self.train_map.connect_stations('B', 'C')
            self.train_map.connect_stations('B', 'D')
            self.train_map.connect_stations('C', 'D')

            self.train_map.add_train('1', ['A', 'B', 'C'])
            self.train_map.add_train('2', ['A', 'B', 'D'])
            self.train_map.add_train('3', ['A', 'C', 'B'])
            self.train_map.add_train('4', ['A', 'C', 'D'])
            self.train_map.add_train('5', ['A', 'D', 'B'])
            self.train_map.add_train('6', ['A', 'D', 'C'])
            self.train_map.add_train('7', ['B', 'A', 'C'])
            self.train_map.add_train('8', ['B', 'A', 'D'])
            self.train_map.add_train('9', ['B', 'C', 'A'])

            Clock.schedule_interval(self.train_map.tick, 1 / 144)
            return self.train_map

        setup_schedule_display()
        setup_map()

    def build(self):
        Window.maximize()
        Clock.schedule_interval(self.tick, 1 / 144)
        #return self.app_screen
        return self.train_map

    def tick(self, dt):
        dt = Database.timespan_real_to_simulated(dt)
        self.app_screen.tick(dt)
        self.database.tick(dt)
        self.train_map.tick(dt)


if __name__ == '__main__':
    MyApp().run()

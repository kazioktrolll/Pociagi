from datetime import datetime
from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from database import Database
from map import Map
from train import TrainDisplay
from kivy.uix.boxlayout import BoxLayout


class MyApp(App):
    def __init__(self, **kwargs):
        super(MyApp, self).__init__(**kwargs)
        self.database = Database()
        self.train_map = Map(self.database)
        self.layout = BoxLayout(orientation='horizontal')

        def setup_map():
            self.database.add_station('A', (0, 0))
            self.database.add_station('D', (200, 0))
            self.database.add_station('C', (0, 300))
            self.database.add_station('B', (70, 70))

            self.database.connect_stations('A', 'B')
            self.database.connect_stations('A', 'C')
            self.database.connect_stations('A', 'D')
            self.database.connect_stations('B', 'C')
            self.database.connect_stations('B', 'D')
            self.database.connect_stations('C', 'D')

            self.database.add_train('1', ['A', 'B', 'C'])
            self.database.add_train('2', ['A', 'B', 'D'])
            self.database.add_train('3', ['A', 'C', 'B'])
            self.database.add_train('4', ['A', 'C', 'D'])
            self.database.add_train('5', ['A', 'D', 'B'])
            self.database.add_train('6', ['A', 'D', 'C'])
            self.database.add_train('7', ['B', 'A', 'C'])
            self.database.add_train('8', ['B', 'A', 'D'])
            self.database.add_train('9', ['B', 'C', 'A'])

            self.train_map.update_widgets()

        setup_map()
        self.app_screen = self.database.get_station('A').schedule_display

        def setup_schedule_display():
            self.app_screen.queue_train(TrainDisplay(
                czas=datetime(2024, 9, 11, 8, 3), do=".", przez=",", peron="!"))
            self.app_screen.queue_train(TrainDisplay(
                czas=datetime(2024, 9, 11, 8, 15), do="Praha", przez="Cokolwiek", peron="2"))
            self.app_screen.queue_train(TrainDisplay(
                czas=datetime(2024, 9, 11, 8, 47), do="Gdynia Główna", przez="Nie wiem", peron="3"))
            self.app_screen.queue_train(TrainDisplay(
                czas=datetime(2024, 9, 11, 8, 58), do="Katowice", przez="Test, Test, Test", peron="1"))

        setup_schedule_display()

        def setup_display():
            self.train_map.size_hint=(.25, 1)
            self.app_screen.size_hint=(.75, 1)

            self.layout.add_widget(self.train_map)
            self.layout.add_widget(self.app_screen)

        setup_display()

    def build(self):
        Window.maximize()
        Clock.schedule_interval(self.tick, 1 / 144)
        return self.layout

    def tick(self, _dt):
        dt = Database.timespan_real_to_simulated(_dt)
        self.app_screen.tick(dt)
        self.database.tick(dt)


if __name__ == '__main__':
    MyApp().run()

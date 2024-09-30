from kivy.graphics import Rectangle, Color, Line
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.widget import Widget

from utensils import bind_single, Colors
from datetime import timedelta


class Map(Widget):
    def __init__(self, database, **kwargs):
        super().__init__(**kwargs)
        self.database = database

        self.center_layout = RelativeLayout(size=(0, 0), center=self.center)
        bind_single(self, 'center', self.center_layout, 'center', lambda c: c)
        self.add_widget(self.center_layout)

        self.connections_layout = RelativeLayout()
        self.center_layout.add_widget(self.connections_layout)
        self.stations_layout = RelativeLayout()
        self.center_layout.add_widget(self.stations_layout)
        self.trains_layout = RelativeLayout()
        self.center_layout.add_widget(self.trains_layout)

        def draw():
            with self.canvas.before:
                Color(*Colors.light_blue)
                rec = Rectangle(pos=(0, 0), size=(self.width, self.height))
                bind_single(self, 'size', rec, 'size', lambda s: s)

        draw()

    def on_touch_down(self, _):
        # used only as a breakpoint for debugging
        pass

    def update_widgets(self):
        self.trains_layout.clear_widgets()
        self.stations_layout.clear_widgets()
        self.connections_layout.clear_widgets()

        for train in self.database.trains.values():
            self.trains_layout.add_widget(train)

        for station in self.database.stations.values():
            self.stations_layout.add_widget(station)

        self.__update_connections()

    def __update_connections(self):
        self.connections_layout.canvas.clear()
        for connection in self.database.connections:
            points = list(self.database.stations[connection[0]].pos + self.database.stations[connection[1]].pos)
            with self.connections_layout.canvas:
                Color(*Colors.white)
                Line(points=points, width=4)


__all__ = ['Map']
"""
if __name__ == '__main__':
    from kivy.app import App
    from kivy.clock import Clock
    from database import Database

    class MyApp(App):
        def build(self):
            database = Database()
            train_map = Map(database)

            train_map.add_station('A', (0, 0))
            train_map.add_station('D', (200, 50))
            train_map.add_station('C', (-50, 300))
            train_map.add_station('B', (100, 100))

            train_map.connect_stations('A', 'B')
            train_map.connect_stations('B', 'C')
            train_map.connect_stations('B', 'D')

            train_map.add_train('1', ['A', 'B', 'C'])
            train_map.add_train('2', ['A', 'B', 'D'])

            t = lambda dt: train_map.tick(timedelta(seconds=dt))
            Clock.schedule_interval(t, 1 / 144)
            return train_map


    MyApp().run()
"""
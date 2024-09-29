from kivy.graphics import Rectangle, Color, Ellipse, Line
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.widget import Widget

from train import Train
from utensils import bind_single, Colors


class Map(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.center_layout = RelativeLayout(size=(0, 0), center=self.center)
        bind_single(self, 'center', self.center_layout, 'center', lambda c: c)
        self.add_widget(self.center_layout)

        self.connections = []
        self.connections_layout = RelativeLayout()
        self.center_layout.add_widget(self.connections_layout)
        self.stations = {}
        self.stations_layout = RelativeLayout()
        self.center_layout.add_widget(self.stations_layout)
        self.trains = {}
        self.trains_layout = RelativeLayout()
        self.center_layout.add_widget(self.trains_layout)

        def draw():
            with self.canvas.before:
                Color(*Colors.light_blue)
                rec = Rectangle(pos=(0, 0), size=(self.width, self.height))
                bind_single(self, 'size', rec, 'size', lambda s: s)

        draw()

    def tick(self, dt):
        for train in self.trains.values():
            train.tick(dt)

    def add_train(self, name, path):
        train = Train(name, path, self.stations)
        self.trains[name] = train
        self.trains_layout.add_widget(train)

    def add_station(self, name, pos):
        s = Station(pos=pos)
        self.stations[name] = s
        self.stations_layout.add_widget(s)

    def on_touch_down(self, touch):
        # used only as a breakpoint for debugging
        pass

    def connect_stations(self, station_1_name, station_2_name):
        self.connections.append((station_1_name, station_2_name))
        self.update_connections()

    def update_connections(self):
        self.connections_layout.canvas.clear()
        for connection in self.connections:
            points = list(self.stations[connection[0]].pos + self.stations[connection[1]].pos)
            with self.connections_layout.canvas:
                Color(*Colors.white)
                Line(points=points, width=4)


class Station(Widget):
    def __init__(self, pos):
        super().__init__(pos=pos, size_hint=(None, None), size=(30, 30))

        with self.canvas:
            Color(*Colors.white)
            Ellipse(size=self.size, pos=(self.x - self.width // 2, self.y - self.height // 2))


__all__ = ['Map']

if __name__ == '__main__':
    from kivy.app import App
    from kivy.clock import Clock


    class MyApp(App):
        def build(self):
            train_map = Map()

            train_map.add_station('A', (0, 0))
            train_map.add_station('D', (200, 50))
            train_map.add_station('C', (-50, 300))
            train_map.add_station('B', (100, 100))

            train_map.connect_stations('A', 'B')
            train_map.connect_stations('B', 'C')
            train_map.connect_stations('B', 'D')

            train_map.add_train('1', ['A', 'B', 'C'])
            train_map.add_train('2', ['A', 'B', 'D'])

            Clock.schedule_interval(train_map.tick, 1 / 144)
            return train_map


    MyApp().run()

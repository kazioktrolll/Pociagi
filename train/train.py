from kivy.uix.stacklayout import StackLayout
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Color
from kivy.clock import Clock

from utensils import bind_single, Colors, ClippedLabel


light_blue = Colors.light_blue
black = Colors.black
white = Colors.white


class TrainDisplay(StackLayout):
    height = 20
    def __init__(self, **kwargs):
        super().__init__()

        self.orientation = 'lr-tb'
        self.size_hint = (1, None)
        self.height = TrainDisplay.height

        self.czas = kwargs['czas']
        self.do = kwargs['do']
        self.przez = kwargs['przez']
        self.peron = kwargs['peron']

        # Draw background
        with self.canvas:
            Color(*light_blue)
            rect = Rectangle(pos=self.pos, size=(self.width, self.height))
        bind_single(self, 'pos', rect, 'pos',
                    lambda pos: (pos[0] + 3, pos[1] + 3))
        bind_single(self, 'size', rect, 'size',
                    lambda size: (size[0] - 6, size[1] - 6))

        # Create Labels
        czas_label  = ClippedLabel(text=self.czas.strftime("%H:%M"),  font_size="40px", color=black, size_hint=(None, 1))
        do_label    = ClippedLabel(text=self.do,    font_size="40px", color=white, size_hint=(None, 1))
        padding     = ClippedLabel(                                                size_hint=(None, 1))
        peron_label = ClippedLabel(text=self.peron, font_size="40px", color=white, size_hint=(None, 1))
        przez_label = ClippedLabel(text=self.przez, font_size="40px", color=white, size_hint=(None, 1))


        def do_after_build(_):
            czas_label.width = 110
            do_label.width = do_label.texture.width + 20 if do_label.texture.width < 280 else 300
            padding.width = 300 - do_label.width
            peron_label.width = 50
            bind_single(self, 'width', przez_label, 'width', lambda width: width - 460)

        self.add_widget(czas_label)
        self.add_widget(do_label)
        self.add_widget(padding)
        self.add_widget(przez_label)
        self.add_widget(peron_label)
        Clock.schedule_once(do_after_build)


class StationsPathIterator(object):
    def __init__(self, path, stations):
        self.path = path
        self.stations = stations
        self.forward = True
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        station = self.stations[self.path[self.current]]
        self.current += 1 if self.forward else -1
        if self.current == len(self.path) - 1 or self.current == 0:
            self.forward = not self.forward
        return station


class Train(Widget):
    def __init__(self, name, path, stations_dict):
        super().__init__(pos=(0, 0), size_hint=(None, None), size=(10, 20))

        self.name = name
        self.path_by_stations = path
        self.stations_dict = {k: v for k, v in stations_dict.items() if k in path}

        self.path_by_points: list[tuple[int, int]] = [stations_dict[st].pos for st in self.path_by_stations]
        self.speed = 50 #pixels per second

        self.stations_iterator = StationsPathIterator(path, self.stations_dict)
        self.current_station = next(self.stations_iterator)
        self.next_station = next(self.stations_iterator)

        with self.canvas:
            Color(*black)
            rec = Rectangle(pos=(self.x - self.width // 2, self.y - self.height // 2), size=self.size)
            bind_single(self, 'pos', rec, 'pos',
                        lambda p: (p[0] - self.width // 2, p[1] - self.height // 2))

    def tick(self, dt):
        position_difference = (self.next_station.x - self.x, self.next_station.y - self.y)
        distance = (position_difference[0] ** 2 + position_difference[1] ** 2) ** 0.5
        direction = (position_difference[0] / distance, position_difference[1] / distance)

        delta_pos = (direction[0] * self.speed * dt, direction[1] * self.speed * dt)
        delta_pos_distance = (delta_pos[0] ** 2 + delta_pos[1] ** 2) ** 0.5

        if self.current_station:
            self.current_station = None

        if delta_pos_distance < distance:
            self.pos = (self.x + delta_pos[0], self.y + delta_pos[1])
        else:
            self.pos = self.next_station.pos
            self.current_station = self.next_station
            self.next_station = next(self.stations_iterator)




__all__ = ['TrainDisplay', 'Train']

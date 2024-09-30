from kivy.uix.widget import Widget
from kivy.graphics import Color, Line
from utensils import Colors, get_length


class Connection(Widget):
    def __init__(self,station_A_name, station_B_name, database):
        super().__init__(size_hint=(None, None))
        self.__station_A = database.get_station(station_A_name)
        self.__station_B = database.get_station(station_B_name)

        def draw():
            points = list(self.__station_A.pos + self.__station_B.pos)
            with self.canvas:
                Color(*Colors.white)
                Line(points=points, width=4)
        draw()

    @property
    def len(self):
        vector = (self.__station_A.x - self.__station_B.x, self.__station_A.y - self.__station_B.y)
        return get_length(vector)

from kivy.app import App
from kivy.graphics import Color, Ellipse
from kivy.uix.widget import Widget

from utensils import create_rotated_rectangle


class MyWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        center = self.center
        self.size_hint = (None, None)
        self.size = (1000, 1000)

        with self.canvas:
            Color(0, 0, 0, 1)
            Ellipse(pos=(0, 0), size=(1000, 1000))
        with self.canvas:
            Color(255, 255, 255, 1)
            Ellipse(pos=(25, 25), size=(950, 950))
        with self.canvas:
            Color(0, 0, 0, 1)

            radius = 400
            rect_width = 30
            rect_height = 100
            for i in range(12):
                angle_deg = i * 30  # Each strip is 30 degrees apart
                create_rotated_rectangle(angle_deg, rect_width, rect_height, radius, center)

            radius = 400
            rect_width = 10
            rect_height = 40
            for i in range(60):
                angle_deg = i * 6  # Each strip is 6 degrees apart
                create_rotated_rectangle(angle_deg, rect_width, rect_height, radius, center)

        self.export_to_png("../../images/clock_image.png")


class MyApp(App):
    def build(self):
        return MyWidget()


if __name__ == '__main__':
    MyApp().run()

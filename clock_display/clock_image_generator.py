from math import radians, sin, cos

from kivy.app import App
from kivy.graphics import Color, Ellipse, PushMatrix, Rectangle, Rotate, PopMatrix
from kivy.uix.widget import Widget


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

            center_x, center_y = center
            radius = 400
            rect_width = 30
            rect_height = 100
            for i in range(12):
                angle_deg = i * 30  # Each strip is 30 degrees apart
                angle_rad = radians(angle_deg)

                # Calculate rectangle position along the circle
                rect_x = center_x + radius * cos(angle_rad) - rect_width / 2
                rect_y = center_y + radius * sin(angle_rad) - rect_height / 2

                # Apply rotation to face towards the center
                PushMatrix()
                Rotate(angle=angle_deg + 90,
                       origin=(rect_x + rect_width / 2, rect_y + rect_height / 2))  # Rotate rectangle

                # Draw the rectangle
                Rectangle(pos=(rect_x, rect_y), size=(rect_width, rect_height))

                PopMatrix()  # Restore transformation matrix

            center_x, center_y = center
            radius = 400
            rect_width = 10
            rect_height = 40
            for i in range(60):
                angle_deg = i * 6  # Each strip is 30 degrees apart
                angle_rad = radians(angle_deg)

                # Calculate rectangle position along the circle
                rect_x = center_x + radius * cos(angle_rad) - rect_width / 2
                rect_y = center_y + radius * sin(angle_rad) - rect_height / 2

                # Apply rotation to face towards the center
                PushMatrix()
                Rotate(angle=angle_deg + 90,
                       origin=(rect_x + rect_width / 2, rect_y + rect_height / 2))  # Rotate rectangle

                # Draw the rectangle
                Rectangle(pos=(rect_x, rect_y), size=(rect_width, rect_height))

                PopMatrix()  # Restore transformation matrix

        self.export_to_png("../images/clock_image.png")


class MyApp(App):
    def build(self):
        return MyWidget()

if __name__ == '__main__':
    MyApp().run()
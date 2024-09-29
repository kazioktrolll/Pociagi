from kivy.clock import Clock
from kivy.graphics import Color
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout

from utensils import create_rotated_rectangle


class ClockArm(Widget):
    def __init__(self, size, color=(0, 0, 0, 1)):
        self.arm_size = size
        self.radius = (size[1] - size[0]) // 2
        self.color = color
        super().__init__()
        self.angle = -90
        self.size = (1000, 1000)
        self.image = Image()
        self.update()

    def update(self, _=None):
        with self.canvas:
            self.canvas.clear()
            Color(*self.color)
            create_rotated_rectangle(rect_angle_deg=self.angle,
                                     rect_width=self.arm_size[0],
                                     rect_height=self.arm_size[1],
                                     radius=self.radius, center=self.center)
        self.image.texture = self.export_as_image().texture

    def rotate(self, angle):
        self.angle = (self.angle + angle) % 360
        self.update()

    def set_angle(self, angle):
        self.angle = (angle - 90) % 360
        self.update()

    def get_widget(self):
        _return = FloatLayout()
        _return.add_widget(self.image)
        return _return


if __name__ == '__main__':
    from kivy.app import App


    class TestApp(App):
        def build(self):
            widget = Widget(size=(100, 100))
            arm = ClockArm(size=(50, 300), color=(0, 1, 0, 1))
            widget.add_widget(arm.get_widget())
            Clock.schedule_interval(lambda _: arm.rotate(6), 1)
            return widget


    TestApp().run()

__all__ = ['ClockArm']

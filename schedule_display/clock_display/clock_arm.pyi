from typing import Any

from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.widget import Widget


class ClockArm(Widget):
    def __init__(self, size: tuple[int, int], color: tuple[float, float, float, float] = ...):
        self.image: Image
        self.radius: int
        ...

    def update(self, _: Any = ...) -> None:
        ...

    def rotate(self, angle: float) -> None:
        ...

    def set_angle(self, angle: float) -> None:
        ...

    def get_widget(self) -> FloatLayout:
        ...


__all__: list[str]

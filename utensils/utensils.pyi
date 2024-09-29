from typing import Callable, Any
from kivy.uix.label import Label
from kivy.uix.stacklayout import StackLayout
from kivy.uix.stencilview import StencilView
from datetime import timedelta as td

Color = tuple[float, float, float, float]


class Colors(object):
    white: Color
    black: Color
    blue: Color
    light_blue: Color
    yellow: Color


def get_bind_lambda(target, value_name: str,
                    transform_lambda: Callable[[Any], Any]
                    ) -> Callable[[Any, Any], None]: ...


def bind_single(parent, parent_attr_name: str,
                child, child_attr_name: str,
                transform_lambda: Callable[[Any], Any]
                ) -> None: ...


class ClippedLabel(Label, StencilView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind: super().bind
        ...


class ClippedStackLayout(StackLayout, StencilView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind: super().bind
        ...


def create_rotated_rectangle(rect_angle_deg: float,
                             rect_width: int, rect_height: int,
                             radius: int, center: tuple[int, int]
                             ) -> None: ...


def get_length(vector: tuple[float, float]) -> float: ...


def normalize(vector: tuple[float, float]) -> tuple[float, float]: ...


__all__: list[str]

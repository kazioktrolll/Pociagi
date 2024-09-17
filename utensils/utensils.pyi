from kivy.uix.stacklayout import StackLayout
from kivy.uix.stencilview import StencilView
from kivy.uix.label import Label

from typing import Tuple, Callable, Any


Color = Tuple[float, float, float, float]


class Colors(object):
    white:         Color = None
    black:         Color = None
    blue:          Color = None
    light_blue:    Color = None
    yellow:        Color = None


def get_bind_lambda(target, value_name: str, transform_lambda: Callable[[Any], Any])\
        -> Callable[[Any, Any], None]: ...

def bind_single(parent, parent_attr_name: str, child, child_attr_name: str,
                transform_lambda: Callable[[Any], Any]) -> None: ...


class ClippedLabel(Label, StencilView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind = super().bind
        ...


class ClippedStackLayout(StackLayout, StencilView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind = super().bind
        ...


__all__ = ['ClippedLabel', 'ClippedStackLayout', 'bind_single', 'Colors']

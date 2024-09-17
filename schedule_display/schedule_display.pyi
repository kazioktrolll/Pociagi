from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.stacklayout import StackLayout
from kivy.graphics import Rectangle
from kivy.uix.stencilview import StencilView

from typing import Callable, Any

from datetime import datetime, timedelta


def get_bind_lambda(target, value_name: str,
                    transform_lambda: Callable[[Any], Any]) -> Callable[[Any, Any], None]: ...

def bind_single(parent, parent_attr_name: str,
                child,  child_attr_name: str,
                transform_lambda: Callable[[Any], Any]) -> None: ...

class ClippedLabel(Label, StencilView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind = super().bind

class ClippedStackLayout(StackLayout, StencilView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind = super().bind

class TrainDisplay(StackLayout):
    def __init__(self, **kwargs):
        super().__init__()
        self.bind = super().bind

        self.czas: str = None
        self.do: str = None
        self.przez: str = None
        self.peron: str = None
        ...


class ScheduleDisplay(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind = ...
        self.background: Rectangle = ...

        self.czas: str = ...
        self.do: str = ...
        self.przez: str = ...
        self.peron: str = ...

    def tick(self, dt: int) -> None: ...

    def on_touch_down(self, _) -> None: ...

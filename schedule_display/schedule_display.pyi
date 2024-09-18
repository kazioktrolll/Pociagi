from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.stacklayout import StackLayout
from kivy.uix.stencilview import StencilView


class ClippedLabel(Label, StencilView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind: super().bind

class ClippedStackLayout(StackLayout, StencilView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind: super().bind

class TrainDisplay(StackLayout):
    def __init__(self, **kwargs):
        super().__init__()
        self.bind: super().bind

        self.czas: str
        self.do: str
        self.przez: str
        self.peron: str
        ...


class ScheduleDisplay(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind: super().bind
        self.train_queue: list[TrainDisplay]

    def tick(self, dt: int) -> None: ...

    def on_touch_down(self, _) -> None: ...

__all__: list[str]

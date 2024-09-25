from datetime import datetime

from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.uix.stacklayout import StackLayout
from kivy.input.motionevent import MotionEvent


class TrainDisplay(StackLayout):
    height: int
    def __init__(self,czas:datetime, do:str, przez:str, peron:str, **kwargs):
        super().__init__()
        self.bind: super().bind
        ...


class ScheduleDisplay(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind: super().bind
        self.root_layout: FloatLayout
        self.train_layout: StackLayout

        self.train_queue: list[TrainDisplay]

    def tick(self, dt: int) -> None: ...

    def on_touch_down(self, touch: MotionEvent) -> bool: ...

    def queue_train(self, train: TrainDisplay) -> None: ...

    def update_trains_to_display(self) -> None: ...

__all__: list[str]

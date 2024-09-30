from datetime import timedelta

from kivy.input.motionevent import MotionEvent
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.widget import Widget

from database import Database
from train import TrainDisplay


class ScheduleDisplay(Widget):
    def __init__(self, database: Database, **kwargs):
        super().__init__(**kwargs)
        self.database: Database
        self.bind: super().bind
        self.root_layout: FloatLayout
        self.train_layout: StackLayout

        self.train_queue: list[TrainDisplay]

    def tick(self, dt: timedelta) -> None: ...

    def queue_train(self, train: TrainDisplay) -> None: ...

    def __update_trains_to_display(self) -> None: ...


__all__: list[str]

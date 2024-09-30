from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.widget import Widget
from database import Database


class Map(Widget):
    def __init__(self, database: Database, **kwargs) -> None:
        self.center_layout: RelativeLayout
        ...

    def update_widgets(self) -> None: ...

    def __update_connections(self) -> None: ...

    def on_touch_down(self, _) -> None: ...

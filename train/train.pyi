from kivy.uix.stacklayout import StackLayout
from datetime import datetime


class TrainDisplay(StackLayout):
    height: int
    def __init__(self,czas:datetime, do:str, przez:str, peron:str, **kwargs) -> None:
        super().__init__()
        self.bind: super().bind
        ...

class Train(object): ...

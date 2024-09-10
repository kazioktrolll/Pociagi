from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.stacklayout import StackLayout
from kivy.graphics import Color, Rectangle
from kivy.uix.stencilview import StencilView
from kivy.clock import Clock

from typing import Callable, Any


white = (1, 1, 1, 1)
black = (0, 0, 0, 1)
blue = (0.2, 0.4, 1, 1)
light_blue = (0.4, 0.6, 1, 1)
yellow = (1, 1, 0, 1)


def get_bind_lambda(target, value_name: str, transform_lambda: Callable[[Any], Any]):
    # Example: bind child size as parent size /2
    # target: child
    # value_name: 'size'
    # transform_lambda: lambda size: (size[0] // 2, size[1] // 2)
    bind_lambda = lambda instance, value: setattr(target, value_name, transform_lambda(value))
    return bind_lambda

def bind_single(parent, parent_attr_name: str, child, child_attr_name: str, transform_lambda: Callable[[Any], Any]):
    # Example: bind child y as .5 parent height
    # bind_single(parent, 'height', child, 'y', lambda h: h // 2
    parent.bind(**{parent_attr_name: get_bind_lambda(
        child, child_attr_name, transform_lambda
    )})


class ClippedLabel(Label, StencilView):
    def __init__(self, **kwargs):
        super(ClippedLabel, self).__init__(**kwargs)
        self.bind = super().bind


class TrainDisplay(StackLayout):
    def __init__(self, **kwargs):
        super(TrainDisplay, self).__init__()
        self.bind = super().bind

        self.orientation = 'lr-tb'
        self.size_hint = (1, None)
        self.height = 60

        self.czas: str = kwargs['czas']
        self.do: str = kwargs['do']
        self.przez: str = kwargs['przez']
        self.peron: str = kwargs['peron']

        # Draw background
        with self.canvas:
            Color(*light_blue)
            rect = Rectangle(pos=self.pos, size=(self.width, self.height))
        bind_single(self, 'pos', rect, 'pos',
                    lambda pos: (pos[0] + 3, pos[1] + 3))
        bind_single(self, 'size', rect, 'size',
                    lambda size: (size[0] - 6, size[1] - 6))

        # Create Labels
        czas_label =  ClippedLabel(text=self.czas,  font_size="40px", color=black, size_hint=(None, 1))
        do_label =    ClippedLabel(text=self.do,    font_size="40px", color=white, size_hint=(None, 1))
        padding =     ClippedLabel(                                                size_hint=(None, 1))
        peron_label = ClippedLabel(text=self.peron, font_size="40px", color=white, size_hint=(None, 1))
        przez_label = ClippedLabel(text=self.przez, font_size="40px", color=white, size_hint=(None, 1))


        def do_after_build(dt):
            czas_label.width = 110
            do_label.width = do_label.texture.width + 20 if do_label.texture.width < 280 else 300
            padding.width = 300 - do_label.width
            peron_label.width = 50
            bind_single(self, 'width', przez_label, 'width', lambda width: width - 460)

        self.add_widget(czas_label)
        self.add_widget(do_label)
        self.add_widget(padding)
        self.add_widget(przez_label)
        self.add_widget(peron_label)
        Clock.schedule_once(do_after_build)


class ScheduleDisplay(Widget):
    def __init__(self, **kwargs):
        super(ScheduleDisplay, self).__init__(**kwargs)
        self.bind = super().bind

        with self.canvas:
            Color(*blue)
            self.background = Rectangle(pos=(0, 0), size=(self.width, self.height))
            bind_single(self, 'size', self.background, 'size', lambda s: s)

        main_layout = StackLayout(orientation='tb-lr')
        bind_single(self, 'size', main_layout, 'size', lambda s: s)
        self.add_widget(main_layout)

        odjazdy_label = Label(text="Odjazdy", font_size="70px", color=yellow, size_hint=(1, None), height=200)
        main_layout.add_widget(odjazdy_label)

        naglowki_layout = StackLayout(orientation='lr-tb', size_hint=(1, None), height=50)
        main_layout.add_widget(naglowki_layout)

        czas_label  = Label(text="Czas",  font_size="30px", color=yellow, size_hint=(None, 1), width=100)
        do_label    = Label(text="Do",    font_size="30px", color=yellow, size_hint=(None, 1), width=100)
        peron_label = Label(text="Peron", font_size="30px", color=yellow, size_hint=(None, 1), width=120)
        przez_label = Label(text="Przez", font_size="30px", color=yellow, size_hint=(None, 1))

        bind_single(naglowki_layout, 'width', przez_label, 'width',
                    lambda width: width - czas_label.width - do_label.width - peron_label.width)

        naglowki_layout.add_widget(czas_label)
        naglowki_layout.add_widget(do_label)
        naglowki_layout.add_widget(przez_label)
        naglowki_layout.add_widget(peron_label)

        train_layout = StackLayout(orientation='tb-lr', size_hint=(1, None))
        bind_single(naglowki_layout, 'y', train_layout, 'height', lambda y: y)
        main_layout.add_widget(train_layout)

        train_layout.add_widget(TrainDisplay(
            czas='08:00', do=".", przez=",", peron="!"))
        train_layout.add_widget(TrainDisplay(
            czas='08:10', do="Praha", przez="Cokolwiek", peron="2"))
        train_layout.add_widget(TrainDisplay(
            czas='08:35', do="Gdynia Główna", przez="Nie wiem", peron="3"))
        train_layout.add_widget(TrainDisplay(
            czas='08:58', do="Katowice", przez="Test, Test, Test", peron="1"))

    def on_touch_down(self, _):
        pass
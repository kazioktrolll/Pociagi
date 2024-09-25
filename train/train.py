from kivy.uix.stacklayout import StackLayout
from kivy.graphics import Rectangle, Color
from kivy.clock import Clock

from utensils import bind_single, Colors, ClippedLabel


light_blue = Colors.light_blue
black = Colors.black
white = Colors.white


class TrainDisplay(StackLayout):
    height = 20
    def __init__(self, **kwargs):
        super().__init__()

        self.orientation = 'lr-tb'
        self.size_hint = (1, None)
        self.height = TrainDisplay.height

        self.czas = kwargs['czas']
        self.do = kwargs['do']
        self.przez = kwargs['przez']
        self.peron = kwargs['peron']

        # Draw background
        with self.canvas:
            Color(*light_blue)
            rect = Rectangle(pos=self.pos, size=(self.width, self.height))
        bind_single(self, 'pos', rect, 'pos',
                    lambda pos: (pos[0] + 3, pos[1] + 3))
        bind_single(self, 'size', rect, 'size',
                    lambda size: (size[0] - 6, size[1] - 6))

        # Create Labels
        czas_label  = ClippedLabel(text=self.czas.strftime("%H:%M"),  font_size="40px", color=black, size_hint=(None, 1))
        do_label    = ClippedLabel(text=self.do,    font_size="40px", color=white, size_hint=(None, 1))
        padding     = ClippedLabel(                                                size_hint=(None, 1))
        peron_label = ClippedLabel(text=self.peron, font_size="40px", color=white, size_hint=(None, 1))
        przez_label = ClippedLabel(text=self.przez, font_size="40px", color=white, size_hint=(None, 1))


        def do_after_build(_):
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

__all__ = ['TrainDisplay']

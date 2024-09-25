from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.stacklayout import StackLayout
from kivy.graphics import Color, Rectangle
from kivy.clock import Clock

from utensils import bind_single, ClippedLabel, ClippedStackLayout, Colors

from clock_display import WallClockDisplay

white = Colors.white
black = Colors.black
yellow = Colors.yellow
blue = Colors.blue
light_blue = Colors.light_blue


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


class ScheduleDisplay(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.train_layout = StackLayout()

        def draw():
            self.root_layout = FloatLayout()
            self.add_widget(self.root_layout)
            bind_single(self, 'size', self.root_layout, 'size', lambda s: s)


            # Create background
            with self.canvas.before:
                Color(*blue)
                background = Rectangle(pos=(0, 0), size=(self.width, self.height))
                bind_single(self, 'size', background, 'size', lambda s: s)


            # Main layout
            main_layout = StackLayout(orientation='tb-lr', size_hint=(1, 1))
            self.root_layout.add_widget(main_layout)


            # Header
            odjazdy_label = Label(text="Odjazdy", font_size="70px", color=yellow, size_hint=(1, None), height=200)
            main_layout.add_widget(odjazdy_label)


            # Columns' sub-headers
            naglowki_layout = ClippedStackLayout(orientation='lr-tb', size_hint=(1, None), height=50)
            main_layout.add_widget(naglowki_layout)

            czas_label = Label(text="Czas", font_size="30px", color=yellow, size_hint=(None, 1), width=100)
            do_label = Label(text="Do", font_size="30px", color=yellow, size_hint=(None, 1), width=100)
            peron_label = Label(text="Peron", font_size="30px", color=yellow, size_hint=(None, 1), width=120)
            przez_label = Label(text="Przez", font_size="30px", color=yellow, size_hint=(None, 1))

            bind_single(naglowki_layout, 'width', przez_label, 'width',
                        lambda width: width - czas_label.width - do_label.width - peron_label.width)

            naglowki_layout.add_widget(czas_label)
            naglowki_layout.add_widget(do_label)
            naglowki_layout.add_widget(przez_label)
            naglowki_layout.add_widget(peron_label)


            # Train arrival display layout
            self.train_layout = StackLayout(orientation='tb-lr', size_hint=(1, None))
            bind_single(naglowki_layout, 'y', self.train_layout, 'height', lambda y: y)
            main_layout.add_widget(self.train_layout)


            # Clock
            self.clock_display = WallClockDisplay(size_hint=(None, None), size=(180, 180),
                                                  x=20, top=self.root_layout.top-20)
            self.root_layout.add_widget(self.clock_display)
            bind_single(self.root_layout, 'top', self.clock_display, 'top', lambda y: y-20)
        draw()

        self.train_queue = []
        self.trains_to_display = []

    def tick(self, dt):
        self.clock_display.tick(dt)
        self.update_trains_to_display()

    def on_touch_down(self, touch):
        super().on_touch_down(touch)

    def queue_train(self, train):
        self.train_queue.append(train)

    def update_trains_to_display(self):
        layout_height = self.train_layout.height
        single_train_height = TrainDisplay.height
        how_many_trains_will_fit = layout_height // single_train_height

        self.train_queue.sort(key=lambda t: t.czas)
        current_datetime = self.clock_display.get_datetime()
        for train in self.train_queue:
            if train.czas >= current_datetime:
                i = self.train_queue.index(train)
                self.trains_to_display = self.train_queue[i : i + how_many_trains_will_fit]
                break
        else:
            self.trains_to_display = []

        self.train_layout.clear_widgets()
        for train in self.trains_to_display:
            self.train_layout.add_widget(train)



__all__ = ['ScheduleDisplay', 'TrainDisplay']

from kivy.graphics import Color, Rectangle
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.label import Label
from kivy.uix.stacklayout import StackLayout
from kivy.uix.widget import Widget

from schedule_display.clock_display import WallClockDisplay
from train import TrainDisplay
from utensils import bind_single, ClippedStackLayout, Colors

yellow = Colors.yellow
blue = Colors.blue


class ScheduleDisplay(Widget):
    def __init__(self, database, **kwargs):
        super().__init__(**kwargs)
        self.database = database

        self.train_layout = StackLayout()

        def draw():
            self.root_layout = RelativeLayout()
            self.add_widget(self.root_layout)
            bind_single(self, 'size', self.root_layout, 'size', lambda s: s)
            bind_single(self, 'pos', self.root_layout, 'pos', lambda p: p)

            # Create background
            with self.canvas.before:
                Color(*blue)
                background = Rectangle(pos=(0, 0), size=(self.width, self.height))
                bind_single(self, 'size', background, 'size', lambda s: s)
            bind_single(self, 'pos', background, 'pos', lambda p: p)

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
            self.clock_display = WallClockDisplay(database=database, size_hint=(None, None), size=(180, 180),
                                                  x=20, top=self.root_layout.top - 20)
            self.root_layout.add_widget(self.clock_display)
            bind_single(self.root_layout, 'top', self.clock_display, 'top', lambda y: y - 20)

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
        current_datetime = self.database.get_time()
        for train in self.train_queue:
            if train.czas >= current_datetime:
                i = self.train_queue.index(train)
                self.trains_to_display = self.train_queue[i: i + how_many_trains_will_fit]
                break
        else:
            self.trains_to_display = []

        self.train_layout.clear_widgets()
        for train in self.trains_to_display:
            self.train_layout.add_widget(train)


__all__ = ['ScheduleDisplay', 'TrainDisplay']

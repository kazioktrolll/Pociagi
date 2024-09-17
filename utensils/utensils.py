from kivy.uix.stacklayout import StackLayout
from kivy.uix.stencilview import StencilView
from kivy.uix.label import Label


class Colors(object):
    white      = (1, 1, 1, 1)
    black      = (0, 0, 0, 1)
    blue       = (0.2, 0.4, 1, 1)
    light_blue = (0.4, 0.6, 1, 1)
    yellow     = (1, 1, 0, 1)


def get_bind_lambda(target, value_name, transform_lambda):
    # Example: bind child size as parent size /2
    # target: child
    # value_name: 'size'
    # transform_lambda: lambda size: (size[0] // 2, size[1] // 2)
    bind_lambda = lambda instance, value: setattr(target, value_name, transform_lambda(value))
    return bind_lambda

def bind_single(parent, parent_attr_name, child, child_attr_name, transform_lambda):
    # Example: bind child y as .5 parent height
    # bind_single(parent, 'height', child, 'y', lambda h: h // 2
    parent.bind(**{parent_attr_name: get_bind_lambda(
        child, child_attr_name, transform_lambda
    )})


class ClippedLabel(Label, StencilView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind = super().bind


class ClippedStackLayout(StackLayout, StencilView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind = super().bind


__all__ = ['ClippedLabel', 'ClippedStackLayout', 'bind_single', 'Colors']

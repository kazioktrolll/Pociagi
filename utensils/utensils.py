from kivy.uix.stacklayout import StackLayout
from kivy.uix.stencilview import StencilView
from kivy.uix.label import Label
from kivy.graphics import Rectangle, PopMatrix, PushMatrix, Rotate

from math import radians, sin, cos
from pygame.math import Vector2


class Colors(object):
    white      = (1,  1,  1,  1)
    black      = (0,  0,  0,  1)
    blue       = (.2, .4, 1,  1)
    light_blue = (.4, .6, 1,  1)
    yellow     = (1,  1,  0,  1)


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


def create_rotated_rectangle(rect_angle_deg, rect_width, rect_height, radius, center):
    angle_rad = radians(rect_angle_deg)
    center_x, center_y = center

    # Calculate rectangle position along the circle
    rect_x = center_x + radius * cos(angle_rad) - rect_width / 2
    rect_y = center_y + radius * sin(angle_rad) - rect_height / 2

    # Apply rotation to face towards the center
    PushMatrix()
    Rotate(angle=rect_angle_deg + 90,
           origin=(rect_x + rect_width / 2, rect_y + rect_height / 2))  # Rotate rectangle

    # Draw the rectangle
    Rectangle(pos=(rect_x, rect_y), size=(rect_width, rect_height))

    PopMatrix()  # Restore transformation matrix


def get_length(vector):
    return (vector[0] ** 2 + vector[1] ** 2) ** 0.5


def normalize(vector):
    l = get_length(vector)
    normalized = (vector[0] / l, vector[1] / l)
    return normalized


__all__ = ['ClippedLabel', 'ClippedStackLayout', 'bind_single', 'Colors',
           'create_rotated_rectangle', 'Vector2', 'get_length', 'normalize']

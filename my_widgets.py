"""A collection of object oriented widgets for Pyglet."""

import pyglet
from pyglet.window import mouse
from my_shapes import Rectangle
from helpers import hex_to_rgb


class Button:
    def __init__(
            self,
            root,
            x,
            y,
            w,
            h,
            text="",
            command=None,
            bg="#ffffff",
            tc="#000000",
        ):
        """Create Button Object.

        Args:
            x (int/float): x coordinate of bottom left corner
            y (int/float): y coordinate of bottom left corner
            w (int/float): width
            h (int/float): height
            text (str, optional): label on button. Defaults to ''.
            command (func, optional): Command to execute on button click. Defaults to None.
            bg (str, optional): hex color of button; Defaults to #ffffff.
            tc (str, optional): hex color of text; Defaults to #000000.
        """
        # set up button geometry
        self.base = Rectangle(x, y, w, h, bg)
        self.label = pyglet.text.Label(
            text=text,
            font_size=h * 0.75,
            bold=True,
            anchor_x="center",
            anchor_y="center",
            x=x + w // 2,
            y=y + h // 2,
            color=hex_to_rgb(tc).append(255)
        )
        def fit_label():
            """Scale label to fit inside Button."""
            if self.label.content_width > w:
                self.label.font_size -= 1
                fit_label()
            else:
                return
        fit_label()

        # send data to the window
        self.bounds = [
            x, x+w,
            y, y+h
        ]
        root.buttons.append({
            'bounds': self.bounds,
            'command': command,
            'id': text})


    def draw(self):
        """Draw Button to the window."""
        self.base.draw()
        self.label.draw()

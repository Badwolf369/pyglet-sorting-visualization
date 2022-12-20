"""Manage all output to window."""

import pyglet.gl as gl
from pyglet.window import mouse
import pyglet
from my_shapes import Rectangle
from my_widgets import Button
from helpers import hex_to_rgb


class Window(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.buttons = []
        self.controlPane = Rectangle(
            0,
            self.height - 50,
            self.width,
            50,
            '#d6d6d6'
        )
        self.sortButton = Button(
            self,
            self.width / 2 - 50,
            self.height - 45,
            100,
            40,
            text='Sort',
            bg='#bdbdbd'
        )
        self.sortButtonBorder = Rectangle(
            self.width / 2 - 50,
            self.height - 45,
            100,
            40,
            '#000000'
        )


    def on_draw(self):
        self.clear()
        self.controlPane.draw()
        self.sortButton.draw()
        self.sortButtonBorder.draw(gl.GL_LINE_LOOP)

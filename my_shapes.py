"""A collection of object oriented primitive shapes for Pyglet."""

import pyglet.gl as gl
import pyglet
from helpers import hex_to_rgb


#=============================================================================


class Rectangle():
    """An object-oriented pylget primitive rectangle.
    
    Every rectangle object must have draw() called on it every screen refresh.
    If a value is changed manually, update() must be called for it to take effect."""

    def __init__(
            self,
            x,
            y,
            w,
            h,
            fill=None,
            bd='#000000'):
        """Create a Rectangle object.

        Args:
            x (int/float): x coordinate of bottom left corner
            y (int/float): y coordinate of bottom left corner
            w (int/float): width
            h (int/float): height
            fill (str): hex color of fill; None = no fill. Defaults to None
            bd (str): hex color of border; None = no border. Defaults to None
        """
        try:
            fill = hex_to_rgb(fill)
            bd = hex_to_rgb(bd)
            self.filled_shape = pyglet.graphics.vertex_list(
                4,
                ('v2f', (x,y, x,y+h, x+w,y+h, x+w,y)),
                ('c3B', (
                    fill[0], fill[1], fill[2],
                    fill[0], fill[1], fill[2],
                    fill[0], fill[1], fill[2],
                    fill[0], fill[1], fill[2]
                ))
            )
            self.border_shape = [
                pyglet.graphics.vertex_list(
                    2,
                    ('v2f', (x,y+h, x+w,y+h),
                    ('c3B', (bd[0], bd[1], bd[2], bd[0], bd[1], bd[2])))
                ),
                pyglet.graphics.vertex_list(
                    2,
                    ('v2f', (x+w,y+h, x+w,y),
                    ('c3B', (bd[0], bd[1], bd[2], bd[0], bd[1], bd[2])))
                ),
                pyglet.graphics.vertex_list(
                    2,
                    ('v2f', (x+w,y, x,y),
                    ('c3B', (bd[0], bd[1], bd[2], bd[0], bd[1], bd[2])))
                ),
                pyglet.graphics.vertex_list(
                    2,
                    ('v2f', (x,y, x,y+h),
                    ('c3B', (bd[0], bd[1], bd[2], bd[0], bd[1], bd[2])))
                )
            ]
        except Exception:
            pass
        
        self.width = w
        self.height = h
        self.x = x
        self.y = y
        self.fill = fill
        self.border = bd
    

    def draw(self):
        """Draw Rectangle."""
        if self.fill is not None:
            self.filled_shape.draw(gl.GL_QUADS)
        if self.border is not None:
            for i in self.border_shape:
                i.draw(gl.GL_LINES)


    def update(self):
        """Update drawing to match data."""
        self.update_geometry()
        self.update_color()

    def update_geometry(self):
        """Update only the geometry of Rectangle to match data."""
        self.filled_shape.vertices = [
            self.x, self.y,
            self.x, self.y+self.height,
            self.x+self.width, self.y+self.height,
            self.x+self.width, self.y
        ]
        self.border_shape[0].vertices = [
            self.x, self.y+self.height,
            self.x+self.width, self.y+self.height
        ]
        self.border_shape[1].vertices = [
            self.x+self.width, self.y+self.height,
            self.x+self.width, self.y
        ]
        self.border_shape[2].vertices = [
            self.x+self.width, self.y,
            self.x, self.y
        ]
        self.border_shape[0].vertices = [
            self.x, self.y,
            self.x, self.y+self.height
        ]

    def update_color(self):
        """Update only color of Rectangle to match data"""
        self.filled_shape.colors = [
            self.fill[0], self.fill[1], self.fill[2],
            self.fill[0], self.fill[1], self.fill[2],
            self.fill[0], self.fill[1], self.fill[2],
            self.fill[0], self.fill[1], self.fill[2]
        ]
        for i in self.border_shape:
            i.colors = [
                self.border[0], self.border[1], self.border[2],
                self.border[0], self.border[1], self.border[2]
            ]
    

    def set_fill(self, color):
        """Change color of Rectangle.

        Args:
            color (str): new hex color; None = no fill
        """
        self.fill = hex_to_rgb(color)
        self.update_color()

    def set_border(self, color):
        """Change color of Rectangle.

        Args:
            color (str): new hex color; None = no fill
        """
        self.border = hex_to_rgb(color)
        self.update_color()
        

    def translate_by(self, tx, ty):
        """Translate Rectangle by tx and ty.

        Args:
            tx (int/float): distance to translate along x axis
            ty (int/float): distance to translate along y axis
        """
        self.x += tx
        self.y += ty
        self.update_geometry()

    def translate_to(self, x, y):
        """Translate Rectangle to x,y.

        Args:
            x (int/float): x coordinate of bottom left corner
            y (int/float): y coordinate of bottom left corner
        """
        self.x = x
        self.y = y
        self.update_geometry()


    def scale_by(self, sw, sh):
        """Scale Rectangle by sw and sh.

        Args:
            sw (int/float): width to scale by
            sh (int/float): height to scale by
        """
        self.width += sw
        self.height += sh
        self.update_geometry()

    def scale_to(self, width, height):
        """Scale Rectangle to width and height.

        Args:
            width (int/float): width to scale to
            height (int/float): height to scale to
        """
        self.width = width
        self.height = height
        self.update_geometry()


#=============================================================================
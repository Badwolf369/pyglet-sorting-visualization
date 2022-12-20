"""Start program here. Should not be edited."""

import pyglet
from gui_out import Window
from gui_in import UserIn


def main():
    window = Window(800, 450, "Bubble Sort Algorithm")
    user_in = UserIn(window)

    pyglet.app.run()


if __name__ == "__main__":
    main()

from pyglet.window import mouse

class UserIn():
    def __init__(self, window):
        self.window = window
    
        @window.event
        def on_mouse_press(x, y, mButton, modifiers):
            for b in window.buttons:
                if mButton == mouse.LEFT:
                    box = b['bounds']
                    if (box[0] <= x <= box[1] and box[2] <= y <= box[3]):
                        if b['command'] is None:
                            print(f'Click from {b["id"]}')
                        else:
                            cmd = b['command']
                            cmd()

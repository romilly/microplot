import math

import picoexplorer as display

from plots import Plotter, Frame


class ExplorerPlotter(Plotter):
    def __init__(self):
        width = display.get_width()
        height = display.get_height()
        display_buffer = bytearray(width * height * 2)
        display.init(display_buffer)

    def vert(self, l, t, b):  # left, top, bottom
        n = b - t + 1  # Vertical line
        for i in range(n):
            display.pixel(l, t + i)

    def line(self, x1, y1, x2, y2):  # (x1,y1) to (x2,y2)
        x1 = round(x1)
        y1 = round(y1)
        x2 = round(x2)
        y2 = round(y2)
        if x1 > x2:
            t = x1  # Swap co-ordinates if necessary
            x1 = x2
            x2 = t
            t = y1
            y1 = y2
            y2 = t
        if x2 - x1 == 0:  # Avoid div by zero if vertical
            self.vert(x1, min(y1, y2), max(y1, y2))
        else:  # Draw line one dot at a time L to R
            n = x2 - x1 + 1
            grad = float((y2 - y1) / (x2 - x1))  # Calculate gradient
            for i in range(n):
                y3 = y1 + int(grad * i)
                display.pixel(x1 + i, y3)  # One dot at a time

    def text(self, x, y, text):
        display.text(text, round(x), round(y), 200) # 200 needs replacing

    def default_frame(self):
        return Frame(240, 240, 20, 20, 60, 20)

    def blk(self):
        display.set_pen(0, 0, 0)
        display.clear()
        display.update()

    def show(self):
        display.update()

import math

import picoexplorer as display

from plots import Plotter, Frame


class ExplorerPlotter(Plotter):
    def __init__(self):
        Plotter.__init__(self)
        self.width = display.get_width()
        self.height = display.get_height()
        self._display_buffer = bytearray(self.width * self.height * 2)
        display.init(self._display_buffer)

    # def vert(self, l, t, b):  # left, top, bottom
    #     n = b - t + 1  # Vertical line
    #     for i in range(n):
    #         display.pixel(l, t + i)


    def line(self, x1, y1, x2, y2, color=None):
        if color is not None:
            self.set_pen(color)
        x1 = round(x1)
        y1 = round(y1)
        x2 = round(x2)
        y2 = round(y2)
        for (x, y) in self.bresenham(x1, y1, x2, y2):
            display.pixel(round(x), round(y))

    def get_pixel(self, x, y):
        start = (x + y*self.width)*2
        b_low, b_high = self._display_buffer[start:start+2]
        return b_low + b_high << 8

    def text(self, x, y, text):
        display.text(text, round(x), round(y), 200) # 200 needs replacing

    def default_frame(self):
        return Frame(240, 240, 20, 20, 60, 20)

    def blk(self):
        display.set_pen(0, 0, 0)
        display.clear()
        display.update()

    def set_pen(self, color):
        display.set_pen(*color)

    def show(self):
        display.update()
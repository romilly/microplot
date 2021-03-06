import math

import picoexplorer as display

from plotter import Plotter, Frame


class ExplorerPlotter(Plotter):
    def __init__(self):
        Plotter.__init__(self)
        self.width = display.get_width()
        self.height = display.get_height()
        self._display_buffer = bytearray(self.width * self.height * 2)
        display.init(self._display_buffer)

    def display_pixel(self, x, y):
        display.pixel(x, y)

    def get_pixel(self, x, y):
        start = x + y*self.width
        data = self._display_buffer
        # b_low, b_high = self._display_buffer[start:start+2]
        # return b_low + b_high << 8
        return (data[start * 2] << 8) + data[start * 2 + 1]

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

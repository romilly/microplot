import picoexplorer as display

from abstract_plotter import AbstractPlotter, Frame
from color import COLORS

class Plotter(AbstractPlotter):
    def __init__(self):
        AbstractPlotter.__init__(self)
        width = display.get_width()
        height = display.get_height()
        self._display_buffer = bytearray(width * height * 2)
        display.init(self._display_buffer)

    def display_pixel(self, x, y):
        display.pixel(x, y)

    def get_pixel(self, x, y):
        start = x + y*self.width()
        data = self._display_buffer
        return COLORS.rgb565_to_rgb_tuple((data[start * 2] << 8)
            + data[start * 2 + 1])

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

    def circle(self, x, y, r, color):
        self.set_pen(color)
        display.circle(x, y, r)

    def show(self):
        display.update()

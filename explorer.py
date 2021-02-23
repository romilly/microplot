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

    """Implementation of Bresenham's line drawing algorithm

        See en.wikipedia.org/wiki/Bresenham's_line_algorithm
        Code from https://github.com/encukou/bresenham
        """

    def bresenham(self, x0, y0, x1, y1):
        """Yield integer coordinates on the line from (x0, y0) to (x1, y1).
        Input coordinates should be integers.
        The result will contain both the start and the end point.
        """
        dx = x1 - x0
        dy = y1 - y0

        xsign = 1 if dx > 0 else -1
        ysign = 1 if dy > 0 else -1

        dx = abs(dx)
        dy = abs(dy)

        if dx > dy:
            xx, xy, yx, yy = xsign, 0, 0, ysign
        else:
            dx, dy = dy, dx
            xx, xy, yx, yy = 0, ysign, xsign, 0

        D = 2 * dy - dx
        y = 0

        for x in range(dx + 1):
            yield x0 + x * xx + y * yx, y0 + x * xy + y * yy
            if D >= 0:
                y += 1
                D -= 2 * dx
            D += 2 * dy

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

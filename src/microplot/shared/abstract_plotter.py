from bmp import MonoBitmapWriter


class Frame:
    def __init__(self, *specs):
        self.width, self.height, self.tm, self.bm, self.lm, self.rm = specs

    def bottom(self):
        return self.height - self.bm

    def y_span(self):
        return self.bottom() - self.tm

    def right(self):
        return self.width - self.rm


class AbstractPlotter:

    def __init__(self, frame: Frame = None):
        self.frame = frame if frame else self.default_frame()
        self.pen = None

    def line(self, x1, y1, x2, y2, color=None):
        if color is not None:
            self.set_pen(color)
        x1 = round(x1)
        y1 = round(y1)
        x2 = round(x2)
        y2 = round(y2)
        for (x, y) in self.bresenham(x1, y1, x2, y2):
            self.display_pixel(x, y)

    def width(self) -> int:
        return self.frame.width

    def height(self) -> int:
        return self.frame.height

    def text(self, x, y, text):
        pass

    def default_frame(self) -> Frame:
        pass

    def show(self):
        pass

    def get_pixel(self, x, y) -> tuple:
        pass

    def set_pen(self, color: tuple):
        self.pen = color

    def circle(self, x, y, r, color):
        pass

    def display_pixel(self, x, y):
        pass

    def write_mono_bitmap(self, file_name):
        with MonoBitmapWriter(file_name, self.frame.width, self.frame.height) as mbw:
            bytes_in_row = self.frame.width // 8
            row_bytes = bytearray(bytes_in_row)
            for i in range(self.frame.height):
                for j in range(bytes_in_row):
                    row_bytes[j] = 0
                    for k in range(8):
                        x = k + 8 * j
                        y = self.frame.height - (i + 1)
                        bit = ((0,0,0) != self.get_pixel(x, y))
                        row_bytes[j] |= bit << (7 - k)
                mbw.add_row(row_bytes)

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


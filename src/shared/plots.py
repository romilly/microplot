from bmp import MonoBitmapWriter
from colors import COLORS


class Plotter:

    def __init__(self, frame= None):
        self.frame = frame if frame else self.default_frame()
        self.pen = COLORS.BLUE

    def line(self, x1, y1, x2, y2):
        pass

    def text(self, x, y, text):
        pass

    def default_frame(self):
        pass

    def show(self):
        pass

    def get_pixel(self, x, y):
        pass

    def set_pen(self, color):
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
                        bit = (0 != self.get_pixel(x, y))
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


class Frame:
    def __init__(self, *specs):
        self.width, self.height, self.tm, self.bm, self.lm, self.rm = specs

    def bottom(self):
        return self.height - self.bm

    def y_span(self):
        return self.bottom() - self.tm

    def right(self):
        return self.width - self.rm


class Scale:
    def __init__(self, d_min, d_max, o_min, o_max):
        self.d_min = d_min
        self.d_max = d_max
        self.o_min = o_min
        self.o_max = o_max
        self.d_range = d_max - d_min
        self.o_range = o_max - o_min
        self.c = self.o_range / self.d_range

    def scale(self, val):
        return self.o_min + self.c * (val - self.d_min)


def is_iterable(data_item):
    try:
        iter(data_item)
    except TypeError:
        return False
    return True


def lol(data):
    """
    turn a one-level list into a singleton list of lists
    """
    if len(data) == 0 or is_iterable(data[0]):
        return data
    return [data]


class LinePlot:
    def __init__(self, data, title: str):
        self.data = lol(data)
        self.title = title

    def plot(self, plotter):
        frame = plotter.frame
        self.add_axes(frame, plotter, COLORS.WHITE)
        y_max = max(max(each_set) for each_set in self.data)
        y_min = min(min(each_set) for each_set in self.data)
        scale_x = Scale(0, len(self.data[0]), frame.lm, frame.right())
        plotter.text(frame.lm, frame.tm - 20, self.title)
        text_margin = 30
        scale_y = Scale(y_min, y_max, frame.bottom(), frame.tm + text_margin)
        self.add_y_scale(frame, plotter, scale_y, y_max, y_min, COLORS.WHITE)
        for (index, each_set) in enumerate(self.data):
            color = COLORS.color(index)
            coords = list(enumerate(each_set))
            old_x, old_y = coords[0]
            for new_x, new_y in coords[1:]:
                x1= scale_x.scale(old_x)
                y1 = scale_y.scale(old_y)
                x2 = scale_x.scale(new_x)
                y2 = scale_y.scale(new_y)
                plotter.line(x1, y1, x2, y2, color)
                old_x, old_y = new_x, new_y
        plotter.show()

    def add_y_scale(self, frame, plotter, scale_y, y_max, y_min, color):
        y_step = (y_max - y_min) / 10
        y_nums = list(y_min + y_step * index for index in range(11))
        y_ticks = list(scale_y.scale(y_num) for y_num in y_nums)
        for (y_num, y_tick) in zip(y_nums, y_ticks):
            plotter.text(5, round(y_tick - 10), '%4.2f' % y_num)
            plotter.line(frame.lm, round(y_tick), frame.lm - 5, round(y_tick), color)
        coords = list(enumerate(self.data))
        return coords

    def add_axes(self, frame, plotter, color):
        plotter.line(frame.lm, frame.tm + 30, frame.lm, frame.bottom(), color)
        plotter.line(frame.lm, frame.bottom(), frame.right(), frame.bottom(), color)
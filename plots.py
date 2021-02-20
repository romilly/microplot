class Plotter:
    def line(self, x1, y1, x2, y2):
        pass

    def text(self, x, y, text):
        pass

    def default_frame(self):
        pass

    def show(self):
        pass


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


class LinePlot:
    def __init__(self, list_y, title: str, frame=None):
        self.list_y = list_y
        self.title = title
        self._frame = frame

    def plot(self, plotter):
        frame = self._frame if self._frame else  plotter.default_frame()
        plotter.line(frame.lm, frame.tm, frame.lm, frame.bottom())
        plotter.line(frame.lm, frame.bottom(), frame.right(), frame.bottom())
        y_max = max(self.list_y)
        y_min = min(self.list_y)
        scale_x = Scale(0, len(self.list_y), frame.lm, frame.right())
        scale_y = Scale(y_min, y_max, frame.bottom(), frame.tm)
        y_step = (y_max - y_min) / 10
        y_nums = list(y_min + y_step*index for index in range(11))
        y_ticks = list(scale_y.scale(y_num) for y_num in y_nums)
        for (y_num, y_tick) in zip(y_nums, y_ticks):
            plotter.text(5, round(y_tick-10), '%4.2f' % y_num)
            plotter.line(frame.lm, round(y_tick), frame.lm-5, round(y_tick))
        coords = list(enumerate(self.list_y))
        old_x, old_y = coords[0]
        for new_x, new_y in coords[1:]:
            x1= scale_x.scale(old_x)
            y1 = scale_y.scale(old_y)
            x2 = scale_x.scale(new_x)
            y2 = scale_y.scale(new_y)
            plotter.line(x1, y1, x2, y2)
            old_x, old_y = new_x, new_y
        plotter.show()
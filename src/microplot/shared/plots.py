from color import COLORS

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
            color = COLORS.color(index, None)
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
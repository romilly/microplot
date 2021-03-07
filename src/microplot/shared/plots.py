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
        return round(self.o_min + self.c * (val - self.d_min))


def is_iterable(data_item):
    try:
        iter(data_item)
    except TypeError:
        return False
    return True


class Plot:
    def __init__(self, data, title: str):
        self.data = data
        self.title = title

    def add_y_scale(self, frame, plotter, scale_y, y_max, y_min, color):
        y_step = (y_max - y_min) / 10
        y_nums = list(y_min + y_step * index for index in range(11))
        y_ticks = list(scale_y.scale(y_num) for y_num in y_nums)
        for (y_num, y_tick) in zip(y_nums, y_ticks):
            plotter.text(5, round(y_tick - 10), '%4.2f' % y_num)
            plotter.line(frame.lm, round(y_tick), frame.lm - 5, round(y_tick), color)
        coords = list(enumerate(self.data))
        return coords

    def add_x_scale(self, frame, plotter, scale_x, x_max, x_min, color):
        x_step = (x_max - x_min) / 10
        x_nums = list(x_min + x_step * index for index in range(11))
        x_ticks = list(scale_x.scale(x_num) for x_num in x_nums)
        for (x_num, x_tick) in zip(x_nums, x_ticks):
            plotter.text(round(x_tick - 5), frame.bottom()+5,  '%d' % round(x_num))
            plotter.line(round(x_tick), frame.bottom(),  round(x_tick), frame.bottom()+5, color)
        coords = list(enumerate(self.data))
        return coords

    def add_axes(self, frame, plotter, color):
        plotter.line(frame.lm, frame.tm + 30, frame.lm, frame.bottom(), color)
        plotter.line(frame.lm, frame.bottom(), frame.right(), frame.bottom(), color)


class LinePlot(Plot):

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


class ScatterPlot(Plot):
    """
    Draw a scatter plot
    """

    def plot(self, plotter):
        frame = plotter.frame
        frame.bm = frame.bm+10
        self.add_axes(frame, plotter, COLORS.WHITE)
        plotter.text(frame.lm, frame.tm - 20, self.title)
        if len(self.data) == 0:
            return
        x_max = max(max((item[0]) for item in each_set) for each_set in self.data)
        x_min = min(min((item[0]) for item in each_set) for each_set in self.data)
        y_max = max(max((item[1]) for item in each_set) for each_set in self.data)
        y_min = min(min((item[1]) for item in each_set) for each_set in self.data)
        text_margin = 30
        radius = 5
        scale_x = Scale(x_min, x_max, frame.lm+radius, frame.right()-radius)
        scale_y = Scale(y_min, y_max, frame.bottom()-(radius+text_margin), frame.tm + text_margin+radius)
        self.add_y_scale(frame, plotter, scale_y, y_max, y_min, COLORS.WHITE)
        self.add_x_scale(frame, plotter, scale_x, x_max, x_min, COLORS.WHITE)
        for (index, each_set) in enumerate(self.data):
            color = COLORS.color(index)
            for x, y in each_set:
                plotter.circle(scale_x.scale(x), scale_y.scale(y), 5, color)
        plotter.show()




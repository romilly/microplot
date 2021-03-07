from microplot.shared.abstract_plotter import AbstractPlotter, Frame


class Plotter(AbstractPlotter):
    def __init__(self, frame= None):
        AbstractPlotter.__init__(self, frame)
        self.circles = []

    def circle(self, x, y, r, color):
        self.circles.append((x, y, r, color))

    def default_frame(self):
        return Frame(320, 240, 20, 20, 60, 20)
import math
from plotter import Plotter
from plots import LinePlot
from bitmap_saver import save_pixels


def row(i):
    offset = [0, 45, 90, 135, 180][i]
    return list(math.sin(math.radians(x + offset))
             for x in range(0, 361, 5))


data = list(row(i) for i in range(5))
plot = LinePlot(data,'Muli-line plot')
plotter = Plotter()
plot.plot(plotter)
save_pixels('data/demo-color24.bmp', plotter)

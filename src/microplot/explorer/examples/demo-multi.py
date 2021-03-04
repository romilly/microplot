import math
from explorer import ExplorerPlotter
from plots import LinePlot
from bitmapsaver import save_pixels


def row(i):
    offset = [0, 45, 90, 135, 180][i]
    return list(math.sin(math.radians(x + offset))
             for x in range(0, 360, 4))


data = list(row(i) for i in range(5))
plot = LinePlot(data,'Muli-line plot')
plotter = ExplorerPlotter()
plot.plot(plotter)
# plotter.write_mono_bitmap('graph.bmp')
save_pixels('cdemo.bmp', plotter)

import math
from explorer import ExplorerPlotter
from plots import LinePlot


def row(i):
    offset = [0, 45, 90, 135, 180][i]
    return list(math.sin(math.radians(x + offset))
             for x in range(0, 360, 4))


data = list(row(i) for i in range(5))

# sines = list(math.sin(math.radians(x))
#              for x in range(0, 360, 4))
#
# cosines = list(math.cos(math.radians(x))
#              for x in range(0, 360, 4))
#
# mid = list(math.sin(math.radians(x + 45))
#              for x in range(0, 360, 4))


plot = LinePlot(data,'Muli-line plot')
plotter = ExplorerPlotter()
plot.plot(plotter)
plotter.write_mono_bitmap('graph.bmp')
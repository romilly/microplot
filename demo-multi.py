import math
from explorer import ExplorerPlotter
from plots import LinePlot

sines = list(math.sin(math.radians(x))
             for x in range(0, 360, 4))

cosines = list(math.cos(math.radians(x))
             for x in range(0, 360, 4))

mid = list(math.sin(math.radians(x + 45))
             for x in range(0, 360, 4))


plot = LinePlot((sines, cosines, mid),'MicroPlot line')
plotter = ExplorerPlotter()
plot.plot(plotter)
plotter.write_mono_bitmap('graph.bmp')
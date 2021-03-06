import math
from clue import CluePlotter
from plots import LinePlot

sines = list(math.sin(math.radians(x))
             for x in range(0, 360, 4))

plot = LinePlot(sines,'MicroPlot line')
plotter = CluePlotter()
plot.plot(plotter)
while True:
    pass
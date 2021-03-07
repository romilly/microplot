import math
from plotter import Plotter
from plots import LinePlot

sines = list(math.sin(math.radians(x))
             for x in range(0, 361, 4))

plot = LinePlot([sines],'MicroPlot line')
plotter = Plotter()
plot.plot(plotter)
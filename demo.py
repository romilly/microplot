import math
from explorer import ExplorerPlotter
from plots import LinePlot

sines = list(math.sin(math.radians(x)) for x in range(0, 360, 4))

plot = LinePlot((sines),'MicroPlot line')
plot.plot(ExplorerPlotter())
import math
from plotter import Plotter
from plots import LinePlot

def run():
    sines = list(math.sin(math.radians(x))
                 for x in range(0, 361, 5))
    plot = LinePlot([sines],'MicroPlot line')
    plotter = Plotter()
    plot.plot(plotter)
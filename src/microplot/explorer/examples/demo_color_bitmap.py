import math
from plotter import Plotter
from plots import LinePlot
from bitmapsaver import save_pixels


def run():
    sines = list(math.sin(math.radians(x))
                 for x in range(0, 361, 4))
    plot = LinePlot([sines],'MicroPlot line')
    plotter = Plotter()
    plot.plot(plotter)
    save_pixels('color-plot.bmp', plotter)    


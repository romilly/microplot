import math
from explorer import ExplorerPlotter
from plots import LinePlot
from bitmapsaver import save_pixels

sines = list(math.sin(math.radians(x))
             for x in range(0, 360, 4))

plot = LinePlot([sines],'MicroPlot line')
plotter = ExplorerPlotter()
plot.plot(plotter)
#plotter.write_mono_bitmap('mono.bmp')
# save_pixels('demo1.bmp', plotter)
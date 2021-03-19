from plotter import Plotter
from plots import ScatterPlot

data = [[(20, 30), (40, 50), (10, 90), (60, 60)], [(10, 25), (45, 65)], [(33, 70)]]

plot = ScatterPlot(data, 'Scatter Plot', "Triangle")
plotter = Plotter()
plot.plot(plotter)
while True:
    pass
